import RPi.GPIO as GPIO

pins = [17, 27, 22, 23]
lf = 0
lr = 1
rf = 2
rr = 3

class Motion(object):
    def start(self):
        GPIO.setmode(GPIO.BCM)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def stop(self):
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)

    def left(self):
        self.stop()
        GPIO.output(pins[lr], GPIO.HIGH)
        GPIO.output(pins[rf], GPIO.HIGH)

    def right(self):
        self.stop()
        GPIO.output(pins[lf], GPIO.HIGH)
        GPIO.output(pins[rr], GPIO.HIGH)

    def forward(self):
        self.stop()
        GPIO.output(pins[lf], GPIO.HIGH)
        GPIO.output(pins[rf], GPIO.HIGH)

    def backward(self):
        self.stop()
        GPIO.output(pins[lr], GPIO.HIGH)
        GPIO.output(pins[rr], GPIO.HIGH)
