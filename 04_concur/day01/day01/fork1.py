"""
fork.py fork进程创建演示2
"""

import os
from time import sleep

print("===========================")
a = 1

# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("The new process")
    print("a = ",a) # 从父进程继承空间a
    a = 10000 # 修改自己的a
else:
    sleep(1)
    print("The old process")
    print("a:",a)

print("All a->",a) # 父子进程都执行