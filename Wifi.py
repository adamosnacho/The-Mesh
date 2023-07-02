Running = True
sta_if.active(True)

sta_if.disconnect()
sta_if.active(True)

networks = []
scr.text('SCANNING NET',0,0,1)
scr.show()
for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
	networks.append(ssid.decode())
print(networks)
ssid = PickList(networks,scr)
pssw = Keyboard('password:',scr)
os.chdir('/')
with open('wifi','w') as f:
	f.write(str([ssid,pssw]))
sta_if = do_connect()
