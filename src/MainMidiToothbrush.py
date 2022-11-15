import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import mido
from mido import MidiFile
  # Define the Reset Pin
reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
oled_reset = digitalio.DigitalInOut(board.D4) #set pin

song_name = "Long_Long_Time" #name of file without extension

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
text = (' ')
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

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def button_callback(channel):
	if channel == 10:
		print("Button was pushed!")
		text = song_name
		#load a midi file
		#mid = MidiFile('mary4.mid')
		#mid = MidiFile('star1.mid')

		mid = MidiFile(song_name+".mid")

		#print available ports #print(mido.get_output_names())
		#print the contents of the midi file.
		#for i, trackD in enumerate(mid.tracks):
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
	if channel == 12:
                print("IT WORKS!")
#GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BCM) # Use physical pin numbering
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled >GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(12,GPIO.RISING,callback=button_callback)
message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up


#load a midi file
#mid = MidiFile('mary4.mid')
#mid = MidiFile('star1.mid')
#mid = MidiFile(song_name+".mid")
#print available ports #print(mido.get_output_names())
#print the contents of the midi file.
#for i, track in enumerate(mid.tracks):
#  print('Track {}: {}'.format(i, track.name))
#   for msg in track:
#     print(msg)
#open a port either external with ttymidi or internal with timidity
#outport = mido.open_output('/dev/Toothbrush Port 1', 57600, timeout=0.5)
#outport = mido.open_output('ttymidi:MIDI in 128:1')
#play the file on the assigned port
#for msg in MidiFile('mary.mid').play():
#for msg in mid.play():
#   outport.send(msg)
#close the port
#outport.close()

