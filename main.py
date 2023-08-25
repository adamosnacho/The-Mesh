from machine import Pin, I2C
import time, os, machine, network, _thread
from sh1106 import SH1106_I2C
from funcs import *
import urequests as requests
#oled init
i2c = machine.I2C(sda=Pin(6), scl=Pin(7))
scr = SH1106_I2C(128, 64, i2c)
scr.contrast(200)
#lists and sets all apps
def upda():
	apps = os.listdir('/apps')
	
	if len(apps) == 0:
		apps.append('none.py')
	return apps

#wifi init
sta_if = do_connect()

Connected = False
#get local version
with open('v','r') as f:
	v = f.read()
v = eval(v)



#loading screen
scr.clear()
scr.text('The Mesh|v-'+str(v).replace('',''),0,0,1)
scr.text('by Adam Ryan',0,54,1)
scr.show()
time.sleep(1)


NetBtm = Bitmap(5,5,'11111 00000 01110 00000 00100',1)

#main menu
apps = upda()
apps.append('dev.py')
On = True
pn = 0
vchecked = False

while On:
	scr.clear()
	Connected = sta_if.isconnected()
	if Connected:
		scr.blit(NetBtm,123,0)
	if Connected and not vchecked:
		vchecked = True
		vext = requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/v').text
		vext = eval(vext)
		print(vext)
		print(v)
		if vext != v:
			print('Update required!')
			scr.clear()
			scr.text('Update required!',0,0,1)
			scr.show()
			time.sleep(3)
			exec(requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/apps/upd.py').text)
		
	for i in range(len(apps)):
		if i == pn:
			scr.text('>' + apps[i].replace('.py', ''), 1, ((i * 10) - (pn * 10))+30, 1)
		else:
			scr.text(apps[i].replace('.py', ''), 1, ((i * 10) - (pn * 10))+30, 1)
	if Btn(1):
		pn -= 1
		time.sleep(0.1)
	if Btn(2):
		pn += 1
		time.sleep(0.1)
	pn = Clamp(pn, 0, len(apps) - 1)
	if Btn(4) and apps[pn] != 'none.py':
		scr.clear()
		scr.show()
		time.sleep(0.005)
		os.chdir('/data')
		try:
			if apps[pn] != 'dev.py':
				exec(RF('apps/'+apps[pn]))
			else:
				while Btn(4):continue
				exec(RF('dev/'+PickList(os.listdir('/dev'),scr)))
		except Exception as e:
			print(e)
			for i in range(len(str(e))*10):
				scr.clear()
				scr.text(str(e),(i*-1)+20,0,1)
				scr.show()
				time.sleep(0.009)
			
		os.chdir('/')
		scr.clear()
		scr.show()
		time.sleep(0.01)
		apps = upda()
		apps.append('dev.py')
	scr.show()
	time.sleep(0.001)
