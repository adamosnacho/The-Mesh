import framebuf, random

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
		self.wx = startPos + random.randint(-2,2)
	def upd(self):
		if self.wx < 0:self.wx = 130 + random.randint(-2,2)
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
windSpeed = 10

#waves
w = []
for i in range(26):
	w.append(wave(i*5))

while Running:
	if not gover:
		#windchange
		if random.randint(0,200) == 1:
			windSpeed = random.randint(6,14)
			
		
		score += 1
		if Btn(4) or Btn(3) or Btn(2) or Btn(1):
			rot_temp = (4 * (windSpeed / 6)) / 12
			rot -= rot_temp
		#calculations
		rot = Clamp(rot, -5, 3)
		if InRange(fy,16,26):
			wm = 7
			rot += 0.1
			m += 1
		else:
			if fy < 26:
				rot += 1.4
			wm = 3
			m += 0.03
		if fy > 27:
			fy = 27
		fy += rot
		
		#16 min 27 water
		#conditions
		if m >= 500:gover = True
		
		scr.clear()
		scr.blit(f,20,int(fy))
		for _w in w:
			_w.move(wm)
			_w.upd()
		scr.fill_rect(0,56,128,10,1)
		scr.text(str(round(m,1))+'m | '+str(windSpeed)+'kts',0,0,1)
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
		scr.text(str(high) + 'p',0,40,1)
		scr.text('up - exit | down - again',0,50,1)
		scr.show()
		while not Btn(1):continue
		Running = False

