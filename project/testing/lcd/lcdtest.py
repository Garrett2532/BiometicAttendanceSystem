from RPLCD import CharLCD
from RPi import GPIO
import time 
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.clear()
lcd.write_string(u'Hello World!')
time.sleep(3)
lcd.clear()
lcd.write_string(u'testing...')
x = 'It Worked!'
time.sleep(3)
lcd.clear()
lcd.write_string(x)
time.sleep(3)
lcd.clear()
GPIO.cleanup()
