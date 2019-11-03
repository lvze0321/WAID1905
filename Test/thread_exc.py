from threading import Thread,Lock
import os
from time import sleep

lock = Lock()

urls = [
    "/home/tarena/桌面/",
    "/home/tarena/下载/",
]

filename = input('文件：')
exp = []
for i in urls:
    if os.path.exists(i+filename):
        exp.append(i+filename)

if not exp:
    os._exit()

num = len(exp)
file_size = os.path.getsize(exp[0])
block_size = file_size // num + 1


fd = open(filename,'wb')
def load(path,n):
    f = open(path,'rb')
    seek_bytes = block_size * n
    f.seek(seek_bytes)
    data = f.read(block_size)

    with lock:
        fd.seek(seek_bytes)
        sleep(1)
        fd.write(data)

n = 0
for path in exp:
    t = Thread(target=load,args=(path,n))
    t.start()
    n += 1






