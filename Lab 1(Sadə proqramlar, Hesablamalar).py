#1
"""
a=int(input("a:"))
print(a**4)
"""

#2
"""
w=int(input("enter width:"))
l=int(input("enter length:"))
area=w*l
print(area)
"""

#3
"""
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
V=a*b*c
S=2*(a*b+b*c+a*c)
print(f" volume is {V}")
print(f" area is {S}")
"""

#4
"""
from math import *
r=int(input("r:"))
h=int(input("h:"))
S=pi*r**2*h
print(S)
"""

#5
"""
from math import *
a=int(input("a:"))
b=int(input("b:"))
q=int(input("q:"))
q=radians(q)
S=0.5*a*b*sin(q)
print(S)
"""

#6
"""
a,b,c=map(int,input().split())
avg=(a+b+c)/3
pr=a*b*c
print(avg)
print(pr)
"""

#7
"""
from random import *
a=randint(1000,9999)
b=a%10
c=a//10%10
d=a//100%10
e=a//1000
sums=b**2+c**2+d**2+e**2
pr=(b*c*d*e)**2
print(a)
print(sums)
print(pr)
"""
#8
"""
from random import *
a=uniform(6.5,10.5)
b=uniform(6.5,10.5)
pr=a*b
print("{:.2f}".format(pr))
print(round(pr,2))
"""

#9
"""
from random import *
a=randint(10000,99999)
for i in str(a):
    print(int(i),   int(i)**2)
"""

#10
"""
from math import *
from random import *
x=uniform(-1,1)
y=uniform(-1,1)
a=sqrt(1+y**2)*sin(x**2/(1+abs(y)))
b=cos((sin(5*x)**2)/(sqrt(abs(y))))
print(a)
print(b)
"""

#11
"""
a=int(input("enter the 3digit number:"))
b=a%10
c=a//10%10
d=a//100
print(d,c,b)
"""
