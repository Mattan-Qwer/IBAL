# working Title: IBAL 
A modular lamp and display project to spend light and help with time management.

## Requirements
- Show the clock in the LEDs
- Show a timer in the LEDs
- Lamp with different Colors and Temperatures of Light
- Controlable over LCD and turn decoder


## Development
See also the mindmap file.
### Hardware
First hardware from 23.08.2021 has following constrains.

* 5A * 5V AC/DC converter
** is at hand
** is a little bit to small for all LEDs at the same time in full brigthness
* 241 ws2812 in multiple rings
** this is the given LED display/lamp
* ESP8266 in form of NodeMCU
** very powerfull und capebile for extenstions
** has 3,3V Pins, so a voltage level shift for the LED and maybe LCD is needed
* 2 line 16 charakter display with i2C connection board
** standard LCD Display (cheap and in storage)
* 2 turn decoders for input
** my favorite input device
** digital feedback over potiontiometer and endless scrolling ...

### Electronics
First revision of the pcb is in production, should be with me till end of septmber.

### Software

#### Arduino is in progress
#### picture converter
Picture converter for the polar coordinat display is done.
Not testet with real hardware yet.



