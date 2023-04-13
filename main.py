from machine import Pin, I2C
import time, os, machine, requests, network
from ssd1306 import SSD1306_I2C
from funcs import *

i2c = machine.I2C(sda=Pin(4), scl=Pin(5))
scr = SSD1306_I2C(128, 64, i2c)

On = True
pn = 0
apps = os.listdir()

Connected = False


with open('wifi','r') as f:
	WIFISET = eval(f.read())
print('setup')
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
try:
	sta_if.connect(WIFISET[0], WIFISET[1])
except:pass

if not Btn(1):
	apps.remove('main.py')
	apps.remove('funcs.py')
	apps.remove('ssd1306.py')
	apps.remove('boot.py')
	apps.remove('console.py')
	apps.remove('wifi')
	apps.remove('requests.py')

scr.clear()
scr.text('The Mesh | v-1',0,0,1)
scr.text('by Adam Ryan',0,54,1)
scr.show()
time.sleep(0.7)

while On:
	if sta_if.isconnected:
		Connected = True
	else:
		Connected = False
	scr.clear()
	for i in range(len(apps)):
		
		if i == pn:
			scr.text('>' + apps[i].replace('.py', ''), 1, ((i * 10) - (pn * 10))+30, 1)
		else:
			scr.text(apps[i].replace('.py', ''), 1, ((i * 10) - (pn * 10))+30, 1)
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
		scr.text('Loading...',1,1,1)
		scr.show()
		time.sleep(0.2)
		exec(RF(apps[pn]))
	time.sleep(0.05)



