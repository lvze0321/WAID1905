import re 

pattern = r'\d+'
s = "2008年事情多，08奥运，512地震"

it = re.finditer(pattern,s) 

# print(dir(next(it)))

for i in it:
    #ｍａｔｃｈ对象group函数获取匹配内容
    print(i.group())

try:
    obj = re.fullmatch(r'\w+','hello1973')
    print(obj.group())
except AttributeError as e:
    print(e)

obj = re.match(r'[A-Z]\w+',"Hello World")
print(obj.group())

obj = re.search(r'\d+',s)
print(obj.group())