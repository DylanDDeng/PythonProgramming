# List,dictionary,set 
# the value in list can be changed  
mylist = [1,3,True,6.5,'chileme']


mylist[2]  = False  # change the True value to the False Value
print(mylist)  
# duplicate the value in list 
mylist*3   
# some methods in list 
# append(item)
mylist.append(34) 
# pop 
mylist.pop()   
# pop(i) 删除列表中第i个元素的位置 
mylist.pop(0)  # 第1个元素删除
mylist 
# count(item) 返回item在列表中出现的次数 
mylist1 = [1,1,1,2,3,4,5,4] 
mylist1.count(1)  # mylist.count()  return error if no argument in the count()  
mylist1.count(4) 
# index(item)  返回列表中item的位置 
mylist1.index(max(mylist1))  
# sort（） 排序 
mylist1.sort()
mylist1 
#reverse() 倒序 
mylist1.reverse() 
mylist1 
# -----------------------------------------this is a line to separarete the content -----------------------------------------
# range fucntion 
range(0,10) # will not return anything 
list(range(0,10)) # use list function can return the value 
list(range(5,10)) 
list(range(5,10,2)) 
list(range(1,20,4))   
list(range(10,1,-2))  # reverse   

# -----------------------------------------this is a line to separarete the content ----------------------------------------- 
# string 字符串 
myName  = 'David'  
# length of string 
len(myName) 
# slice 
myName[2]   
# upper() 
myName.upper() 
# lower() 
myName.lower() 
# find(item) return item first time occur index 
myName.find('d')  
# split(schar) split the string at the location schar, return as list
myName.split('v')  
# count(item) return the times item occur 
myName.count('a')  
# center(w) 返回一个字符串，原字符串居中，使用空格填充新的字符串，使其长度为w 
myName.center(10) 
len(myName.center(10))
# list 是可以修改的 但是字符串不行 
# tuple 和列表类型，但是tuple 不能被修改 
# -----------------------------------------this is a line to separarete the content -----------------------------------------  
myTuple = (2,True,4.96) 
myTuple 
# length of myTuple 
len(myTuple) 
# slice 
myTuple[0] 
# *3 
myTuple*3 
#  slice 
myTuple[0:2] 
# if change the element in the tuple 
# will be error 
myTuple[1]  = 2  
# -----------------------------------------this is a line to separarete the content -----------------------------------------   
# set 
mySet = {4,6,7,5,'David',False}  
mySet 
# in 询问集中是否有元素 
4 in mySet 
# length 
len(mySet)  
# slice will  return error 
mySet[0]  # set is not subscriptiable  
# | or 
mySet1 = {'David',3,True,4,5,11} 
mySet | mySet1  
# & and
mySet & mySet1 
# -  
mySet - mySet1  # 返回只出现在mySet中的元素 
# <=
mySet1 <= mySet  
# add(item)
mySet.add('w') 
mySet 
# remove(item) 
mySet.remove('w') 
mySet 
# pop() 
mySet.pop() #随机移除set 中的一个元素  
# -----------------------------------------this is a line to separarete the content -----------------------------------------    
# dictionary 
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}  
capitals  
# 通过键访问对应的值 
capitals['Iowa'] 
# 添加新的值 
capitals['Utah'] = 'SaltLakeCity' 
capitals ['California'] = 'Sacramento'  
# length 
len(capitals)  
# keys（）
capitals.keys() 
len(capitals.keys()) 
# values() 
capitals.values()    
# items() 
capitals.items() 
for i in capitals.items(): 
    print(i) 
a = list(capitals.items())  
a[0][0]  
# get(k) 返回k对应的值，如果没有就返回None  
capitals.get('Iowa') 
# get(k,alt) 返回k对应的值，如果没有则返回alt 
capitals.get('China','error') 
# -----------------------------------------this is a line to separarete the content -----------------------------------------     
aName = input('Please enter your name:')  
print('Your Name in all capitals is', aName.upper(),'and has length is ',len(aName)) 

# type of input function is string, change to float 
sradius = float(input('Please enter the radius of the circle')) 
diameter = 2*sradius 
diameter  
# -----------------------------------------this is a line to separarete the content -----------------------------------------     
# 格式化字符串 
print('Hello') 
print('Hello','World')  
print('Hello','World',sep = '***')  
print('Hello World',end = '***')  
# 
age = float(input('Please enter the age: ')) 
print(aName,'is',age,'years old') 
#使用格式化字符串 
print('%s is %d years old.'%(aName,age)) # %s is string , %d is integer 
# 
price = 24 
item = 'banana' 
print('The %s costs %d cents' %(item, price))  
#.2f 
print('The %s costs %.2f cents' %(item, price))   
# while loop 
counter = 1 
while counter <=5: 
    print('hello world') 
    counter +=1  

counter = 1 
while counter < 10: 
    if counter % 2 ==0: 
        print("hello world")
    counter +=1 

