import re 

# s = "Hello World"
# pattern = r"hello"
# regex = re.compile(pattern,flags=re.I)

# s = '''hello world
# hello kitty
# 你好，北京
# '''
# pattern = r".+"
# regex = re.compile(pattern,re.S)

# s = '''hello world
# nihao beijing
# '''
# pattern = r"^nihao"
# regex = re.compile(pattern,re.M)

s = '''Hello world
nihao beijing
'''
pattern = r"^nihao"
regex = re.compile(pattern,re.A|re.I)

try:
    s = regex.search(s).group()
except Exception :
    print("没有匹配到内容")
else:
    print(s)
