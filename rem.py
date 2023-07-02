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
