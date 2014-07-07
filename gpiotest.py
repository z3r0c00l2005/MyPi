try:
    import RPi.GPIO as GPIO
    import smbus
    import time
except RuntimeError:
    print("Error importing modules. Check running as root")

Solenoid1Open = 7
Solenoid1Close = 8
Solenoid2Open = 10
Solenoid2Close = 11
Solenoid3Open = 12
Solenoid3Close = 13
Solenoid4Open = 15
Solenoid4Close = 16
Solenoid5Open = 18
Solenoid5Close = 19
Solenoid6Open = 21
Solenoid6Close = 22
Solenoid7Open = 23
Solenoid7Close = 24

    # Use Port A for Open and B for close
Solenoid8 = 00000001
Solenoid9 = 00000010
Solenoid10 = 00000100
Solenoid11 = 00001000
Solenoid12 = 00010000
Solenoid13 = 00100000
Solenoid14 = 01000000
Solenoid15 = 10000000




def InitialiseSMBusExtender():
    bus = smbus.SMBus(1)
    DEVICE = 0x20 # Device Address
    IODIRA = 0x00 # Pin Direction Register Port A
    IODIRB = 0x01 # Pin Direction Register Port B
    OLATA = 0x14 # Register for Outputs Port A
    OLATB = 0x15 # Register for Inputs Port B
    GPIOA = 0x12 # Register for Inputs Port A
    GPIOB = 0x13 # Register for Inputs Port B

    bus.write_byte_data(DEVICE,IODIRA,0x00) # Set port A to all outputs
    bus.write_byte_data(DEVICE,IODIRB,0x00) # Set port B to all outputs
    bus.write_byte_data(DEVICE,OLATA,0) # Set port A outputs to 0000000
    bus.write_byte_data(DEVICE,OLATB,0) # Set port B outputs to 0000000
    return

def InitialiseGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Solenoid1Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid1Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid2Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid2Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid3Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid3Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid4Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid4Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid5Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid5Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid6Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid6Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid7Open, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Solenoid7Close, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    return

def Cleanup():
    GPIO.cleanup()
    return

def blink(pin):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
        return

InitialiseGPIO()
for i in range(0,10):
        blink(Solenoid6Close)
Cleanup()

#A0
