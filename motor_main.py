##################################################
#                                                #
# Program:                                       #
#       motor_main.py                            #
# History:                                       #
#       2021/09/15                               #
# < using 4-steps step motor >                   #
#                                                #
##################################################

from motor_function import motor_init, motor_run, motor_param

# <motor parameter setting> 
#     <set motor output pins> 
motor1 = [17, 18, 27, 22] 
motor2 = [10, 9, 11, 8]
#     </set motor output pins>      
# </motor parameter setting> 

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
            # select motor and duration
            print('[which motor to run] (1: motor1, 2: motor 2) ')
            print('[duration time] (unit: second) ')
            print('[MODE] (mode1: clockwise -> counterwise, mode2: counterwise -> clockwise )')
            motorSelect, duration, MODE = input().split()
            MOTOR_SELECT = int(motorSelect)
            DURATION = int(duration)
            if motorSelect == 1:
                # motor_run(OUTPUTPINS, MODE, DURATION, MOTOR_STEPS, SEQUENCE, SEQUENCE_COUNT, PIN_COUNT)
                motor_run(motor1, MODE, DURATION, MOTOR1_STEPS)
            if motorSelect == 2:
                # motor_run(OUTPUTPINS, MODE, DURATION, MOTOR_STEPS, SEQUENCE, SEQUENCE_COUNT, PIN_COUNT)
                motor_run(motor2, MODE, DURATION, MOTOR2_STEPS)
            
    except KeyboardInterrupt:  
        print('Program Closed.')
    finally:
        gpio.cleanup()
