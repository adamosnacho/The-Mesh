Running = True
os.chdir('/')

if Connected:
	scr.text('Loading apps...',0,0,1)
	scr.show()
	appList = eval(requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/apps/AppList.ls').text)
	if Btn(3):
		while Btn(3):continue
		appName = Keyboard('app name',scr)
	else:
		appName = PickList(appList,scr)
	appCnt = requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/apps/'+str(appName)+'.py').text
	if appCnt == '404: Not Found':
		scr.clear()
		scr.text('No Such App!',0,0,1)
		scr.show()
		time.sleep(2)
	else:
		scr.clear()
		scr.text('Installing...',0,0,1)
		scr.show()
		with open(appName+'.py', 'w') as appfile:
			appfile.write(appCnt)
		time.sleep(2)
else:
	scr.clear()
	scr.text('No Internet!',0,0,1)
	scr.show()
	time.sleep(2)

