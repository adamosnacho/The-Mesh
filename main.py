from machine import Pin, I2C
import time, os, machine
from ssd1306 import SSD1306_I2C
from funcs import *
i2c = machine.I2C(sda=Pin(4), scl=Pin(5))
scr = SSD1306_I2C(128, 64, i2c)
On = True
pn = 0
apps = os.listdir()
if not Btn(1):
	apps.remove('main.py')
	apps.remove('funcs.py')
	apps.remove('ssd1306.py')
	apps.remove('boot.py')
	apps.remove('console.py')
	apps.remove('wifi')
	apps.remove('requests.py')


while On:
# 	tmr.alarm(6, 1000, 1, function() tmr.wdclr() end)
	scr.clear()
	for i in range(len(apps)):
		
		if i == pn:
			scr.text(apps[i].replace('.py', '') + ' <', 1, i * 10, 1)
		else:
			scr.text(apps[i].replace('.py', ''), 1, i * 10, 1)
	scr.show()
	if Btn(1):
		pn -= 1
		time.sleep(0.2)
	if Btn(2):
		pn += 1
		time.sleep(0.2)
	pn = Clamp(pn, 0, len(apps) - 1)
	if Btn(4):
		scr.clear()
		scr.text('Loading '+ apps[pn].replace('.py', '') + '...',1,1,1)
		scr.show()
		time.sleep(0.8)
		exec(RF(apps[pn]))
	time.sleep(0.05)



