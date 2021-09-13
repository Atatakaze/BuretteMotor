##################################################
# ============================================== #
# ====== <step motor ( 4 step sequence )> ====== #
# ====== <last modeified: 2021/09/13> ========== #
# ============================================== #
##################################################

import RPi.GPIO as gpio
import time
import sys
from array import array
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# ====== <motor parameters> ====== #
STEPS_PER_REVOLUTION = 32*64
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
SEQUENCE_REVERSE = [[1, 1, 0, 0],
		    [1, 0, 0, 1],
		    [0, 0, 1, 1],
		    [0, 1, 1, 0]]
# ====== </motor parameter> ====== #

SEQUENCE_COUNT = len(SEQUENCE)
PIN_COUNT = len(pin)

sequence_index = 0
direction = 1
steps = 0
duration_count = 0

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

# ====== <motor mode 1> ====== #
def SPIN():
  print('Start working ...')

  duration_count = 0
  global sequence_index, steps, direction

  while duration_count < duration_time:
    for i in range(PIN_COUNT):
      gpio.output(pin[i], SEQUENCE[sequence_index][i])
      time.sleep(0.01)
    steps += direction
    if steps >= STEPS_PER_REVOLUTION:
      direction = -1
    elif steps < 0:
      direction = 1

    sequence_index += direction
    sequence_index %= SEQUENCE_COUNT

    print('index={}, direction={}'.format(sequence_index, direction))
    time.sleep(wait_time)
    duration_count += 1
  print('Finished !')
# ====== </motor mode1>

# ====== <motor mode 2> ====== #
def SPIN_REVERSE():
  print('Start working ...')

  duration_count = 0
  global sequence_index, steps, direction
  
  while duration_count < duration_time:
    for i in range(PIN_COUNT):
      gpio.output(pin[i], SEQUENCE_REVERSE[sequence_index][i])
      time.sleep(0.01)
    steps += direction
    if steps >= STEPS_PER_REVOLUTION:
      direction = -1
    elif steps < 0:
      direction = 1

    sequence_index += direction
    sequence_index %= SEQUENCE_COUNT

    print('index={}, direction={}'.format(sequence_index, direction))
    time.sleep(wait_time)
    duration_count += 1
  print('Finished !')
# ====== </motor mode2>

# ====== <main program> ====== #
try:
  print('Ress Ctrl-C to stop the program.')
  while True:
    mode = int(input('Select which mode to run :'))
    if mode == 1:
      print('Mode 1 => motor rotates clockwise')
      SPIN()
    elif mode == 2:
      print('Mode 2 => motor rotates counterwise')
      SPIN_REVERSE()
    else :
      print('Please enter 1 or 2')

except KeyboardInterrupt:
  print('Program Closed.')
finally:
  gpio.cleanup()
# ====== </main program> ====== #

