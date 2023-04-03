import network,requests
with open('wifi','r') as f:
	WIFISET = eval(f.read())
print('setup')
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFISET[0], WIFISET[1])

def wof(name):
    with open(name,'w') as f:
        f.write(requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/apps/'+name).text)

while not sta_if.isconnected:time.sleep(1)

wof('main.py')
wof('store.py')
wof('WifiConfig.py')
wof('console.py')
wof('funcs')
os.remove('upd.py')
machine.reset()
