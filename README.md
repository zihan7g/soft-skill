# Simple Relay Control Via Serial

Simple Relay Control Via Serial


## Components

1. Hardware
2. relay_sketch.ino
3. relay.py


## Wiring Diagram

## Prerequisites (installation)

1. PySerial package. To install, type the following from the command prompt:
“pip install pyserial”
  
## Usage instructions (as a library)

1. Launch “idle” on window
2. Type: “import os;print(os.getcwd())"
3. Copy “relay.py” to subdirectory “Lib” within the folder above (displayed in idle in blue)
4. Now you can use the library using “import relay” then calling the following functions:
5. Note that if the hardware is not connected, then an exception will be thrown when importing the library
6. Note that if the hardware is connected but being used by another program, an exception will also be thrown when importing the library

## Usage instructions (from the command line)

1. To turn on the relay from the command line, go to the folder where “relay.py” is stored and type the following command:

     a. “python relay.py 1” turns the relay on

     b. “python relay.py 0” turns the relay off

2. Note that if the hardware is not connected, an error message will be displayed.
3. Note that if the hardware is connected but being used by another program, an error message will be displayed
