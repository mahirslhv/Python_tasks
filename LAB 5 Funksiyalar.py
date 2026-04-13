#1
"""
def checker():
    s=0
    while True:
        i=int(input("enter i:"))
        if i!=(-1):
            s+=i
        else:
            return s

if checker()%2==0:
    print("cut")
else:
    print("tek")
"""

#2
"""
def odd_even(a,b):
    if a>b:
        c=a%b
    else:
        c=b%a
    if c%2==0:
        return f"{c} is even reminder"
    else:
        return f"{c} is odd reminder"
a,b=map(int,input("a,b:").split())
print(odd_even(a,b))
"""

#3\
"""
n=int(input("n:"))
k=int(input("k:"))
def check(n,k):
    if k**k==n:
        return True
    else:
        return False
print(check(n,k))
"""

#4


#5
"""
n=int(input("enter n:"))
def length(n):
    count=-1
    if n<0:
        n=abs(n)
    while n>0:
        b=n%10
        count+=1
        n=n//10
    return count
print(length(n))
"""

#6
"""
n=int(input("enter n:"))  
def disarium(n):
    ters=0
    copy=n
    while n>0:
        b=n%10
        ters=ters*10+b
        n=n//10
        
    c=0
    dis=0
    while ters>0:
        c+=1
        d=ters%10
        dis+=d**c
        ters=ters//10
    if copy==dis:
        return f"{copy} is disarium"
    else:
        return f"{copy} is not disarium"
    
print(disarium(n))
"""

#7
"""
n=int(input("n:"))
def curson(n):
    a=2**n+1
    b=2*n+1
    if a%b==0:
        return f"{n} is  curson"
    else:
        return f"{n} is not curson"
print(curson(n))
"""

#8
"""
n=int(input("n:"))

def factorial(i):
    fact=1
    f=0
    while f<i:
        f+=1
        fact*=f
    return fact

def kempner(n):
    i=0
    while i<n:
        i+=1
        if factorial(i)%n==0:
            return f"{i}!->{n}"
print(kempner(n))
"""

#9
"""
n=int(input("n:"))

def sade(res):
    count=0
    for i in range(2,res):
        if res%i==0:
            count+=1
    if count==0:
        return True
    else:
        return False
    
def moran(n):
    copy=n
    s=0
    while n>0:
        b=n%10
        s+=b
        n=n//10
    res=copy//s
    if sade(res)==True:
        return f"{copy} is moran"
    else:
        return f"{copy} is not  moran"
print(moran(n))
"""


#10
"""
from math import*
n=int(input("enter n:"))
def checker(n):
    copy=n
    ters=0
    while n>0:
        b=n%10
        ters=ters*10+b
        n=n//10
    a=ters%10
    d=copy%10
    q=sqrt(d+b)

    if q>3:
        return True
    else:
        return False
print(checker(n))
"""

#12
"""
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
def num_ch(x,y):
    for i in range(2,x):
        for j in range(2,y):
            if x%i==0 and y%j==0 and i==j:
                return False
            else:
                return True
print(num_ch(num1,num2))
"""

#13 ???


#14
"""
n1=int(input("n1:"))
n2=int(input("n2:"))
def ekob_ebob(n1,n2):
    ebob=0
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            ebob=i

    ekob=(n1*n2)/ebob
    return ebob,ekob
print(ekob_ebob(n1,n2))
"""

#15
"""
a,b,c=map(int,input("a,b,c:").split())

def checker(a,b,c):
    
    if a > b:
        a, b = b, a  
    if a > c:
        a, c = c, a 
    if b > c:
        b, c = c, b

    return f"Sıralama: {a}, {b}, {c}"
print(checker(a,b,c))
"""

#16
"""
n1,n2=map(int,input("Kesrin surret ve mexrecini daxil edin:  ").split())

def ebob(n1,n2):
    ebob=0
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            ebob=i
    return ebob

k=int(n1/(ebob(n1,n2)))
m=int(n2/(ebob(n1,n2)))
print(f"{k}/{m}")
"""

#17
"""
n=int(input("Natural eded daxil edin:  "))
def ters_eded(n):
    ters=""
    while n>0:
        b=n%10
        ters=ters+str(b)
        n=n//10
    return f"Ters eded: {ters}"
print(ters_eded(n))
"""

