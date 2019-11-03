"""
模拟僵尸进程产生
"""

import os,sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(2)
else:
    """
    os.wait() 处理僵尸进程
    """
    pid,status = os.wait()
    print("pid:",pid)
    print("statis:",status) # child退出状态*256

    while True:  # 父进程不退出
        pass