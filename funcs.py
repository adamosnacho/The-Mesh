from machine import Pin, I2C, ADC
import framebuf, os, network

def RF(name):return open('/'+name, 'r').read()

def exists(path):
	try:
		with open(path,'r') as f:
			f.close()
		return True
	except:
		return False
def Btn(key):
	if key == 1:
		return not Pin(9,Pin.IN, Pin.PULL_UP).value()
	if key == 2:
		return not Pin(2,Pin.IN, Pin.PULL_UP).value()
	if key == 3:
		return not Pin(4,Pin.IN, Pin.PULL_UP).value()
	if key == 4:
		return not Pin(3,Pin.IN, Pin.PULL_UP).value()

def Clamp(x,Min,Max):
	if x > Max: return Max
	if x < Min: return Min
	return x

def Map(x, IS, IE, OS, OE):
	return OS + (OE - OS) * ((x - IS) / (IE - IS))
def Bitmap(xs,ys,pix,scale,e=False):
	lpix = []
	pix = pix.replace(' ','')
	
	#lexer
	for index in range(0, len(pix), xs):
		lpix.append(pix[index : index + xs])
	
	#scale x
	for i in range(len(lpix)):
		newlp = ''
		lp = lpix[i]
		for char in range(len(lp)):
			for res in range(scale):
				newlp += lp[char]
		lpix[i] = newlp
	
	#scale y
	newlp = []
	for i in range(len(lpix)):
		for res in range(scale):
			newlp.append(lpix[i])
	lpix = newlp
	pix = ''.join(lpix)
	
	fb = framebuf.FrameBuffer(bytearray((xs*scale) * (ys*scale)), (xs*scale), (ys*scale), framebuf.MONO_VLSB)
	fb.fill(0)
	cp = 0
	for y in range(ys*scale):
		for x in range(xs*scale):
			fb.pixel(x,y,int(pix[cp]))
			cp += 1
	return(fb)

def do_connect():
	with open('wifi','r') as f:
		WIFISET = eval(f.read())
	sta_if = network.WLAN(network.STA_IF) # create station interface
	sta_if.active(True)
	sta_if.connect(WIFISET[0],WIFISET[1])
	return sta_if
