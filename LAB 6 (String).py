#1
"""
txt=input("enter the text:")
string=input("Enter the symbol")

if string in txt:
    print(True)
else:
    print(False)
"""

#2
"""
txt=input("enter the string:")
new=""
for sym in txt:
    if sym=="B":sym="A"
    elif sym=="A":sym="B"
    elif sym=="a":sym="b"
    elif sym=="b":sym="a"
    new+=sym
print("Result:",end=" ")
print(new)
"""

#3
"""
string=input("enter the string:")
def my_split(string, delimiter):
    my_list = []
    word = ""
    for i in range(len(string)):
        if string[i] != delimiter:
            word += string[i]
        else:
            if word != "":
                my_list += [word]
                word = ""
    if word != "":
        my_list += [word]        
    return my_list

ls=my_split(string," ")
count=0
for i in ls:
    count+=1
print(f" The count of found numbers is:  {count}")
"""


#4
"""
string=input("enter the text:")
def my_split(string,delimiter):
    my_list=[]
    word=""
    for i in range(len(string)):
        if string[i]!=delimiter:
            word+=string[i]
        elif word!=" ":
            my_list+=[word]
            word=""
    if word!="":
        my_list+=[word]
    return my_list

ls=my_split(string," ")
ln=[]
for i in ls:
    ln+=[len(i)]

def maxi(ln):
    maxs=ln[0]
    for i in ln:
        if i>maxs:
            maxs=i
    return maxs

for j in ls:
    if len(j)==maxi(ln):
        print(f"{j}, uzunlugu {maxi(ln)}")
"""

#5
"""
string=input("enter your surname, patronyc, and name:")

def my_split(string,delimiter):
    my_list=[]
    word=""
    for i in range(len(string)):
        if string[i]!=delimiter:
            word+=string[i]
        elif word!="":
            my_list+=[word]
            word=""
    if word!="":
        my_list+=[word]
    return my_list  

ls=my_split(string," ")
surname=ls[0]
name=ls[1][0]
patronyc=ls[2][0]
print(f"Result: {name}.{patronyc}.  {surname}")
"""

#6
"""
file_spot=input("enter the path of file:")

def my_split(string,delimiter):
    my_list=[]
    word=""
    for i in range(len(file_spot)):
        if file_spot[i]!=delimiter:
            word+=file_spot[i]
        elif word!="":
            my_list+=[word]
            word=""
    if word!="":
        my_list+=[word]
    return my_list

path=my_split(file_spot,"/")
for i in path:
    print(i)
"""

#7
"""
def evez(cumle,axtar,deyis):
    word=" "
    i=0
    while i<len(cumle):
        if cumle[i: i+len(axtar)]==axtar:
            word+=deyis
            i+=len(axtar)
        else:
            word+=cumle[i]
            i+=1
    return word
cumle=input("cumle:")
axtar=input("axtar:")
deyis=input("deyis")
"""

#8
"""
text=input("enter the text:")
axtar=input("enter axtar:")
def finder(text,axtar):
    i=0
    count=0
    while i<len(text):
        if text[i:i+len(axtar)]==axtar:
            count+=1
        i+=1
    return count
print(finder(text,axtar))
"""
 
#9
"""
text=input("enter text:")
fin=input("enter the finder:")
rep=input("enter the replacer:")

def my_replace(text,fin,rep):
    i=0
    word=" "
    while i<len(text):
        if text[i: i+ len(fin)]==fin:
            word+=rep
            i+=len(fin)
        else:
            word+=text[i]
            i+=1
    return word

print(my_replace(text,fin,rep))
"""


#10
"""
cumle=input("cumle:")
axtar=input("axtar:")
deyis=input("deyis:")

def my_replace(cumle,axtar,deyis):
    i=0
    word=" "
    while i<len(cumle):
        if cumle[i: i+len(axtar)]==axtar:
            word+=deyis
            i+=len(axtar)
        else:
            word+=cumle[i]
            i+=1
    return word

print(my_replace(cumle,axtar,deyis))
"""

