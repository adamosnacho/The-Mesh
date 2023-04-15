import requests
def wof(name):
	scr.clear()
	scr.text('Installing:',0,0,1)
	scr.text(name,0,10,1)
	scr.show()
	cnt = requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/'+name).text
	with open(name,'w') as:
		if cnt != '' or cnt != '404: Not Found':
			f.write()
if sta_if.isconnected():
	scr.clear()
	scr.text('Connection',0,0,1)
	scr.text('estabilished.',0,10,1)
	scr.show()
	time.sleep(2)
	wof('main.py')
	wof('store.py')
	wof('WifiConfig.py')
	wof('console.py')
	wof('funcs.py')
	scr.clear()
	scr.text('Done!',0,0,1)
	scr.show()
	os.remove('upd.py')
	time.sleep(4)
else:
	scr.clear()
	scr.text('No Internet!',0,0,1)
	scr.show()
	time.sleep(4)
