from machine import Pin, I2C, ADC
import ssd1306

def RF(name):return open(name, 'r').read()

def Btn(key):
	if key == 1:
		return not Pin(13,Pin.IN, Pin.PULL_UP).value()
	if key == 2:
		return not Pin(12,Pin.IN, Pin.PULL_UP).value()
	if key == 3:
		return not Pin(14,Pin.IN, Pin.PULL_UP).value()
	if key == 4:
		return not Pin(2,Pin.IN, Pin.PULL_UP).value()


def Clamp(x,Min,Max):
	if x > Max: return Max
	if x < Min: return Min
	return x

def Map(x, IS, IE, OS, OE):
	return OS + (OE - OS) * ((x - IS) / (IE - IS))
