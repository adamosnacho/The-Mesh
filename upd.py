import requests


def wof(name):
    scr.clear()
    scr.text('Installing:',0,0,1)
    scr.text(name,0,10,1)
    scr.show()
    with open(name,'w') as f:
        f.write(requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/'+name).text)

if not sta_if.isconnected: machine.reset()
wof('main.py')
wof('store.py')
wof('WifiConfig.py')
wof('console.py')
wof('funcs.py')
os.remove('upd.py')
machine.reset()
