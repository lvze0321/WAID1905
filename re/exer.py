import re 

f = open('test.txt') 

data = f.read()

# pattern = r'\b[A-Z]\S*' 
pattern = r'-?\d+\.?/?\d*%?'

l = re.findall(pattern,data)
print(l)