#11
"""
txt = input("enter text:")
new=""
ind=0
for i in txt:
    if i==" ":
        new+=i
        ind=0
    else:
        if ind!=1:
            new+=i
        ind+=1

print(new)
"""

#12
"""
sait="AQUE"
samit="bcmf"
reqem="3579"
durgu="”!?,;”"
t=[]
string=input("enter string:")

for i in string:
    if (i in sait) or (i in samit) or (i in reqem) or (i in durgu):
        j=i
    if j not in t:
        t+=[j]
print(*t)
"""   

#13
"""
string=input("enter:")

def my_split(string,delimiter):
    word=""
    my_list=[]
    for i in range(len(string)):
        if string[i]!=delimiter:
            word+=string[i]
        elif word!=" ":
            my_list+=[word]
            word=""
    if word!=" ":
        my_list+=[word]
    return my_list

t=my_split(string,"+")

summ=0
for i in t:
    summ+=int(i)
print(f"Cavab: {summ}")
"""

#14 ***
"""
string=input("enter the string:")
new=""
for i in string:
    if i=="-":
        new+="+-"
    else:
        new+=i
        
def my_split(string,delimiter):
    word=""
    my_list=[]
    for i in range(len(string)):
        if string[i]!=delimiter:
            word+=string[i]
        elif word!=" ":
            my_list+=[word]
            word=""
    if word!=" ":
        my_list+=[word]
    return my_list

t=my_split(new,"+")

sm=0
for j in t:
    sm+=int(j)
print(f"Result: {sm}")
"""

                
            
            


#15
"""
string=input("enter:")

def my_split(string,delimiter):
    my_list=[]
    word=""
    for i in range(len(string)):
        if string[i]!=delimiter:
            word+=string[i]
        elif word!=" ":
            my_list+=[word]
            word=""
    if word!=" ":
        my_list+=[word]
    return my_list

t=my_split(string," ")

print(f"Birinci soz: {t[0]}")
"""

#16
"""
string=input("enter the name of file:")

def my_split(string,delimiter):
    word=""
    my_list=[]
    for i in range(len(string)):
        if string[i]!=delimiter:
            word+=string[i]
        elif word!=" ":
            my_list+=[word]
            word=""
    if word!=" ":
        my_list+=[word]
    return my_list

ls=my_split(string,".")
n=len(ls)

name=""
for i in range(len(ls)):
    if i==n-1:
        continue
    else:
        name+=ls[i]
        
old_ext=ls[n-1]
new_ext=input("enter new extention:")

def my_replace(string,old_ext,new_ext):
    i=0
    w=""
    while i<len(string):
        if string[i: i+len(old_ext)]==old_ext:
            w+=new_ext
            i+=len(old_ext)
        else:
            w+=string[i]
            i+=1
    return w

print(my_replace(string,old_ext,new_ext))
"""

#17
"""
txt=input("enter the name of file:")
def length(txt):
    i=0
    for j in txt:
        i+=1
    return i

name=False
if length(txt)<=10:
    for i in txt:
        if i!=" "  and not (i in ban):
            name=True
        else:
            name=False

if name==True:
    print(f"{txt}.xlsx")
else:
    print("enter the right name")
"""

#18
"""
name=input("enter the name of file:")
ss=[".","-","~","_","=",":"]
def length(name):
    c=0
    for i in name:
        c+=1
    return c

l=False
if length(name)>=5 and length(name)<=15:
    l=True
else:
    print("The length of file is insufficient,it should be at least 5 and maximum 15")

sy=False
for a in name:
    if a in ss:
        sy=True
if sy==False:
    print("File name doesn't contain any special symbol!")

k=False
for a in name:
    if "a"<=a<="z":
        k=True
if k==False:
    print("File name does not contain any lowercase letter!")

b=False
for a in name:
    if "A"<=a<="Z":
        b=True
if b==False:
    print("File name does not contain any uppercase letter!")

r=False
for a in name:
    if "0"<=a<="9":
        r=True
if r==False:
    print("You should have at least one number in your name of file!")

if l==True and sy==True and k==True and b==True and r==True:
    print("Your name of file is correct!")
else:
    print("Your file name is not correct!")
"""
    
    
