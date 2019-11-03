"""
process_server.py 基于process的多进程并发
"""

from socket import *
from multiprocessing import Process
import os
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 具体处理客户端请求
def handle():
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888...")

while True:
    # 循环处理客户端链接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端事物
    p = Process(target = handle)
    p.daemon = True # 父进程结束则所有服务终止
    p.start()
