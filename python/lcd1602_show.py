#!/usr/bin/env python3
import LCD1602
import time

def setup():
    LCD1602.init(0x27, 1)	# init(slave address, background light)
    LCD1602.write(0, 0, 'Greetings!!!!')
    LCD1602.write(0, 1, 'From SunFounder')
    # time.sleep(0)

def destroy():
    LCD1602.clear()

if __name__ == "__main__":
try:
    setup()
except KeyboardInterrupt:
    destroy()
