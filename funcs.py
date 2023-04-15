from machine import Pin, I2C, ADC
import ssd1306,framebuf

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
def Bitmap(xs,ys,pix,scale):
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
	print(lpix)
	fb = framebuf.FrameBuffer(bytearray((xs*scale) * (ys*scale)), (xs*scale), (ys*scale), framebuf.MONO_VLSB)
	fb.fill(0)
	cp = 0
	for y in range(ys*scale):
		for x in range(xs*scale):
			fb.pixel(x,y,int(pix[cp]))
			cp += 1
	return(fb)



