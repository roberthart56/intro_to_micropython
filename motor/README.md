# Output device:  DC motors.

Motor control is one of the best things to do with microcontrollers, but it requires a bit more electronics than just connecting to a microcontroller pin, as you would an LED.  Why?
 
- Most motors require more current than microcontroller pins can provide.
- Usually, you want to drive motors in both directions.
- When motors are stopped, they can generate big voltages (think sparks) that can damage electronics.
- 

<br><br>


<figure>
  <img src="./images/led_circuit.png" width="400" alt="my alt text"/>
  <figcaption>LED equivalent circuit.</figcaption>
</figure>

<br><br>

<figure>
  <img src="./images/led_physical.jpg" width="400" alt="my alt text"/>
  <figcaption>LED on breadboard attached to a pin of a microcontroller module.</figcaption>
</figure>

