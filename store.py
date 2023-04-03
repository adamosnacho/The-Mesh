import network
Running = True

def Keyboard(title):
	tick = 0
	data = ''
	pn = 0
	charDict = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'), ('f', 'f'), ('g', 'g'), ('h', 'h'), ('i', 'i'), ('j', 'j'), ('k', 'k'), ('l', 'l'), ('m', 'm'),('n','n'), ('o', 'o'), ('p', 'p'), ('q', 'q'), ('r', 'r'), ('s','s'), ('t', 't'), ('u', 'u'), ('w', 'w'), ('y', 'y'), ('z', 'z'), ('x', 'x'), (',', ','), ('[', '['), (']', ']'), ('{', '{'), ('}', '}'), ('(', '('), (')', ')'), ("'", "'"), ('_', '_'), ('-', '-'), (':', ':'), (';', ';'),('.', '.'),("'", "'"),('tab','    '),('del','%del'),('space',' ')]
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

if Connected:
    appName = Keyboard('app')
    appCnt = requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/apps/'+appName+'.py').text
    if appCnt == '404: Not Found':
    	machine.reset()
    else:
    	with open(appName+'.py', 'w') as appfile:
    		appfile.write(appCnt)
    	machine.reset()
