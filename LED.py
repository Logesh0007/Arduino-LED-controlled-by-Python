import pyfirmata
import time

pin = 13                     # pin number for LED
port = "COM3"        # Port number
board = pyfirmata.Arduino(port)

# One time
'''
print("ON")                 
board.digital[pin].write(1)                    # Turn on

time.sleep(5)                       # It'll turned off after 5 secs

print("OFF")
board.digital[pin].write(0)                     # Turn off

'''
# Infinite loop
while 1:                  
    print("ON")
    board.digital[pin].write(1)               # Turn ON
    time.sleep(1)

    print("OFF")
    board.digital[pin].write(0)               # Turn OFF
    time.sleep(1)

