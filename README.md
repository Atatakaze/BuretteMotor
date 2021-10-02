# **BuretMotor** #

***

**PATH = "~/Documents/TEL_lab/RedWine/"**

## **Program:** ##

> Using Raspberry Pi to control the motor that is installed on a burette. 

## **Instruction:** ##

- ### motor_main.py & motor_function.py ### 

   Run `motor_main.py` to open and close the burette. 
    
     *\<motor1 steps> is the steps needed when motor1 open or close the burette. (defualt 100)* 
     
     *\<motor2 steps> is the steps needed when motor2 open or close the burette. (default 100)* 
     
     
``` python
>>> python motor_main.py <motor1 steps> <motor2 steps>
```
    
   *\<which motor to run> (1: motor1, 2: motor 2)* 
     
   *\<duration time> (unit: second) -> volume(ml) = 5.46 \* duration(s) + 3.19* 
     
   *\<MODE> (mode1: clockwise -> counterwise, mode2 counterwise -> clockwise )* 
    
- ### motor_main_test.py & motor_function_test.py ###

    Run `motor_main_test.py` to open and close burette.  
     
     *\<motor1 speed> is the rotating speed of motor1. (default 10)* 
     
     *\<motor1 duration> is the steps that motor1 rotates. (default 100)* 
     
     *\<motor2 speed> is the rotating speed of motor2. (default 10)* 
     
     *\<motor2 duration> is the steps that motor2 rotates. (default 100)* 
    
     
``` python
>>> python motor_main_test.py <motor1 speed> <motor1 duration> <motor2 speed> <motor2 duration>
```
    
   *\<which motor to run> (1: motor1, 2: motor 2)* 
     
   *\<which direction to rotate> (1: clockwise, -1: counterwise):* 
   
- ### GUI_main.py & GUI_function.py ### 

   Run `GUI_main.py` to open GUI. 
    
     *Using class to define different windows.*

- ### GUI_UsingFunctionDefine.py ###  
    
     *Using functions to define different windows. (abandon)*    
    
    
