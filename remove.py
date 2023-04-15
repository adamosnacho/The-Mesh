def Keyboard(title):
	tick = 0
	data = ''
	pn = 0
	charDict = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'),('N','N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S','S'), ('T', 'T'), ('U', 'U'), ('W', 'W'), ('Y', 'Y'), ('Z', 'Z'), ('X', 'X'),('V','V'),('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'), ('f', 'f'), ('g', 'g'), ('h', 'h'), ('i', 'i'), ('j', 'j'), ('k', 'k'), ('l', 'l'), ('m', 'm'),('n','n'), ('o', 'o'), ('p', 'p'), ('q', 'q'), ('r', 'r'), ('s','s'), ('t', 't'), ('u', 'u'), ('w', 'w'), ('y', 'y'), ('z', 'z'), ('x', 'x'),('v','v'), (',', ','), ('[', '['), (']', ']'), ('{', '{'), ('}', '}'), ('(', '('), (')', ')'), ("'", "'"), ('_', '_'), ('-', '-'), (':', ':'), (';', ';'),('.', '.'),("'", "'"),('!','!'),('tab','    '),('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('del','%del'),('space',' ')]


	Tp = True
	while Tp:
		tick += 1
		# calculate pointer and allow for buton selection
		if Btn(1):
			pn -= 1
			time.sleep(0.08)
		if Btn(2):
			pn += 1
			time.sleep(0.08)
		pn = Clamp(pn,0,len(charDict) - 1)
		if Btn(3):
			Tp = False
		if Btn(4):
			if charDict[pn][1] == '%del':
				data = data[:-1]
			else:
				data += charDict[pn][1]
			time.sleep(0.2)
		# screen stuff
		scr.clear()
		if round(tick / 7) % 2 == 0:
			scr.text(data + '<',(-(len(data) * 8)) + 120,20,1)
		else:
			scr.text(data,(-(len(data) * 8)) + 120,20,1)

		#pick letter bar and title
		scr.fill_rect(0,0,128,10,1)
		scr.text(title + ' <' + charDict[pn][0] + '>',0,0,0)
		
		#show the screen
		scr.show()

	return data
os.chdir('/')
files = os.listdir()
Picking = True
pn = 0
while Picking:
	if Btn(1):
		pn -= 1
		time.sleep(0.1)
	if Btn(2):
		pn += 1
		time.sleep(0.1)
	pn = Clamp(pn,0,len(files)-2)
	
	scr.clear()
	for i in range(len(files)-1):
		if i == pn:scr.text('>'+files[i],0,((i * 10) - (pn * 10))+30,1)
		else:scr.text(files[i],0,((i * 10) - (pn * 10))+30,1)
	scr.show()
	
	if Btn(4):
		file = files[pn]
		while Btn(4):continue
		Picking = False
os.remove(file)
