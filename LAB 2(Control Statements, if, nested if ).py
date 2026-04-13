#1
"""
a,b=map(int,input("a,b:").split())
if a>b:
    print("a is bigger than b")
else:
    print("b is bigger than a")
"""

#2
"""
a=int(input("a:"))
if a>0:
    print("a is positive")
else:
    print("a is negative")
"""

#3
"""
name=input("Enter the name of student:")
a,b,c=map(int,input("enter a,b,c:").split())
avg=(a+b+c)/3
if avg>=85:
    print("excellent")
elif avg>=75:
    print("very good")
elif avg>=65:
    print("good")
elif avg>=50:
    print("pass")
else:
    print("fail")
"""

#4
"""
a=int(input("enter a:"))
if a%3==0:
    print("yes")
else:
    print("no")
"""

#5
"""
a=int(input("enter a:"))
if a%6==0:
    print("yes")
else:
    print("no")
"""

#6
"""
a=int(input("enter a:"))
if a%2==0:
    print("yes")
else:
    print("no")
"""

#7
"""
a,b,c=map(int,input("a,b,c:").split())
sm=a+b+c
if a==b and b==c:
    sm*=3
else:
    sm=sm
print(sm)
"""
#8
"""
a,b,c=map(int,input("a,b,c:").split())
sm=a+b+c
if a==b or b==c or a==c:
    sm=0
else:
    sm=sm
print(sm)
"""
#9
"""
from math import *
a,b,c=map(int,input("a,b,c:").split())
d=b**2-(4*a*c)
if d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
elif d==0:
    x1=-b/(2*a)
    x2=x1
else:
    print("heqiqi koku yoxdur")
"""

#10
"""
price=float(input("enter the price:"))
disc=0
if price>1000:
    disc=price-(price*0.1)
    price=disc
else:
    price=price
print(price)
"""

#11
"""
price=float(input("enter the price:"))
disc=0
if price>500:
    disc=price-price*0.03
    price=disc
elif price>1000:
    disc=price-price*0.05
    price=disc
print(price)
"""
#12
"""
a,b=map(int,input("a,b:").split())
if a>b:
    print("a is bigger than b")
elif a<b:
    print("b is bigger than b")
else:
    print("a and b are equal")
"""

#13
"""
from random import *
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a is {a}")
print(f"b is {b}")
print(f"c is {c}")
if a>b and b>c:
    print(f"{b} is median")
elif a>c and c>b:
    print (f"{c} is median")
else:
    print(f"{a} is median")
"""
#14
"""
s=int(input("enter the number of figure's sides:"))
if s==10:
    print("decagon")
elif s==9:
    print("nonagon")
elif s==8:
    print("octagon")
elif s==7:
    print("heptagon")
elif s==6:
    print("hexagon")
elif s==5:
    print("pentagon")
elif s==4:
    print("quadrilateral")
elif s==3:
    print("triangle")
"""

#15
"""
year=input("long or short year:")
month = input("enter the name of the month:")
if  month=="April" or month=="June" or month=="September" or month=="November":
    print(f"There are 30 days in {month}")
elif month=="February" and year=="Long":
    print(f"There are 29 days in {month}")
elif month=="February" and year=="Short":
    print(f"There are 28 days in {month}")
else:    print(f"There are 31 days in {month}")
"""

#16
"""
asif_age=int(input("enter the age of Asif:"))
vasif_age=int(input("enter the age of Vasif:"))
agasif_age=int(input("enter the age of Agasif:"))
print(f"Asif age:{asif_age}")
print(f"Vasif age:{vasif_age}")
print(f"Agasif age:{agasif_age}")

if (asif_age>vasif_age and vasif_age>agasif_age) or (asif_age>agasif_age and agasif_age>vasif_age):
    print("Asif is the oldest")
elif (vasif_age>asif_age and asif_age>agasif_age) or (vasif_age>agasif_age and agasif_age>asif_age):
    print("Vasif is the oldest")
elif (agasif_age>vasif_age and vasif_age>asif_age) or (agasif_age>asif_age and asif_age>vasif_age):
    print("Agasif is the oldest")
elif (asif_age>vasif_age and vasif_age==agasif_age):
    print("Asif is the oldest,Vasif and Agasif are the peers")
elif (vasif_age>vasif_age and asif_age==agasif_age):
    print("Vasif is the oldest,Asif and Agasif are the peers")
elif (agasif_age>vasif_age and vasif_age==asif_age):
    print("Agasif is the oldest,Vasif and Asif are the peers")
"""

#17
"""
a,b,c=map(int,input("enter a,b,c:").split())
if a==b and b==c:
    print("beraberterefli")
elif a==b or b==c:
    print("beraberyanli")
elif a!=b and b!=c and a!=c:
    print("muxtelifterefli")
"""

