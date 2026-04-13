"""
#1
i=4
while i<10:
    i+=1
    if i==7 or i==9:
        continue
    print(i)
"""

#2
"""
s=0
while True:
    n=int(input("enter n:"))
    if n!=0:
        s+=n
    else:
        print(s)
        break
"""

#3
"""
summ=0
count =0
while True:
    num=int(input("enter the number:"))
    if num==-1:
        break
    summ+=num
    count+=1
    
if count==0:
    count =1
print(f" Average = {summ/count}")
"""

#4
"""
num=int(input("enter the number:"))
summ=0
while num>0:
    b=num%10
    num=num//10
    summ+=b
print(summ)
"""

#5
"""
num=int(input("enter the number:"))
rev=0
copy=num
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==copy:
    print("yes")
else:
    print("no")
"""

#6
"""
num=int(input("enter  the number:"))
var=False
while num>0:
    b=num%10
    c=num//10%10
    if b==c:
        var=True
    num=num//10
if var:
    print("yes")
else:
    print("no")
"""
#7
"""
i=99
while i<999:
    i+=1
    copy=i
    s=0
    while copy>0:
        s+=(copy%10)**3
        copy//=10
    if i==s:
        print(i,end="  ")
"""

#8
"""
num=int(input("enter  the number:"))
vur=2
while num>1:
    if num%vur==0:
        print(f"{vur}")
        num=num//vur
    else:
        vur+=1
"""


#9
"""
num2 = int(input("enter num2:"))
count=-1
num10=0
while num2>0:
    count+=1
    b=num2%10
    num10+=b*(2**count)
    num2//=10
print(num10)
"""


#10
"""
num10= int(input("enter num10:"))
num2=""
while num10>0:
    b=num10%2
    num10=num10//2
    num2+=str(b)

for i in num2[::-1]:
    print(i,end="")


#2)

num=int(input("enter num:"))
rev=""
while num>0:
    b=num%2
    rev=str(b)+rev
    num=num//2
print(rev)
"""

#11
"""
f1=0
f2=1
print(f"Fibonacci numbers: 0 1",end=" ")
while f1+f2<=50:
    f_sum=f1+f2
    print(f_sum,end=" ")
    f1,f2=f2,f_sum
"""

#12
#a)
"""
n=0
s=0
N=int(input("enter N:"))
while n<=N:
    n+=1
    s+=n/((1+n**3)**0.5)
print(s)


#b)

n=0
s=0
N=int(input("enter N:"))
while n<N:
    n+=1
    s+=(n**n)/n
print(s)


#c)
n=0
N=int(input("N:"))
s=0
while n<N:
    n+=1
    s+=(1.1**n+n**2)/5*n
print(s)
"""


#13
"""
print("1. ) Reqemleri topla")
print("2. ) Reqemleri vur")
print("3. ) Cixmaq ucun her hansi basqa bir knopkaya bas")
n=int(input("iki reqemli eded daxil edin:  "))
ch=input("Bir secim edin:  ")
res=0
while True:
    if ch=="1" or ch=="2":
        b=n%10
        c=n//10
        if ch=="1":
            res=(b+c)
        elif ch=="2":
            res=(b*c)
        print(res)
        break
    else:
        break
"""

#14
"""
num=int(input("number:"))
copy=num
num2=num**2
len_num=-1
l_n_2=-1
while num>0:
    num=num//10
    len_num+=1

ters=" "
while l_n_2<len_num:
    l_n_2+=1
    b=num2%10
    num2//=10
    ters=str(b)+ters

if int(ters)==copy:
    print("avtomorf")
else:
    print("no")

#14-2
N=int(input("enter N:"))
i=1
while i<=N:
    count=0
    i_copy=i
    while i_copy>0:
        count+=1
        i_copy//=10
    if i==((i*i)%(10**count)):
        print(f"{i}*{i}={i*i}")
    i+=1
"""


#15N natural ədədi daxil edin. N-dən böyük olmayan və öz rəqəmlərinin hər birinə bölünən 
#ədədləri ekrana çıxardın.
"""
i=1
N=int(input("enter N:"))
while i<=N:
    flag=True
    copy=i
    while copy>0:
        if copy%10==0:
            flag=False
            break
        elif i%(copy%10)!=0:
            flag=False
            break
        copy=copy//10
    if flag==True:
        print(i,end=" ")
    i+=1

"""
