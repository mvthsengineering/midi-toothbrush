# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This demo will fill the screen with white, draw a black box on top
and then print Hello World! in the center of the display

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import mido
from mido import MidiFile
  # Define the Reset Pin
reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
oled_reset = digitalio.DigitalInOut(board.D4)

song_name = "Surprise" #name of file without extension

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, reset=reset_pin, addr=0x3d)

# Use for SPI
# spi = board.SPI()
# oled_cs = digitalio.DigitalInOut(board.D5)
# oled_dc = digitalio.DigitalInOut(board.D6)
# oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = song_name
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()
#load a midi file 
#mid = MidiFile('mary4.mid') 
#mid = MidiFile('star1.mid')
mid = MidiFile(song_name+".mid")  
#print available ports #print(mido.get_output_names())  
#print the contents of the midi file. 
#for i, track in enumerate(mid.tracks): 
#  print('Track {}: {}'.format(i, track.name)) 
#   for msg in track: 
#     print(msg)  
#open a port either external with ttymidi or internal with timidity 
#outport = mido.open_output('/dev/Toothbrush Port 1', 57600, timeout=0.5) 
outport = mido.open_output('ttymidi:MIDI in 128:1')
#play the file on the assigned port 
#for msg in MidiFile('mary.mid').play(): 
for msg in mid.play():  
    outport.send(msg)  
#close the port 
outport.close()

