# Output device:  DC motors.

Motor control is one of the best things to do with microcontrollers, but it requires a bit more electronics than just connecting to a microcontroller pin, as you would an LED.  Why?
 
- Most motors require more current than microcontroller pins can provide.
- Usually, you want to drive motors in both directions.
- When motors are stopped, they can generate big voltages (think sparks) that can damage electronics.

One way to drive a small motor is shown below, where a small [board from pololu.com](https://www.pololu.com/product/4733) is used to drive a motor both ways.  I like this solution because it is small and easy to put into a project.  The motor is powered from the 5V pin of the microcontroller.  The direction and speed are controlled by the pins attached to the yellow wires in the picture.  For details, see the Pololu website linked above.

<figure>
  <img src="./images/pololu_pic.jpg" width="400" alt="my alt text"/>
  <figcaption>Motor driven with Pololu #4733 board. .</figcaption>
</figure>

<br><br>
Another way to drive up to two motors is the use the [other driver in your kit](https://www.amazon.com/dp/B0D95GBYQF?ref=ppx_yo2ov_dt_b_fed_asin_title), based on the L298N chip.  There are many tutorials on the internet for using this driver.  (It can be used to drive a stepper motor which gives you very good control over rotation angle.)

A final way, if you only want to drive in one direction, is to use a transistor.  We have included a few 
field effect transistors (FETs) in your kit.  An explanation of how to use one to drive a motor is given 
[here](https://roberthart56.github.io/SCFAB/SC_lab/Output_Devices/FET/index.html)


