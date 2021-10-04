from GUI_function import Tkwindow, Custom, Sweet
import RPi.GPIO as GPIO

# ====== <parameter> ====== #
SWEETNESS_ENABLE = False
SWEETNESS = 'Normal Sweet'
ACIDITY_ENABLE = False
ACIDITY = 0
# ====== </parameter> ====== #

if __name__ == "__main__":    
    # program start
    try:
        print('Ress Ctrl-C to stop the program.')
        while True:
            # open GUI
            root = Tkwindow()
            
    except KeyboardInterrupt:  
        print('Program Closed.')
    finally:
        GPIO.cleanup()
        print('GPIO clean up.')
