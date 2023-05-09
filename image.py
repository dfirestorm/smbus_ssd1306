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

# Clear display.
disp.clear()
disp.display()


image = Image.open('happycat_oled_64.ppm').convert('1')

# Alternatively load a different format image, resize it, and convert to 1 bit color.
#image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

# Display image.
disp.image(image)
disp.display()