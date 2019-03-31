import RPi.GPIO as GPIO
import numpy.linalg as la

pins = [17, 27, 22, 23]
lf = 0
lr = 1
rf = 2
rr = 3

class Motion(object):
    pwms = [None] * 4

    def start(self):
        GPIO.setmode(GPIO.BCM)
        for i, pin in enumerate(pins):
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
            self.pwms[i] = GPIO.PWM(pin, 30)

    def stop(self):
        for pwm in self.pwms:
            pwm.stop()

    def direction(self, d):
        md = [0,0]
        if d[0] >= 0 and d[1] >= 0:
            md[0] = 1
            md[1] = -(d[0]*2 - 1)
        elif d[0] < 0 and d[1] >= 0:
            md[0] =  (d[0]*2 + 1)
            md[1] = 1
        elif d[0] >= 0 and d[1] < 0:
            md[0] =  (d[0]*2 - 1)
            md[1] = -1
        else:
            md[0] = -1
            md[1] = -(d[0]*2 + 1)

        len = la.norm(d)
        if len > 1:
            len = 1

        f = 60
        l = abs(md[0]) * f * len
        r = abs(md[1]) * f * len
        if md[0] > 0:
            self.pwms[lf].start(l)
            self.pwms[lr].stop()
        else:
            self.pwms[lr].start(l)
            self.pwms[lf].stop()
        if md[1] > 0:
            self.pwms[rf].start(r)
            self.pwms[rr].stop()
        else:
            self.pwms[rr].start(r)
            self.pwms[rf].stop()

    def left(self):
        self.direction([-1, 0])

    def right(self):
        self.direction([1, 0])

    def forward(self):
        self.direction([0, 1])

    def backward(self):
        self.direction([0, -1])
