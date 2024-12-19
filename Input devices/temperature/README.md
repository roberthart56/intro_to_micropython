# Input Device to measure temperature:  Thermistor.

A thermistor is a temperature-dependent resistor.  It is attached in series to another resistor, a configuration called a voltage divider.  When its temperature changes, the voltage between the two resistors changes.

The voltage at the middle of the voltage divider is read by one of the microcontroller pins that is capable of analog to digital conversion (ADC).  It reports voltages as numbers in the range 0 - 65536 (2 to the power 16).


<br><br>


<figure>
  <img src="./images/temperature_circuit.jpg" width="400" alt="my alt text"/>
  <figcaption>Thermistor circuit.</figcaption>
</figure>

<br><br>

<figure>
  <img src="./images/thermistor_pic.jpg" width="400" alt="my alt text"/>
  <figcaption>Thermistor circuit on a breadboard attached to a pin of a microcontroller module.</figcaption>
</figure>


### Measuring temperature.

Here is one way to use the thermistor to make a practical thermometer that can be put in water.  First, solder wire leads to the thermistor wires.

<figure>
  <img src="./images/Th_solder.jpg" width="400" alt="my alt text"/>
  <figcaption>Thermistor soldered.</figcaption>
</figure>

Cover the leads in heat shrink tubing to protect from shorting together.
<br>

<figure>
  <img src="./images/Th_shrink.jpg" width="400" alt="my alt text"/>
  <figcaption>Thermistor leads with shrink tube.</figcaption>
</figure>
<br>

Encase the first few cm in more shrink tube, and seal the bead with epoxy to keep water out.

<figure>
  <img src="./images/Th_epoxy.jpg" width="400" alt="my alt text"/>
  <figcaption>Thermistor encased in shrink tube with epoxy on the tip.</figcaption>
</figure>


