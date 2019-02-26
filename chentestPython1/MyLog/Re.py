import re

#match（）函数只检测RE是不是在string的开始位置匹配，如果匹配成功，则返回一个Match
#search()会扫描整个string查找匹配；只到找到第一个匹配然后返回
#也就是说match（）只有在0位置匹配成功的话才有返回，
#如果不是开始位置匹配成功的话，match()就返回none。
#findall , finditer 用于查找所有匹配

pattern = re.compile(r'hello')
match = pattern.match('hello world! ')
if match:
     print (match.group())
     
     
pattern = re.compile(r'world')
match = pattern.search('hello world!')
if match:
     print (match.group())
     
 
     
#\w Unicode (str) patterns
#+  1 time or max time 
#(...)  Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
pattern = re.compile(r"(\w+) (\w+)")
match = pattern.findall('Isaac Newton Aot iuy physicist huy7')
print (match)

pattern = re.compile(r"(\w+) (\w+)")
match = pattern.finditer('Isaac Newton Aot iuy physicist huy7')
for m in match:
    print (m.group(0))
 
     
#\d number
#+ 1 time or any time     

pattern = re.compile(r's\d\d+')
match = pattern.match('s227a5tt45')
print (match.group())


pattern = re.compile(r'\d\d+')
match = pattern.finditer('227a5tt  533df')
for m in match:
    print (m.group(0))
    
    
 
#. one char 
#*  0 time or any time
#?  0 time or 1 time
pattern = re.compile(r's\d.\d?')
match = pattern.match('s4t8')
print (match.group())

pattern = re.compile(r's\d.\d*\w?\w')
match = pattern.finditer('fs4t8  s332ddd')
for m in match:
    print (m.group(0))

      