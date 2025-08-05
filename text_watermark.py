# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np

# image opening
image = Image.open("wallpaper.jpg")
# this open the photo viewer
# image.show()  

# text Watermark
watermark_image = image.copy()

draw = ImageDraw.Draw(watermark_image)
# ("font type",font size)
w, h = image.size
x, y = int(w / 2), int(h / 2)
if x > y:
  font_size = y
elif y > x:
  font_size = x
else:
  font_size = x
  
font = ImageFont.truetype("arial.ttf", int(font_size/6))

# add Watermark
# (0,0,0)-black color text
draw.text((x, y), "titan", fill=(0, 0, 0), font=font, anchor='ms')
plt.subplot(1, 2, 1)
plt.title("black text")
plt.imshow(watermark_image)

# add Watermark
# (255,255,255)-White color text
draw.text((x, y), "titan", fill=(255, 255, 255), font=font, anchor='ms')
plt.subplot(1, 2, 2)
plt.title("white text")
plt.imshow(watermark_image)

plt.show()