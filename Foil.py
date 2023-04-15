import framebuf

#create save file
if not exists('Foil.high'):
	with open('Foil.high','w') as f:
		f.write('10000')
	print('created file!')
else:print('file exists!')

Running = True

class wave:
	def __init__(self,startPos):
		self.fb = Bitmap(5,3,'00100 01100 11111',1,e=True)
		self.wx = startPos
	def upd(self):
		if self.wx < 0:self.wx = 130
		scr.blit(self.fb,int(self.wx),53)
	def move(self,x):
		self.wx -=x

f = Bitmap(10,12,'0000010000 0001110000 0011110000 0011110000 0111110000 0111110000 0011110000 1000010011 0111111100 0100000000 0100000000 1111000000',2)
fly = False
gover = False
fvy = 0
fxv = 10
fy = 28
m = 0
score = 0

#waves
w = []
for i in range(26):
	w.append(wave(i*5))

while Running:
	if not gover:
		#controls
		score += 1
		if Btn(3):fvy -= fxv / 10
		if Btn(4):fxv += 0.5
		else:fxv-=0.5
		fxv = Clamp(fxv,0.3,4)
		#phisics
		fvy += 0.2
		
		#pos manipul
		fy += fvy
		fy = int(fy)
		
		#conds
		if fy > 39:
			fy = 39
			fvy = 0
		
		if fy < 33:
			fly = False
			fvy += 1
			fxv -= 0.4
			
		if fy >33 and fy < 38:
			m += 1
			wm = 4 + fxv
			fly = True
		else:
			m+=0.1
			wm = 1 + fxv
			fly = False
		
		for _w in w:
			_w.move(wm)
		
		if m >= 100:gover = True
		
		scr.clear()
		scr.blit(f,20,fy)
		for _w in w:
			_w.upd()
		scr.fill_rect(0,56,128,10,1)
		scr.text(str(round(m,1))+'m',0,0,1)
		scr.show()

	else:
		score = int(score / 10)
		with open('Foil.high','r') as f:
			high = int(round(float(f.read())))
		if high > score:
			high = score
			with open('Foil.high','w') as f:
				f.write(str(int(score)))
		
		scr.clear()
		scr.text('Done.',0,0,1)
		scr.text('Score:',0,10,1)
		scr.text(str(score) + 'p',0,20,1)
		scr.text('High Score:',0,30,1)
		scr.text(str(high),0,40,1)
		scr.text('Press up to exit!',0,50,1)
		scr.show()
		while not Btn(1):continue
		Running = False