for item in range(5): 
    print(item**2)

wordlist = ['cat','dog','rabbit'] 
letterlist = [] 

for aword in wordlist: 
    for letter in aword: 
        letterlist.append(letter) 
letterlist 

# list comprehension 
sqlist = [] 
for x in range(1,11): 
    sqlist.append(x**2) 
sqlist  

sqlist1 = [x**2 for x in range(1,11)] 
sqlist1

sqlsit2 = [x**2 for x in range(1,11) if x%2 ==0]
sqlsit2 

sqlist3 = [ch.upper for ch in 'comprehension' if ch not in 'aeiou' ] 
sqlist3 

import numpy as np 
anumber = int(input("Please enter an integer "))  
try: 
    print(np.sqrt(anumber)) 
except: 
    print("Bad value for square root")  
    print("Using absolute value instead") 
    print(np.sqrt(abs(anumber)))     

# function  --------------  
def square(n):  
    if n%2 ==0:  
        raise RuntimeError("We want the odd number not the even number ") 
    else: 
        print(n**2)

 #   return n**2 
square(6)

# 牛顿迭代法  
def squareroot(n): 
    root = n/2 
    for k in range(20): 
        root = (1/2)*(root + n/root)    
#        print(root)
#     print(k)
    return root  

squareroot(9)

# class 
class Fraction: 
    def __init__(self,top,bottom): 
        self.num = top 
        self.den = bottom  

    def show(self): 
        return str(self.num) + '/' + str(self.den)

myf1 = Fraction(3,5).show()
print(myf1)


class Fraction: 
    def __init__(self,top,bottom): 
        self.num = top 
        self.den = bottom   

    def __str__(self): 
        return str(self.num) + '/' + str(self.den) 
myf = Fraction(3,5)
print(myf) 


class Fraction: 
    def __init__(self,top,bottom): 
        self.num = top 
        self.den = bottom   

    def __str__(self): 
        return str(self.num) + '/' + str(self.den)  

    def __add__(self,otherfraction): 
        newnum = self.num * otherfraction.den  + self.den * otherfraction.num 
        newden = self.den * otherfraction.den 

        return Fraction(newnum, newden) 


f1 = Fraction(1,4) 
f2 = Fraction(1,2) 

print(f1 + f2) 

## gcd fucntion 
def gcd(m,n): 
    while m%n !=0: 
        oldm = m 
        oldn = n 

        m = oldn 
        n = oldm%oldn 
    return n  


class Fraction: 
    def __init__(self,top,bottom): 
        self.num = top 
        self.den = bottom   

    def __str__(self): 
        return str(self.num) + '/' + str(self.den)  

    def __add__(self,otherfraction): 
        newnum = self.num * otherfraction.den  + self.den * otherfraction.num 
        newden = self.den * otherfraction.den  

        common = gcd(newnum,newden) 

        return Fraction(newnum//common, newden//common)   

    def __eq__(self,other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 

        return firstnum == secondnum 
         

f1 = Fraction(1,4) 
print(f1) 
f2 = Fraction(1,2) 

print(f1 + f2) 

print(Fraction(1,4) + Fraction(3,7 ))  

# Logic Gate 
class LogicGate: 
    def __init__(self,n): 
        self.label = n 
        self.output = None 
    
    def getLabel(self): 
        return self.label 

    def getOutput(self): 
        self.output = self.performGateLogic() 
        return self.output  

# Binary Gate 
class BinaryGate(LogicGate): 
    def __init__(self,n): 
        super().__init__(n)
        
        self.pinA = None 
        self.pinB = None 

    def getPinA(self): 
        if self.pinA  == None: 
            return int(input("Enter Pin A input for gate" + self.getLabel() + "--->"))  
        else: 
            return self.pinA.getFrom().getOutput() 

    def getPinB(self): 
        return int(input("Enter Pin B input for gate" + self.getLabel() + "-->")) 

# Binary Gate 
class UnaryGate(LogicGate): 
    def __init__(self,n): 
        super().__init__(n) 

        self.pin = None 

    def getPin(self): 
        return int(input("Enter Pin input for gate "+ self.getLabel()+"--->")) 

# And Gate & Or Gate 
class AndGate(BinaryGate): 
    def __init__(self,n): 
        super().__init__(n)  
    
    def performGateLogic(self): 
        a = self.getPinA() 
        b = self.getPinB() 

        if a == 1 and b == 1: 
            return 1 
        else: 
            return 0  

# Connector 
class Connector: 
    def __init__(self,fgate,tgate): 
        self.fromgate = fgate 
        self.togate = tgate 

        tgate.setNextPin(self) 

    def getFrom(self): 
        return self.fromgate 

    def getTo(self): 
        return self.togate

def setNextPin(self,source): 
    if self.pinA ==  None:  
        self.pinA = source 

    else: 
        if self.pinB ==None: 
            self.pinB = source 
        else: 
            raise RuntimeError("No EMPTY PINS ")

 


