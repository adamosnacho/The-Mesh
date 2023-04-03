import requests


def wof(name):
    scr.clear()
    scr.text('Installing:',0,0,1)
    scr.text(name,0,10,1)
    scr.show()
    with open(name,'w') as f:
        f.write(requests.get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/'+name).text)
if Connected:
    wof('main.py')
    wof('store.py')
    wof('WifiConfig.py')
    wof('console.py')
    wof('funcs.py')
    scr.clear()
    scr.text('DONE!',0,0,1)
    scr.show()
    os.remove('upd.py')
    machine.reset()
    time.sleep(15)
