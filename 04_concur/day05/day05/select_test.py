"""
select 函数示例
"""

from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

f1 = open('log.txt','r')
f2 = open('1.txt','w')

print("监控IO")
rs,ws,xs = select([f1,f2],[],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)