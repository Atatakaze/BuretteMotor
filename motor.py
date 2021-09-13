import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

pin = [29, 31, 33, 35]
for i in range(4):
  gpio.setup(pin[i], gpio.OUT)

forward_seq = ['0010', '0100', '1000', '0001']
reverse_seq = ['0010', '0001', '1000', '0100']

def forward(steps, delay):
  for i in range(steps):
    for step in forward_seq:
      set_motor(step)
      time.sleep(delay)

def reverse(steps, delay):
  for i in range(steps):
    for step in reverse_seq:
      set_motor(step)
      time.sleep(delay)

def set_motor(step):
  for i in range(4):
    gpio.output(pin[i], step[i] == '1')

set_motor('0000')
forward(180, 0.1)
#set_motor('0000')
#reverse(180, 0.01)

