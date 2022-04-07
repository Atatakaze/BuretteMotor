# **BuretMotor** #

***

## **Settings:** ##

**PATH** = "~/Documents/TEL_lab/RedWine/"

**Environment:** Python3, tkinter, RPi.GPIO

## **Program:** ##

> Using Raspberry Pi to control the motor that is installed on a burette, thus mixing two wines in a specific ratio.  

## **Instruction:** ##

- ### GUI_main.py ### 

   Run `GUI_main.py` to launch this program with GUI. 
   
   ( including `GUI_function.py` and `motor_function.py` )
    
   **GUI**
   
   - Initial Windows
      
      Choose which mode to run, auto mode or custom mode? 
      
      *( auto mode: Automatically mix two wines with the ratio that yields the highest score. )*
      
      *( custom mode: Enable user to customize their flavor according to their own taste. )*
     
      <img height="100" src="https://user-images.githubusercontent.com/89720769/162132113-23826edc-8384-4a5c-9b29-9fefc447299b.png"> 
   
   - Auto Mode
   
      <img height="100" src="https://user-images.githubusercontent.com/89720769/162134602-4e8a02b3-14eb-4e18-bf15-4cf7695d5a6f.png">
      
   - Custom Mode
      
      1. Choose what you would like to adjust.
    
         <img height="100" src="https://user-images.githubusercontent.com/89720769/162134943-dc7698b3-fc89-4bb2-b2b1-7d26e5c5edfe.png">
      
      2. Customize your flavor
      
         <center class="half">
            <img height="200" src="https://user-images.githubusercontent.com/89720769/162134968-dd1d4120-3440-4148-9878-2f5b7da665a8.png"><img width="2" src="https://user-images.githubusercontent.com/89720769/162136570-e6ee67e5-529c-4921-ac0d-bad1658d6818.png"><img height="200"  src="https://user-images.githubusercontent.com/89720769/162134985-0b83d196-6470-45ff-bff3-b91a1d27384e.png">
         </center>
     
      3. Confirmation
   
         <img height="100" src="https://user-images.githubusercontent.com/89720769/162135000-3f7f0cd8-9761-44a2-a9c3-f1667bf77938.png">

   - Finish Windows 
   
      Inform the user that the process is finished and the score of their mixing.
      
      <center class="half">
         <img height="100" src="https://user-images.githubusercontent.com/89720769/162138284-f0f9e876-eb9e-4fc0-a116-a80c9be0427c.png"><img width="2" src="https://user-images.githubusercontent.com/89720769/162136570-e6ee67e5-529c-4921-ac0d-bad1658d6818.png"><img height="100"  src="https://user-images.githubusercontent.com/89720769/162138293-d0cc0749-4e2a-49e1-afc1-92c726cf2898.png">
      </center>
     
- ### motor_main.py & motor_function.py ### 

   Run `motor_main.py` to launch this program with command line. 
   
   ( including `motor_function.py` )
    
   *\<motor1 steps> is the steps needed when motor1 open or close the burette. (defualt 100)* 
     
   *\<motor2 steps> is the steps needed when motor2 open or close the burette. (default 100)* 
     
     
   ``` python
   $ python motor_main.py <motor1 steps> <motor2 steps>
   ```
    
   *\<which motor to run> (1: motor1, 2: motor 2)* 
     
   *\<duration time> (unit: second) -> volume(ml) = 5.46 \* duration(s) + 3.19* 
     
   *\<MODE> (mode1: clockwise -> counterwise, mode2 counterwise -> clockwise )* 

- ### MotorTesting ###  
    
   These codes are used to check if our burette motor works proporly and measure the relationship between volume and the duration time that the burette stays open. 
   
   - ### motor_main_test.py & motor_function_test.py ###

      Run `motor_main_test.py` to open and close burette.  
     
      *\<motor1 speed> is the rotating speed of motor1. (default 10)* 
     
      *\<motor1 duration> is the steps that motor1 rotates. (default 100)* 
     
      *\<motor2 speed> is the rotating speed of motor2. (default 10)* 
     
      *\<motor2 duration> is the steps that motor2 rotates. (default 100)* 
    
      ``` python
      $ python motor_main_test.py <motor1 speed> <motor1 duration> <motor2 speed> <motor2 duration>
      ```
    
      **which motor to run** *(1: motor1, 2: motor 2)* 
     
      **which direction to rotate** *(1: clockwise, -1: counterwise)* 
    
    
