# %%
from GUI_function import Tkwindow, Custom, Sweet
#from motor_function import motor_init, motor_run, motor_param, calVolume
#import RPi.GPIO as GPIO

# ====== <parameter> ====== #
SWEETNESS_ENABLE = False
SWEETNESS = 'Normal Sweet'
ACIDITY_ENABLE = False
ACIDITY = 0
# ====== </parameter> ====== #

root = Tkwindow()
'''
if __name__ == "__main__":
    
    # setting motor duration
    # >>> python motor_main.py <motor1 steps> <motor2 steps>
    MOTOR1_STEPS, MOTOR2_STEPS = motor_param()

    # initial motor 1
    MOTOR1_SEQUENCE, MOTOR1_SEQUENCE_COUNT, MOTOR1_PIN_COUNT = motor_init(motor1)
    # initial motor 2
    MOTOR2_SEQUENCE, MOTOR2_SEQUENCE_COUNT, MOTOR2_PIN_COUNT = motor_init(motor2)
    
    # program start
    try:
        print('Ress Ctrl-C to stop the program.')
        while True:
            # open GUI
            root = Tkwindow()

            # select motor and duration
            MOTOR_SELECT = int(input('[which motor to run] (1: motor1, 2: motor 2): '))
            DURATION = int(input('[duration time] (unit: second): '))
            MODE = int(input('[MODE] (1: clockwise -> counterwise, 2: counterwise -> clockwise ): '))
            #motorSelect, duration, MODE = input('>>> ').split()
            #MOTOR_SELECT = int(motorSelect)
            #DURATION = int(duration)
            print('MOTOR_SELECT: ', MOTOR_SELECT)
            print('DURATION: ', DURATION)
            print('MODE: ', MODE)
            
            if MOTOR_SELECT == 1:
                # motor_run(OUTPUTPINS, MODE, DURATION, MOTOR_STEPS, SEQUENCE, SEQUENCE_COUNT, PIN_COUNT)
                motor_run(motor1, MODE, DURATION, MOTOR1_STEPS)
            if MOTOR_SELECT == 2:
                # motor_run(OUTPUTPINS, MODE, DURATION, MOTOR_STEPS, SEQUENCE, SEQUENCE_COUNT, PIN_COUNT)
                motor_run(motor2, MODE, DURATION, MOTOR2_STEPS)
            
    except KeyboardInterrupt:  
        print('Program Closed.')
    finally:
        GPIO.cleanup()
'''
# %%
