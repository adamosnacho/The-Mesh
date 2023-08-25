import network
import urequests
import time
import os




def do_connect():
    sta_if = network.WLAN(network.STA_IF) # create station interface
    sta_if.active(True)
    sta_if.connect(ssid,pssw)
    return sta_if


def dwnl_install(name,lc):
	try:os.chdir(lc)
	except:pass
	print('downloading '+name)
	cnt = urequests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/'+name).text
	print('installing '+name)
	with open(name,'w') as f:
		f.write(cnt)
	print('installed '+name)
	print('')
	print('')
	print('')
sta_scan = network.WLAN(network.STA_IF)
sta_scan.active(True)
networks = []
i = 0
for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_scan.scan():
	networks.append(str(i)+' - '+ssid.decode())
	i+=1

print(str(networks))

inp = input('Enter network id (number before name) -> ')
ssid = networks[int(inp)].replace(str(inp)+' - ','')
pssw = input('password -> ')

sta_scan.active(False)
del(sta_scan)

sta_if = do_connect()

print('Waiting for internet...')
time.sleep(5)
if not sta_if.isconnected():
	print('FATAL ERROR: Did not manage to connect to internet!')
else:
	print('Connected')
	try:
		os.mkdir('data')
		os.mkdir('apps')
		os.mkdir('dev')
	except:pass
	dwnl_install('main.py','/')
	dwnl_install('sh1106.py','/')
	dwnl_install('Wifi.py','/apps')
	dwnl_install('store.py','/apps')
	dwnl_install('console.py','/dev')
	dwnl_install('funcs.py','/')
	dwnl_install('wifi','/')
	dwnl_install('v','/')






