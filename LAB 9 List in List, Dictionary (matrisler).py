###1

#a) matrisin mutleq qiymetice elementlerin cemini tap:
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter columns:"))

a=[[randint(-10,10)for i in range(col)]for j in range(row)]

sums=0

for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
        sums+=a[i][j]
    print()
print(sums)
"""

#b) matrisin elemntlerin kvadratin hasilini tapin:
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))

a=[[randint(-10,10)for i in range(col)]for j in range(col)]

p=1
for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
        p*=(a[i][j]**2)
    print()
print(p)
"""

#c) k nomreli setrin elementlerin hasili tapin(0<k<row):
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
k=int(input("enter the k:")) #row
a=[[randint(-10,10)for i in range(col)]for j in range(col)]
pr=1
for i in range(row):
    for j in range(col):
      if i==k:
          pr*=a[i][j]
      print("{:4d}".format(a[i][j]),end="")
    print()
print(pr)
"""

#d)  Ən kiçik elementinin yerləşdiyi sütun elementlərinin cəmini tapın.
"""
from random import *
from math import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(-10,10)for i in range(col)]for j in range(col)]
mins=a[0][0]
x=0
s=0
for i in range(row):
    for j in range(col):
        if int(a[i][j])<mins:
            mins=int(a[i][j])
            x=j
        print("{:4d}".format(a[i][j]),end="")
    print()
print(mins)
print(x)

for i in range(row):
    for j in range(col):
        if j==x:
            s+=a[i][x]
print(s)
"""

#e)
"""
from random import *
row=int(input("enter rows:"))
col=int(input("enter columns:"))
a=[[randint(-10,10)for i in range(col)]for j in range(row)]

for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
    print()

ld=[]
rd=[]
if row==col:
    for i in range(row):
        for j in range(col):
            if i+j==row-1:
                ld+=[a[i][j]]

    for i in range(row):
        rd+=[a[i][i]]

print(f"Sag dioqanal: {rd}")
print(f"Sol diaqonal: {ld}")

sld=0
srd=0
for x in ld:
    sld+=x

for x in rd:
    srd+=x

if srd>sld:
    print("Sagdakin cemi boyukdu")
elif sld>srd:
    print("Soldakin cemi boyukdu")
else:
    print("Cemleri hem sol hem sag beraber")
"""




###2
#a)
"""
from random import *
row=int(input("enter rows:"))
col=int(input("enter columns:"))
a=[[randint(-10,10)for i in range(col)]for j in range(row)]
b=[[randint(-10,10)for i in range(col)]for j in range(row)]

print("Matrix A:")
for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
    print()

print("Matrix B:")
for i in range(row):
    for j in range(col):
        print("{:4d}".format(b[i][j]),end="")
    print()


s_same=0
d_same=0
for i in range(row):
    for j in range(col):
        s_same+=(a[i][j]+b[i][j])
        d_same+=(a[i][j]-b[i][j])
        
   
c=[[choice([d_same,s_same]) for i in range(col)]for j in range(row)]
print("Matrix C:")
for i in range(row):
    for j in range(col):
        print("{:4d}".format(c[i][j]),end="")
    print()
"""

#b) 
"""
from random import *
row=int(input("enter rows:"))
col=int(input("enter columns:"))
a=[[randint(-10,10)for i in range(col)]for j in range(row)]
k=int(input("k:")) #row
m=int(input("m:")) #col

print("Matrix A:")
for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
    print()

B=[]
for i in range(row):
    B+=[a[k][i]*a[i][m]]
print("Massiv B:",end=" ")
print(B)
"""
#c)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
k=int(input("enter the k:")) #row
a=[[randint(-10,10)for i in range(col)]for j in range(col)]

for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
    print()

B=[]
for i in range(row):
    B+=[(a[k][i]/a[i][i])]
print("B",end="=")
print(B)
"""

#d)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(-10,10)for i in range(col)]for j in range(col)]

for i in range(row):
    for j in range(col):
        print("{:4d}".format(a[i][j]),end="")
    print()

mds=0
for i in range(row):
    mds+=a[i][i]

