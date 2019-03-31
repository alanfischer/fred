#!/usr/bin/python3

from espeak import espeak
from motion import Motion
from vision import Vision
import logging

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s\r\n', datefmt='%H:%M:%S')


motion = Motion()
vision = Vision()

motion.start()
vision.start()

while True:
  c = getchar()
  if c == 'q':
    motion.direction([-.7,.7])
  elif c == 'w':
    motion.forward()
  elif c == 'e':
    motion.direction([.7,.7])
  elif c == 'x':
    motion.backward()
  elif c == 'a':
    motion.left()
  elif c == 'd':
    motion.right()
  elif c == 'z':
    motion.direction([-.7,-.7])
  elif c == 'c':
    motion.direction([.7,-.7])
  elif c == 'g':
    espeak.synth("HI GUS GUS")
  elif c == 'h':
    espeak.synth("HI CLAIRE")
  elif c == 'j':
    espeak.synth("HI SAMMY")
  elif c == 'k':
    espeak.synth("HI AILIS")
  elif c == 'l':
    espeak.synth("HI ARDAN")
  elif c == 'f':
    espeak.synth("I AM FRED")
  elif c == '`':
    motion.stop()
    vision.stop()
    quit()
  else:
    motion.stop()
