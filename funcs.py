from machine import Pin, I2C, ADC, reset
import framebuf, os, network, time

def RF(name):
	with open('/'+name, 'r') as f:
		cnt = f.read()
	return cnt

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

def InRange(x,minn,maxn):
	if x > minn and x < maxn:
		return True
	else:
		return False
def PickList(choices,scr):
	Picking = True
	pn = 0
	while Picking:
		scr.clear()
		for i in range(len(choices)):
			if i == pn:
				scr.text('>' + choices[i], 1, ((i * 10) - (pn * 10))+30, 1)
			else:
				scr.text(choices[i], 1, ((i * 10) - (pn * 10))+30, 1)
		scr.show()
		if Btn(1):
			pn -= 1
			time.sleep(0.2)
		if Btn(2):
			pn += 1
			time.sleep(0.2)
		pn = Clamp(pn, 0, len(choices) - 1)
		if Btn(4):
			Picking = False
			return choices[pn]

def Keyboard(title,scr):
	chars = "!#$%&'()*+,-./123456789;<=>?@BCDEFGHIJKLMNOPQRSTUVWXYZ\]^_`bcdefghijklmnopqrstuvwxyz|}~ 	"
	scr.clear()
	Typing = True
	pn = 0
	t = ''
	while Typing:
		scr.clear()
		scr.text(t,120+ (-1*len(t)),32,1)
		scr.fill_rect(0,0,128,12,1)
		if pn != len(chars):
			scr.text(str(title)+' <'+chars[pn]+'>',0,1,0)
		else:
			scr.text(str(title)+' <del>',0,1,0)

		if Btn(1):pn+= 1; time.sleep(0.007)
		if Btn(2):pn-= 1; time.sleep(0.007)
		pn = Clamp(pn,0,len(t))

		
