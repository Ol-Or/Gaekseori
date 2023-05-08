import smbus
import time

address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)

try:
    while True:
        bus.write_byte(address,AIN2)
        value = bus.read_byte(address)
        print("Water value: %d" % value)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
