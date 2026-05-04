#1
"""
from random import *
n=int(input(":"))
a=[randint(0,5) for i in range(n)]

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]

A=bubble_sort(a,k=1)
print(a)

x=int(input("enter the searched number:"))
for i in range(len(A)):
    if A[i]==x:
        print(f"A[{i}]={x}",end=",")
"""

#2
"""
from random import *
n=int(input(":"))
a=[randint(10,100) for i in range(n)]
print(a)

def ss(i):
    sm=0
    while i>0:
        b=i%10
        sm+=b
        i=i//10
    return sm

def num_sums(a):
    ls=[]
    for i in a:
        ls+=[ss(i)]
    return ls

f=num_sums(a)

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]

print(bubble_sort(f,k=-1))
"""

#3
"""
ls=[]
n=int(input(":"))
for i in range(n):
    a=input(f"{i+1}.")
    ls+=[a]
print(ls)

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]
print(bubble_sort(ls,k=1))
"""

#4  mentiqin tapmisam amma printde problem yaradir:
'''
ls=[]
n=int(input(":"))
def my_split(string,delimiter):
    word=""
    ls=[]
    for i in string:
        if i!=delimiter:
            word+=i
        else:
            if word!="":
                ls+=[word]
                word=""
    if word!=" ":
        ls+=[word]
    return ls

print("Ad, ata adi ve soyadinizi daxil edin:")
for i in range(n):
    a=input(f"{i+1}.")
    ls+=[my_split(a," ")]

print(ls)

for i in range(len(ls)-1):
    if ls[i][1][0]>ls[i+1][1][0]:
        ls[i][1],ls[i+1][1]=ls[i+1][1],ls[i][1]
        ls[i][0],ls[i+1][0]=ls[i+1][0],ls[i][0]

for i in range(len(ls)):
    print(ls[i][0],ls[i][1])
'''


#5
"""
from random import *
Unsorted_B=[randint(-100,100)for i in range(10)]
print(f"Unsorted_B={Unsorted_B}")
def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]
Sorted_1B=bubble_sort(Unsorted_B,k=-1)
print(f"Sorted_1B={Sorted_1B}")
hs1=Sorted_1B[:len(Sorted_1B)//2]
hs2=Sorted_1B[len(Sorted_1B)//2:]
h1=bubble_sort(hs1,k=1)
h2=bubble_sort(hs2,k=1)
print(f"Sorted_2B",end="=")
print(h1+h2)
"""

#6
"""
from random import *
n=int(input(":"))
a=[randint(-100,100)for i in range(n)]
print("Massiv:",end=" ")
print(*a)

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]

h1=[]
h2=[]
for i in a:
    if i>0:
        h1+=[i]
    else:
        h2+=[i]

h1=bubble_sort(h1,k=-1)
h2=bubble_sort(h2,k=1)
h=h1+h2
print("Netice:",end=" ")
print(*h)

c=0
for i in a:
    if i>0:
        c+=1
print("Musbet elementlerin sayi:",end=" ")
print(c)
"""

#7
"""
from random import *
a=[randint(1,10000)for i in range(1000)]
b=[randint(1,10000)for i in range(1000)]
c=[randint(1,10000)for i in range(1000)]
d=[randint(1,10000)for i in range(1000)]
e=[randint(1,10000)for i in range(1000)]

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]
print("sorted_a",end=" = ")
print(bubble_sort(a,k=1))
print("sorted_b",end=" = ")
print(bubble_sort(b,k=1))
print("sorted_c",end=" = ")
print(bubble_sort(c,k=1))
print("sorted_d",end=" = ")
print(bubble_sort(d,k=1))
print("sorted_e",end=" = ")
print(bubble_sort(e,k=1))
"""

#8
"""
from random import *
n=int(input("enter n:"))
a=[randint(1,100)for i in range(n)]

print("Massiv:",end=" ")
print(*a)

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]
print("Cesidlemeden sonra:",end=" ")
print(*bubble_sort(a,k=1))

x=int(input("enter x:"))
c=0
for i in a:
    if i==x:
        c+=1

if c==0:
    print(f"{x} ededi tapilmadi")
elif c>0:
    print(f"{x} ededi tapildi")
    print("Muqayiselerin sayi:",end=" ")
    print(c)
"""

#9
"""
from random import *
n=int(input("enter n:"))
a=[randint(1,100)for i in range(n)]

print("Massiv:",end=" ")
print(*a)

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]
print("Cesidlemeden sonra:",end=" ")
print(*bubble_sort(a,k=1))

x=int(input("enter x:"))
c=0
for i in a:
    if i==x:
        c+=1

if c==0:
    print(f"{x} ededi tapilmadi")
elif c>0:
    print(f"{x} ededi {c} defe tekrarlanir")
"""

#10
"""
from random import *
n=int(input("enter n:"))
a=[randint(1,100)for i in range(n)]

print("Massiv:",end=" ")
print(*a)

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]
print("Cesidlemeden sonra:",end=" ")
print(*bubble_sort(a,k=1))

x=int(input("enter x:"))
c=0
for i in a:
    if i==x:
        c+=1

def close(a):
    cl=0
    for i in a:
        if i>x:
            cl=i
            break
            
    return cl
            
if c==0:
    print(f"{x} ededi tapilmadi  En yaxin eded: {close(a)}")
elif c>0:
    print(f"{x} ededi tapildi")
"""

#11
"""
from random import *
n=int(input(":"))
a=[randint(100,999)for i in range(n)]

print("Massiv",end=": ")
print(*a)
h1=a[:len(a)//2]
h2=a[len(a)//2:]
print("Ilk yarsi:",end=" ")
print(*h1)
print("Son yarsi:",end=" ")
print(*h2)

def ss1(num):
    c=0
    while num>0:
        b=num%10
        if b%2!=0:
            c+=1
        num=num//10
    return c
        
def ss2(num):
    c=0
    while num>0:
        b=num%10
        if b%2==0:
            c+=1
        num=num//10
    return c

h1c=[]
for i in h1:
    h1c+=[ss1(i)]

h2c=[]
for i in h2:
    h2c+=[ss2(i)]

print("Tek reqemlerin sayi ilk yarsi",end=": ")
print(*h1c)
print("Cut reqemlerin sayi son yarsi",end=": ")
print(*h2c)

def bubble_sort(arr,a,k):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]

h1=bubble_sort(h1c,h1,k=1)
h2=bubble_sort(h2c,h2,k=-1)

print("Cesidlemeden sonra",end=": ")
print(*(h1+h2))
"""


#12
"""
from random import *
n=int(input(":"))
a=[randint (1,1001)for i in range(n)]

print(f"my_list={a}")

def bubble_sort(a,k):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    if k>0:
        return a
    else:
        return a[::-1]

h1=bubble_sort(a[:len(a)//2],k=1)
h2=bubble_sort(a[len(a)//2:],k=-1)

print("mylist",end="=")
print(h1+h2)
"""
