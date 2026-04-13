#1 
"""
num=int(input("enter number:"))
x=int(input("enter the slope:"))
num_2=1
for i in range(1,x+1):
    num_2*=num
print(num_2)
"""
#2
"""
A=int(input("enter the number:"))
A_fact=1
for i in range(1,A+1):
    A_fact*=i
print(f"The factorial of {A} is {A}!=={A_fact}")
"""
#3
"""
for i in range(1,51):
    if i%2==0:
        print(i,end=",")
"""

#4
"""
N=int(input("enter N:"))
sm=0
for i in range(1,N+1):
    sm+=i
print(sm)
"""

#5
"""
n,x=map(int,input("enter n,x:").split())
sm=1
for i in range(1,n+1):
    if i%2!=0:
        sm-=x**i
    else:
        sm+=x**i
print(sm)
"""

#6
"""
for i in range(100,0,-1):
    print(i)
"""

#7
"""
for i in range(0,11):
    print(i, i**2)
"""

#8
"""
sm=0
pr=1
for i in range(0,11):
    if i%2==0:
        sm+=i
    else:
        pr*=i
print(sm)
print(pr)
"""

#9
"""
a,b,c=map(int,input("a,b,c:").split())
for i in range(a,b+1):
    if i%c==0:
        print(i,end=",")
"""

#10
"""
a,b,=map(int,input("a,b:").split())
c_odd=0
c_even=0
for i in range(a,b+1):
    if i%2==0:
        c_even+=1
    else:
        c_odd+=1
print(f"The number of even numbers is {c_even}")
print(f"The number of odd numbers is {c_odd}")
"""

#11
"""
from random import *
for i in range(10):
    a=randint(1,100)
    if a%2==0:
        print("evens:",end="")
        print(f"{a}")
    else:
        print("odds:",end="")
        print(a)
"""
#12
"""
a,b=map(int,input("a,b:").split())
for i in range(a,b+1):
    print(f"{i}*{i}={i**2}")
"""
#13
"""
num_1=int(input("enter the  number1:"))
num_2=int(input("enter the number2:"))
res=0
for i in range(num_1):
    res+=num_2
print(res)
"""

#14
"""
n=int(input("n:"))
pi=3
for i in range(2,n+1):
    if i%2==0:
        pi+=4/(i*(i+1)*(i+2))
    else:
         pi-=4/(i*(i+1)*(i+2))
print(pi)
"""
#15
"""
for i in range(10000,99999):
    if i%133==125 and i%134==111:
        print(i,end=",")
"""

#16
"""
a=int(input("enter a:"))
b=int(input("enter b:"))
ebob=0
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        ebob=i
print(ebob)
"""

#17
"""
a=int(input("enter a:"))
b=int(input("enter b:"))

for i in range(a,b+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0:
        print(i)
"""            

#18
"""
count=0
for x in range(1,185//15+1):
    for y in range(1,185//17+1):
        for z in range (1,185//21+1):
            if 15*x+17*y+21*z==185:
                count+=1
print(count)
"""
