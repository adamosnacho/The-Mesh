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
		self.fb = Bitmap(8,5,'00000100 00011100 00111110 01111110 11111111',1,e=True)
		self.wx = startPos
	def upd(self):
		if self.wx < 0:self.wx = 130
		scr.blit(self.fb,int(self.wx),53)
	def move(self,x):
		self.wx -=x

f = Bitmap(14,19,'00000011100000 00000111100000 00001111100000 00001111100000 00011111100000 00011111100000 00011111100000 00111111100000 00111111100000 00011111100000 00001111100000 00000011100000 11100000100111 001111111111100 00010000000000 00010000000000 00010000000000 00010000000000 11111100000000',2)
gover = False
score = 0
m = 0
fy = 30
rot = 0
wv = 0

#waves
w = []
for i in range(26):
	w.append(wave(i*5))

while Running:
	if not gover:
		#controls
		score += 1
		if Btn(3):rot += 0.5
		if Btn(4):rot -= 0.5
		
		#calculations
		if fy > 16:
			fy -= rot
		else:
			rot = 1
		
		rot = Clamp(rot, -2, 2)
		
		if InRange(fy,16,28):
			m += 1
			wm = 9
			rot += 0.030
		else:
			m += 0.1
			wm = 3
		
		if fy > 27:
			fy = 27
		
		fy += 0.6
		
		
		#conditions
		if m >= 500:gover = True
		
		scr.clear()
		scr.blit(f,20,int(fy))
		for _w in w:
			_w.move(wm)
			_w.upd()
		scr.fill_rect(0,56,128,10,1)
		scr.text(str(round(m,1))+'m',0,0,1)
		scr.show()
		#27 17
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
		scr.text(str(high) + 'p',0,40,1)
		scr.text('Press up to exit!',0,50,1)
		scr.show()
		while not Btn(1):continue
		Running = False
