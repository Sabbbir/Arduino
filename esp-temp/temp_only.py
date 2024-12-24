import machine
import onewire
import ds18x20
import time

# Pin where the data line is connected (e.g., GPIO4)
ds_pin = machine.Pin(2)

# Initialize the OneWire bus and DS18B20 sensor
ow = onewire.OneWire(ds_pin)
ds = ds18x20.DS18X20(ow)

# Scan for devices on the OneWire bus
roms = ds.scan()
if not roms:
    print("No DS18B20 sensors found!")
else:
    print("Found DS18B20 devices:", roms)

# Continuously read and print temperature
while True:
    if roms:
        ds.convert_temp()
        time.sleep(1)  # Wait for temperature conversion
        for rom in roms:
            temp = ds.read_temp(rom)
            print(f"Temperature: {temp:.2f} deg C")  # Use 'deg C' instead of '°C'

    else:
        print("No devices found!")
    time.sleep(.5)  # Delay between readings
