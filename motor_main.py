##################################################
#                                                #
# Program:                                       #
#       motor_main.py                            #
# History:                                       #
#       2021/09/14                               #
# < using 4-steps step motor >                   #
#                                                #
##################################################

from motor_function import motor_init, motor_run
import sys

# <motor parameter setting> 
#     <set motor output pins> 
motor1 = [17, 18, 27, 22] 
#motor2 = []
#     </set motor output pins>      
# </motor parameter setting> 

if __name__ == "__main__":
    
    # setting motor speed and duration
    # >>> python motor_main.py <motor1 speed> <motor1 duration> <motor2 speed> <motor2 duration>
    if len(sys.argv) == 2:
        motor1_speed = int(sys.argv[1])/float(1000)
        motor1_duration = 100
        motor2_speed = 10/float(1000)
        motor2_duration = 100
    elif len(sys.argv) == 3:
        motor1_speed = int(sys.argv[1])/float(1000)
        motor1_duration = int(sys.argv[2])
        motor2_speed = 10/float(1000)
        motor2_duration = 100
    elif len(sys.argv) == 4:
        motor1_speed = int(sys.argv[1])/float(1000)
        motor1_duration = int(sys.argv[2])
        motor2_speed = int(sys.argv[3])/float(1000)
        motor2_duration = 100
    elif len(sys.argv) == 5:
        motor1_speed = int(sys.argv[1])/float(1000)
        motor1_duration = int(sys.argv[2])
        motor2_speed = int(sys.argv[3])/float(1000)
        motor2_duration = int(sys.argv[4])
    else:
        motor1_speed = 10/float(1000)
        motor1_duration = 100
        motor2_speed = 10/float(1000)
        motor2_duration = 100
    
    # initial motor 1
    motor1_SEQUENCE, motor1_SEQUENCE_COUNT, motor1_PIN_COUNT = motor_init(motor1)
    # initial motor 2
    #motor2_SEQUENCE, motor2_SEQUENCE_COUNT, motor2_PIN_COUNT = motor_init(motor2)
    
    # program start
    try:
        print('Ress Ctrl-C to stop the program.')
        while True:
            # select motor
            motor = int(input('Select which motor to run :'))
            # select direction
            direction = int(input('Select which direction to run (1: clockwise, 2: counterwise): '))
            # motor_run(motor, Direction, SEQUENCE, Duration, Speed, SEQUENCE_COUNT, PIN_COUNT)
            motor_run(motor1, direction, motor1_SEQUENCE, motor1_duration, motor1_speed, motor1_SEQUENCE_COUNT, motor1_PIN_COUNT)
            # motor_run(motor, Direction, SEQUENCE, Duration, Speed, SEQUENCE_COUNT, PIN_COUNT)
            #motor_run(motor2, direction, motor2_SEQUENCE, motor2_duration, motor2_speed, motor2_SEQUENCE_COUNT, motor2_PIN_COUNT)
    except KeyboardInterrupt:  
        print('Program Closed.')
    finally:
        gpio.cleanup()
