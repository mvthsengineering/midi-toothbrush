import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button_callback(channel):
	if channel == 10:
		print("Button was pushed!")
		import MidiscreenNew.py
	if channel == 12:
		print("IT WORKS!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(12,GPIO.RISING,callback=button_callback)
message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
