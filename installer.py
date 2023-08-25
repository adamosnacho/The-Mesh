import network
import urequests
import time
import os

class Response:

    def __init__(self, f):
        self.raw = f
        self.encoding = "utf-8"
        self._cached = None

    def close(self):
        if self.raw:
            self.raw.close()
            self.raw = None
        self._cached = None

    @property
    def content(self):
        if self._cached is None:
            try:
                self._cached = self.raw.read()
            finally:
                self.raw.close()
                self.raw = None
        return self._cached

    @property
    def text(self):
        return str(self.content, self.encoding)

    def json(self):
        import ujson
        return ujson.loads(self.content)


def request(method, url, data=None, json=None, headers={}, stream=None, parse_headers=True):
    redir_cnt = 1
    while True:
        try:
            proto, dummy, host, path = url.split("/", 3)
        except ValueError:
            proto, dummy, host = url.split("/", 2)
            path = ""
        if proto == "http:":
            port = 80
        elif proto == "https:":
            import ussl
            port = 443
        else:
            raise ValueError("Unsupported protocol: " + proto)

        if ":" in host:
            host, port = host.split(":", 1)
            port = int(port)

        ai = usocket.getaddrinfo(host, port, 0, usocket.SOCK_STREAM)
        ai = ai[0]

        resp_d = None
        if parse_headers is not False:
            resp_d = {}

        s = usocket.socket(ai[0], ai[1], ai[2])
        try:
            s.connect(ai[-1])
            if proto == "https:":
                s = ussl.wrap_socket(s, server_hostname=host)
            s.write(b"%s /%s HTTP/1.0\r\n" % (method, path))
            if not "Host" in headers:
                s.write(b"Host: %s\r\n" % host)
            # Iterate over keys to avoid tuple alloc
            for k in headers:
                s.write(k)
                s.write(b": ")
                s.write(headers[k])
                s.write(b"\r\n")
            if json is not None:
                assert data is None
                import ujson
                data = ujson.dumps(json)
                s.write(b"Content-Type: application/json\r\n")
            if data:
                s.write(b"Content-Length: %d\r\n" % len(data))
            s.write(b"Connection: close\r\n\r\n")
            if data:
                s.write(data)

            l = s.readline()
            #print(l)
            l = l.split(None, 2)
            status = int(l[1])
            reason = ""
            if len(l) > 2:
                reason = l[2].rstrip()
            while True:
                l = s.readline()
                if not l or l == b"\r\n":
                    break
                #print(l)



def do_connect():
    sta_if = network.WLAN(network.STA_IF) # create station interface
    sta_if.active(True)
    sta_if.connect(ssid,pssw)
    return sta_if


def dwnl_install(name,lc):
	os.chdir(lc)
	print('downloading '+name)
	cnt = get('https://raw.githubusercontent.com/adamosnacho/The-Mesh/Os/'+name).text
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
	dwnl_install('Wifi.py','apps')
	dwnl_install('store.py','apps')
	dwnl_install('requests.py','/')
	dwnl_install('console.py','dev')
	dwnl_install('funcs.py','/')
	dwnl_install('wifi','/')
	dwnl_install('v','/')






