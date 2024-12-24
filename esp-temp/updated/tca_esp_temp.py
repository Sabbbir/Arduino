# main.py

from machine import Pin, SPI
import st7735  # Ensure ST7735.py is uploaded to your ESP32
from font5x8 import font as sysfont  # Import the font dictionary

# Initialize backlight via GPIO13 if used
# If backlight is connected directly to 3.3V, you can skip this section
BACKLIGHT_PIN = 13
backlight = Pin(BACKLIGHT_PIN, Pin.OUT)
backlight.value(1)  # Turn on backlight

# Initialize SPI interface
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))

# Define pin connections
cs = Pin(5, Pin.OUT)       # Chip Select (CS)
dc = Pin(15, Pin.OUT)      # Data/Command (DC or A0)
rst = Pin(4, Pin.OUT)      # Reset (RST)

# Initialize the display
tft = st7735.TFT(spi, dc, rst, cs)
# Initialize display (use initr() for red tab, initb() for blue tab, initg() for green tab)
tft.initb()
tft.rgb(True)        # Set color mode to RGB (set to False if colors are inverted)
# Set rotation (0-3). Adjust as needed for your display orientation
tft.rotation(0)

# Clear the display with a black background
tft.fill(tft.BLACK)

# Function to render text using the simple font


def render_text(tft, position, text, color, font):
    x, y = position
    for char in text:
        ascii_val = ord(char)
        if ascii_val < font['Start'] or ascii_val > font['End']:
            # Skip characters outside the font range
            x += (font['Width'] + 1)
            continue
        # Calculate the index of the character in the font data
        char_index = ascii_val - font['Start']
        # Each character is 5 bytes wide
        start = char_index * font['Width']
        char_data = font['Data'][start:start + font['Width']]

        for col in range(font['Width']):
            byte = char_data[col]
            for row in range(font['Height']):
                if byte & (1 << row):
                    tft.pixel((x + col, y + row), color)
        # Move to the next character position
        x += (font['Width'] + 1)  # 1 pixel space between characters


# Render "Hello World" on the display at position (20, 20) in blue color
render_text(tft, (20, 20), "Hello World!", st7735.BLUE, sysfont)

# Keep the program running
while True:
    pass
