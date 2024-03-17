#!/usr/bin/env python3
import LCD1602
import time
import psutil

def setup():
    LCD1602.init(0x27, 1)	# init(slave address, background light)
    # time.sleep(1)

def destroy():
    LCD1602.clear()

if __name__ == "__main__":
    try:
        setup()
        while True:
            cpu_load = psutil.cpu_percent()
            mem_load = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
            LCD1602.write(0, 0, "CPU%: {:0.2f}".format(cpu_load))
            LCD1602.write(0, 1, "MEM%: {:0.2f}".format(mem_load))
            time.sleep(1)
        
    except KeyboardInterrupt:
        destroy()
