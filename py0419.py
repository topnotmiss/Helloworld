#coding=utf-8

#############Unicode和ASCII码
a = "中国"
b = u"中国"
print type(b)
print type(a)
print a.decode("utf-8")
#这个可以么/   a.encode('ascii')
print len(a), len(b)


############字符串
s = "spam"
a = "中国"
len(s)
print s[-1]
print a[-1]#这里会出现乱码，因为a的第一个字节可能编不出来
print s[1:]
print s[:-1]
s + "xyz"
print s * 8
#字符串的不可变性
# s[0] = "z" #这样不行
s = 'z' + s[1:]
print s

##############类型的特定方法
print  s.find('pa')
print s.replace('pa','xyz')
print s

line = "aaa,bbb,ccc,defg"
print line.split(',')
print line.upper()
print s.isalpha()
print line
print line.lstrip('gfsd')
print line.rstrip("sadfas")

################dir函数调用类的属性，help返回帮助
print dir(line)
print help(str.index)

f = """aaaaaa
b bbbbccccc
dddd"""

import re
match = re.match('Hello[\t]*(.*)world',"Hello  python world")
print match.group(1)

re.match('/(.*)/(.*)/(.*)',"/user/home/python")
#<_sre.SRE_Match object at 0x0000000004685328>
b = re.match('/(.*)/(.*)/(.*)',"/user/home/python")
type(b)
#<type '_sre.SRE_Match'>
b.group()
#'/user/home/python'
b.groups()
#('user', 'home', 'python')


#############list操作
l = ["123",'abc',12.3]
print len(l)
l[:-1]
l + [4,5,6]

l.append('ni')#在末尾加一个
l.pop(2)#删掉Index为2的一项
l.remove('abc')#删掉第一个
l.insert(2,"xyz")#加到index前面

m = ["aa","bb","cc"]
m.sort()#排序
m.reverse()#反转
# m[4]  #会错误，且不能给m[4]赋值

##############list嵌套，即矩阵
m = [[1,2,3],[4,5,6],[7,8,9]]
col2 =  [row[1] for row in m]
print col2

[row[1]+1 for row in m ]
[row[1] for row in m if row[1]%2 == 0]
diag = [m[i][i] for i in [0,1,2]]
doubles = [c*2 for c in "spam"]

################# dictionary:包含键和值
D = {"food":"spam","quality":4,"color":"pink"}
D['food']
D['quality'] += 1

D['id'] = "123456"

#dictionary的排序
D = {"a":1,'b':2,'c':3}
print D

#way 1
ks = D.keys()
ks.sort()
for key in ks:
    print key,"=>",D[key]

#way 2
for key in sorted(D.keys()):#sorted返回并对结果排序
    print key,"=>",D[key]

D.has_key('f')

##############元组，toople
#元组不能改变
t = (1,2,3,4,5)
t += (5,6,7)
print t

##############文件
f = open("data.txt",'w')
f.write("hello\n")
f.write('你好python\n')
f.close()

f = open('data.txt')
byte = f.read()
print byte

############### set
x = set("spam")
y = set(['h','a','m'])
print x,'\n',y
x&y  #交集，intersection
x|y  #并集，union
x-y  #差集，difference

################类
class worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)

Bob = worker('Bob Smith',5000)
Sue = worker('Sue Jones',6000)
print Bob.lastName()
Bob.giveRaise(.10)
print Bob.pay
