from espeak import espeak
from motion import Motion
from vision import Vision

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

motion = Motion()
vision = Vision()

motion.start()
vision.start()

while True:
  c = getchar()
  if c == 'w':
    motion.forward()
  elif c == 's':
    motion.backward()
  elif c == 'a':
    motion.left()
  elif c == 'd':
    motion.right()
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
  elif c == ';':
    espeak.synth("HI SNUGGLES")
  elif c == 'q':
    motion.stop()
    vision.stop()
    quit()
  else:
    motion.stop()
