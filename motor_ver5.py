##################################################
# ============================================== #
# ====== <step motor ( 4 step sequence )> ====== #
# ====== <last modeified: 2021/09/14> ========== #
# ============================================== #
##################################################

import RPi.GPIO as gpio
import time
import sys
from array import array
gpio.setmode(gpio.BCM)      # select BCM mode
gpio.setwarnings(False)     # disable warning message

# ====== <motor parameters> ====== #
# ====== <select output pins> ====== #
pin = [17, 18, 27, 22]      
# ====== <set output pins> ====== #
for i in range(4):
  gpio.setup(pin[i], gpio.OUT)
  gpio.output(pin[i], gpio.LOW)
# ====== <sequence> ====== #
SEQUENCE = [[1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1]]
# ====== </motor parameter> ====== #

SEQUENCE_COUNT = len(SEQUENCE)
PIN_COUNT = len(pin)

sequence_index = 0      # step status
direction = 1       # rotate direction (1->clockwise, 2->counterwise)
duration_count = 0      # mode duration(default = 100)

# ====== <control speed and duration> ====== #
if len(sys.argv) == 2:
  wait_time = int(sys.argv[1])/float(1000)
  duration_time = 100
elif len(sys.argv) == 3:
  wait_time = int(sys.argv[1])/float(1000)
  duration_time = int(sys.argv[2])
else:
  wait_time = 10/float(1000)
  duration_time = 100
# ====== </control speed> ====== #

# ====== <motor rotate> ====== #
def SPIN(direction):
  print('Start working ...')

  duration_count = 0
  global sequence_index, direction

  while duration_count < duration_time:
    for i in range(PIN_COUNT):
      gpio.output(pin[i], SEQUENCE[sequence_index][i])
      time.sleep(0.01)

    sequence_index += direction
    sequence_index %= SEQUENCE_COUNT

    print('index={}, direction={}'.format(sequence_index, direction))
    time.sleep(wait_time)
    duration_count += 1
  print('Finished !')
# ====== </motor mode1>

# ====== <main program> ====== #
try:
  print('Ress Ctrl-C to stop the program.')
  while True:
    mode = int(input('Select which mode to run :'))
    if mode == 1:
      print('motor rotates clockwise')
      SPIN(1)
    elif mode == 2:
      print('motor rotates counterwise')
      SPIN(-1)
    else :
      print('Please enter 1 or 2')

except KeyboardInterrupt:
  print('Program Closed.')
finally:
  gpio.cleanup()
# ====== </main program> ====== #

