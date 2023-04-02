import random
Running = True
y = 56;
yvel = 0
isG = False
cx = 128
gOver = False


while Running:
	if gOver:
		scr.clear()
		scr.text('Game Over!',0,0,1)
		scr.text('Press to play!',0,10,1)
		scr.show()
		if Btn(1) or Btn(2) or Btn(3) or Btn(4):
			print('Start!')
			cx = 130
			gOver = False
	else:
		# player jump
		if y > 55:
			yvel = 0
			
		if Btn(1) and isG:
			yvel -= 5
		yvel += 1
		y += yvel
		
		if y > 55:
			y = 56
			isG = True
		else:
			isG = False
		
		# cactus
		
		cx -= 3
		
		if cx < -8:cx = 130
		
		# cactus collision
		
		if cx > 16 and cx < 24 and y > 50:
			gOver = True
		
		scr.clear()
		scr.line(0,63,128,63,1)
		scr.text('R',20,y,1)
		scr.text('I',cx,56,1)
		scr.show()
		
		
		

