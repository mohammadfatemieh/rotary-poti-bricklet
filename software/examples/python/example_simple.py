#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Rotary Poti Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_poti import BrickletRotaryPoti

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rp = BrickletRotaryPoti(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current position
    position = rp.get_position()
    print("Position: " + str(position)) # Range: -150 to 150

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
