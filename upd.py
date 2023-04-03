import requests


def wof(name):
    with open(name,'w') as f:
        f.write(requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/'+name).text)

if not sta_if.isconnected: machine.reset()
wof('main.py')
wof('store.py')
wof('WifiConfig.py')
wof('console.py')
wof('funcs')
os.remove('upd.py')
machine.reset()
