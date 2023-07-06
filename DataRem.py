while Btn(4):continue
os.chdir('/data')
files = os.listdir()
file = PickList(files,scr)
os.remove(file)
time.sleep(1)
