##################################################
# ============================================== #
# ====== <step motor ( 8 step sequence )> ====== #
# ====== <last modified: 2021/09/10 > ========== #
# ============================================== #
##################################################

import RPi.GPIO as gpio
import time
import sys
from array import array
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# ====== <motor parameters> ====== #
STEPS_PER_REVOLUTION = 64*64
# ====== <select output pins> ====== #
pin = [17, 18, 27, 22]
# ====== <set output pins> ====== #
for i in range(4):
  gpio.setup(pin[i], gpio.OUT)
  gpio.output(pin[i], gpio.LOW)
# ====== <sequence> ====== #
SEQUENCE = [[1, 0, 0, 0],
	    [1, 1, 0, 0],
	    [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]]
# ====== </motor parameter> ====== #

SEQUENCE_COUNT = len(SEQUENCE)
PIN_COUNT = len(pin)

sequence_index = 0
direction = 1
steps = 0

# ====== <control speed> ====== #
if len(sys.argv) > 1:
  wait_time = int(sys.argv[1])/float(1000)
else:
  wait_time = 10/float(1000)
# ====== </control speed> ====== #

# ====== <main program> ====== #
try:
  print('Ress Ctrl-C to sto pthe program.')
  while True:
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

except KeyboardInterrupt:
  print('Program Closed.')
finally:
  gpio.cleanup()
# ====== </main program> ====== #

