import math
import time

from smbus_ssd1306 import SSD1306_128_64

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# 128x64 display with hardware I2C:
disp = SSD1306_128_64()

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Animate text moving in sine wave.
print('Press Ctrl-C to quit.')
while True:
    disp._buffer = list(range(0,256))
    disp.display()
    # Pause briefly before drawing next frame.
    time.sleep(0.1)