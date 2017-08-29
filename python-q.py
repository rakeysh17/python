#!/opt/bin/python
dict = {'a' :  1, 'b' : 2, 'c' : 3}
dict['d'] = 4
del dict['a']
dict ['b'] = 1
print dict

#Path Variable
import os
print os.system('echo $PATH')

#multiple of 5

for i in range(1000, 5000, 5):
  print i

#Prime number
print "printing prime number between 20 and 100"

def division(t,u):
  return t % u

def prime(p):
  for i  in range(2, (p - 1)):
    if division(p , i) == 0:
      break
  else:
    return p 

for i in range(20,100):
  print prime(i)

#Biggest number

li_num = [1, 2, 4, 10, 6, 500, 100]    

def big(li):
  so = sorted(li)
  return so[len(li) - 1]

print big(li_num)

#List operation
a=['help','test',12,1000,'main']
print a
print "replace the 12 with  hello"
a[2] = "hello"
print a
print "create a nested list out of a"
a.append([1, 2, 3, 4])
print a
print "Insert the copy of a itself at the end"
a.extend(a)
print a

#Operation on string

str="Welcome to Python Programming"
print str
print "Print all charachters except last 4"
print str[ :(len(str) - 4)]

print "Print only last two characters"
print str
print str[len(str) - 2 : ]

print str
print """replace the word      "python" with "shell" else raise the exception"""
print str.replace("Python", "shell")

print str
print """Remove the word "Programming"""
print str.replace("Programming", "")

# Number negative 

num = int(raw_input())
print num
if num >=0:
  print  "%s is positive" % num
else:
  print "%s in negative" % num

#fibonacci series
num1 = 0
sum1 = 1
print "fibonacci series"
print sum1
while (num1 <= 200):
  sum1 = sum1 + num1
  print sum1
  num1 = sum1 - num1

#nested tuples
print "nested tuples"

x = [1,2,3,4,5]
y =  x.append(x)
print tuple(x) 