print("Reformed matrix:")
for i in range(row):
    for j in range(col):
        if(i+1)%2==0:
            print("{:4d}".format(a[i][j]//mds,2),end="")
        else:
            print("{:4d}".format(a[i][j]),end="")
    print()
"""

#e)
"""
from random import *
n=int(input("n:"))
a=[[randint(-10,10)for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        print("{:4d}".format(a[i][j]),end="")
    print()

B=[]
for i in range(n):
    s=0
    for j in range(n):
        s+=a[i][j]
    B+=[s]
    
print()
print()
print(B)
"""

#f)
"""
from random import *
n=int(input("n:"))
a=[[randint(-10,10)for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        print("{:4d}".format(a[i][j]),end="")
    print()

B=[]
for i in range(n):
    pr=1
    for j in range(n):
        pr*=a[j][i]
    B+=[pr]
print()
print()
print("B",end="=")
print(B)
"""

###3
"""
#a)

from random import *
n=int(input("enter the n:"))
a=[[randint(10,100)for i in range(n)]for j in range(n)]

maks=a[0][0]
ind_i=0
ind_j=0
for i in range(n):
      for j in range(n):
          if a[i][j]>maks:
              maks=a[i][j]
              ind_i=i
              ind_j=j
          print("{:4d}".format(a[i][j]),end="")
      print()
print(f"{maks}")
print(f"Indeksleri: [{ind_i}],[{ind_j}]")

#b)
print()
print()
print()
print("Reversed columns matrix:")
for i in range(n-1,-1,-1):
    for j in range(n):
          print("{:4d}".format(a[i][j]),end="")
    print()
    
#c

print()
print()
print("pronic numbers in matrix:")
def pronic(num):
    pronic=False
    for c in range(1,num+1):
        if c*(c+1)==num:
            pronic=True
    return pronic

p_list=[]
for i in range(n):
    for j in range(n):
        if (i+1)%2==0:
            if pronic(a[i][j])==True:
                p_list+=[a[i][j]]
print(p_list)

#d)

print()
print()
print()
def sade(num):
    c=0
    s=False
    for i in range(2,num):
        if num%i==0:
            c+=1
    if c==0:
        s=True
    return s
md=[]
idq=[]
pl=[]
for i in range(n):
    md+=[a[i][i]]

for i in range(n):
    for j in range(n):
        if i+j==n-1:
            idq+=[a[i][j]]

for a in md:
    if sade(a)==True:
        pl+=[a]

for a in idq:
    if sade(a)==True:
        pl+=[a]
print("The list with numbers of diaqonal, the prime ones:")
print(pl)
"""

###4
#a)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(10,99)for i in range(col)]for j in range(row)]
n=row*col
s=0
print("Matrix A:")
for i in range(row):
    for j in range(col):
        s+=a[i][j]
        print("{:4d}".format(a[i][j]),end="")
    print()
avm=s/n

for i in range(row):
    for j in range(col):
        if a[i][j]<avm:
            a[i][j]=0
        else:
            a[i][j]=255
        print("{:4d}".format(a[i][j]),end="")
    print()
"""

#b)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(10,99)for i in range(col)]for j in range(row)]

print("Matrix A:")
for i in range(row):
    for j in range(col):
          print("{:4d}".format(a[i][j]),end="")
    print()

print()
print()
for i in range(row):
    for j in range(col):
        if (i==j or j>i) and a[i][j]>50:
            a[i][j]=255
            print("{:4d}".format(a[i][j]),end="")
        elif (i==j or j>i) and a[i][j]<50:
            a[i][j]=0
            print("{:4d}".format(a[i][j]),end="")
        else:
            print("{:4d}".format(a[i][j]),end="")
    print()
"""


#c)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(10,99)for i in range(col)]for j in range(row)]

print("Matrix A:")
for i in range(row):
    for j in range(col):
          print("{:4d}".format(a[i][j]),end="")
    print()

print()
print()
for i in range(row):
    for j in range(col):
        if (i==j or j>i):
            a[i][j]=0
            print("{:4d}".format(a[i][j]),end="")
        else:
            print("{:4d}".format(a[i][j]),end="")
    print()
"""

#d)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(10,99)for i in range(col)]for j in range(row)]

print("original matrix:")
for i in range(row):
    for j in range(col):
          print("{:4d}".format(a[i][j]),end="")
    print()

print("reversed matrix:")
for i in range(row):
    for j in range(col-1,-1,-1):
          print("{:4d}".format(a[i][j]),end="")
    print()
"""

#e)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(10,99)for i in range(col)]for j in range(row)]

print("original matrix:")
for i in range(row):
    for j in range(col):
          print("{:4d}".format(a[i][j]),end="")
    print()

print("reversed matrix:")
for i in range(row-1,-1,-1):
    for j in range(col):
          print("{:4d}".format(a[i][j]),end="")
    print()
"""

#f)
"""
from random import *
row=int(input("enter row:"))
col=int(input("enter col:"))
a=[[randint(10,99)for i in range(col)]for j in range(row)]

print("original matrix:")
for i in range(row):
    for j in range(col):
          print("{:4d}".format(a[i][j]),end="")
    print()
print()
print()
print("90 degrees reversed matrix:")
for i in range(row):
    for j in range(col-1,-1,-1):
        print("{:4d}".format(a[j][i]),end="")
    print()
"""

#5
"""
from random import *
n=int(input("enter the n(tek):"))
col_width = 6

a=[[randint(10,20)for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
          if (i==j) or j==0 or j==n-1:
              a[i][j]="+"

for i in range(n):
    row_str = ""
    for j in range(n):
        item = str(a[i][j])
        spaces = " " * (col_width - len(item))
        row_str = row_str + item + spaces
    print(row_str)

print()
print()

b =[[randint(10,20)for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if (i==0) or (j==0) or (j==n-1) or (i==n//2):
                                            b[i][j]="+"

for i in range(n):
    row_str=""
    for j in range(n):
        item=str(b[i][j])
        spaces=" "*(col_width-len(item))
        row_str=row_str+item+spaces
    print(row_str)
    
print()
print()

c=[[randint(10,20)for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if j==n//2 and i>n//2:
            c[i][j]="0"
        elif i==j and j<(n//2+1):
            c[i][j]="0"
        elif i+j==n-1 and j>=(n//2+1):
            c[i][j]="0"

for i in range(n):
    row_str=""
    for j in range(n):
        item=str(c[i][j])
        space=" "*(col_width-len(item))
        row_str=row_str+item+space
    print(row_str)

print()
print()
d=[[randint(10,20)for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            d[i][j]=0
        print("{:4d}".format(d[i][j]),end="")
    print()

print()
print()
e=[[randint(10,20)for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (i+j==n-1):
            e[i][j]=0
        print("{:4d}".format(e[i][j]),end="")
    print()

print()
print()
e=[[randint(10,20)for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            e[i][j]=0
            print(e[i][j],end="  ")
        else:
            print(e[i][j],end=" ")
    print()
"""
