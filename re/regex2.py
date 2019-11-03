import re 

pattern = r"(ab)cd(?P<dog>ef)"

regex = re.compile(pattern)

#获取ｍａｔｃｈ对象
obj = regex.search('abcdefgh',pos=0,endpos=6)

#ｏｂｊ属性变量
print(obj.pos)  #目标子串的开始位置
print(obj.endpos)  #目标子串的结束位置
print(obj.re)   #正则表达式
print(obj.string)  #目标字符串
print(obj.lastgroup) #最后一组名称
print(obj.lastindex) #最后一组序号
print("====================================")

print(obj.span())  #匹配内容的起止位置
print(obj.start()) #匹配内容的开始位置
print(obj.end())   #匹配内容的结束位置

print(obj.group()) #获取正则匹配到的内容
print(obj.group(1)) #获取第一子组对应内容
print(obj.group('dog')) #获取ｄｏｇ组对应内容

print(obj.groupdict()) #捕获组字典
print(obj.groups()) #所有子组对应内容 