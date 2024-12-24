# main.py

from machine import Pin, SPI
import st7735 as st7735  # Ensure this file is uploaded to your ESP32
from font5x8 import font as sysfont  # Import the font dictionary

# Initialize SPI interface
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))

# Define pin connections
cs = Pin(5, Pin.OUT)       # Chip Select (CS)
dc = Pin(15, Pin.OUT)      # Data/Command (DC or A0)
rst = Pin(4, Pin.OUT)      # Reset (RST)

# Initialize the display
tft = st7735.TFT(spi, dc, rst, cs)
tft.initr()          # Initialize display (use initr() for red tab, initb() for blue tab, initg() for green tab)
tft.rgb(True)        # Set color mode to RGB (set to False if colors are inverted)
tft.rotation(0)      # Set rotation (0-3). Adjust as needed for your display orientation

# Turn on the backlight (if connected via GPIO13)
# led = Pin(13, Pin.OUT)
# led.value(1)  # Turn on backlight

# Clear the display with a black background
tft.fill(tft.BLACK)

# Display "Hello World" at position (10, 10)
tft.text((20, 20), "Hello World!", tft.BLUE, sysfont)

# Keep the program running
while True:
    pass
