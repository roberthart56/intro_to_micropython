# Input Device:  Hall sensor for magnetic field detection.

A hall sensor outputs a voltage from 0 to 3.3V that corresponds to the magnetic field that is directed through its package.  See the data sheet for details: [link to datasheet](https://www.akm.com/content/dam/documents/products/magnetic-sensor/linear-hall-effect-ic/eq731l/eq731l-en-datasheet.pdf) 

Two pins of the sensor are attached to ground and to 3.3V.  The voltage of the third pin is read by one of the microcontroller pins that is capable of analog to digital conversion (ADC).  It reports voltages as numbers in the range 0 - 65536 (2 to the power 16).


<br><br>


<figure>
  <img src="./images/mag_circuit.jpg" width="400" alt="my alt text"/>
  <figcaption>Magnetic field detection circuit.</figcaption>
</figure>

<figure>
  <img src="./images/mag_side_pic.jpg" width="400" alt="my alt text"/>
  <figcaption>Hall sensor, side view.</figcaption>
</figure>


<br><br>

<figure>
  <img src="./images/mag_top_pic.jpg" width="400" alt="my alt text"/>
  <figcaption>Hall sensor on a breadboard attached to a pin of a microcontroller module. Top view. </figcaption>
</figure>