#18
"""
db=int(input("enter the decibel level of noise:"))
if db>=130:
    print("It is a Jackhammer")
elif db>=106:
    print ("It is a Gas lawnmower")
elif db>=70:
    print("It is an Alarm Clock")
elif db>=40:
    print("It is a Quiet Room")
else:
    print("Enter again")
"""

#19
"""
year=int(input("enter the year:"))
if year%400==0:
    print(f"{year} is leap year")
elif year%100==0:
    print(f"{year} is not leap year")
elif year%4==0:
    print(f"{year} is  leap year")
else:
    print(f"{year} is  leap year")
"""

#20
"""
i=float(input("enter the magnitude of earthquake:"))
if i>=10.0:
    print("meteoric")
elif i>=8.0:
    print("great")
elif i>=7.0:
    print("major")
elif i>=6.0:
    print("strong")
elif i>=5.0:
    print("moderate")
elif i>=4.0:
    print("light")
elif i>=3.0:
    print("minor")
elif i>=2.0:
    print("very minor")
else:
    print("micro")
"""

#21
"""
alp=input("enter the letter a,b,c,d,e,f,g,h:")
num=int(input("enter the number:(1-8)::"))
if (alp=="a" or alp=="c" or alp=="e" or alp=="g") and num%2!=0:
        print(f" {alp}{num} is black")
elif (alp=="a" or alp=="c" or alp=="e" or alp=="g") and num%2==0:
    print(f" {alp}{num} is white")
elif (alp=="b" or alp=="d" or alp=="f" or alp=="h") and num%2==0:
    print(f" {alp}{num} is black")
elif (alp=="b" or alp=="d" or alp=="f" or alp=="h") and num%2!=0:
    print(f" {alp}{num} is white")
else:
    print("Enter right parametres")
"""

#22-A
"""
x= float(input("x:"))
y= float(input("y:"))
if x**2-2<=y and  ((x>=0 and ((y>=0 and x>=y) or (y<=0))) or (x<=0 and ((y>=0 and -x>=y) or (y<=0)))):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-B
"""
x,y=map(float,input("x,y:").split())
if x**2+y**2<=1 and ((x>=0 and y>=x) or (x<=0 and (y>=0 or y<=0))):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-C
"""
x,y=map(float,input("x,y:").split())
if x**2+y**2<=1 and ((x>=0 and (y>=0 and y<=0)) or (x<=0 and ((y>=0 and y>=-x) or (y<=0 and x>=y)))):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-D
"""
x,y=map(float,input("x,y:").split())
if (y>=2*x**2 and y>=1-x and  y>=0 and ((x>=0 and x<=1) or x<=0)) or (y<=2*x**2 and x>=0 and x<=1 and y>=0 and y>=1-x):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-E
"""
x,y=map(float,input("x,y:").split())
if (x**2+y**2<=1 and x>=0 and (y>=0 or y<=0)) or (x**2+y**2>=1 and x>=0 and y>=0 and y<=1 and y>=x-1):
    print("aiddir")
else:
     print("aid deyil")
"""

#22-F
"""
x,y=map(float,input("x,y:").split())
if (x**2+y**2<=1) or (x**2+y**2>=1 and 1>=x>=0 and 1>=y>=0):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-G
"""
x,y=map(float,input("x,y:").split())
if (x>=0 and y>=0 and y>=1/x and y<=-x+4) or (x<=0 and y<=0 and y<=1/x and y>=-x-4):
    print("aiddir")
else:
    print("aid deyil")
"""
#22-H
"""
x,y=map(float,input("x,y:").split())
if (x>=0 and y<=1 and y>=x**2) or (x<=0 and y>=-1 and y<=-x**2):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-J
"""
x,y=map(float,input("x,y:").split())
if x**2+y**2>=4 and x<=0 and y<=0 and y>=-2 and x>=y:
     print("aiddir")
else:
    print("aid deyil")
"""

#22-K
"""
x,y=map(float,input("x,y:").split())
if y>=(x-2)**2-3 and x>=0 and ((y>=0 and x>=abs(y)) or (y<=0 and x<=abs(y))):
    print("aiddir")
else:
    print("aid deyil")
"""

#22-L
"""
x,y=map(float,input("x,y:").split())
if x**2+y**2<=25 and (( x<=0 and (y>=0 and y>=x+2)) or (x<=0 and y<=0)):
     print("aiddir")
else:
    print("aid deyil") 
"""

#22-M
"""
x,y=map(float,input("x,y:").split())
if x**2+y**2<=1 and (x>=0 and ((y>=0 and 1-x>=y) or y<=0) or (x<=0 and y>=0)):
     print("aiddir")
else:
    print("aid deyil") 
"""
