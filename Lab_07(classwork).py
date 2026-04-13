#1 Aşağıdakı tuple-da verilmiş 24 ədədinin indekslərini çap edin.
"""
tuples = (4,6,3,9,12,24,24,76,63)
count=0
for i in tuples:
    if i!=24:
        count+=1
    else:
        break
print(f"The index of 24 in given tuple is {count}")
"""

#2 Aşağıdakı tuple-da verilmiş ədədlərdən 3-ə bölünən ədədləri çap edin.
"""
Tuple = (4, 6, 3, 9, 12, 24, 24, 76, 63)
for i in Tuple:
    if i%3==0:
        print(i,end="  ")
"""


#3. İstifadəçi tərəfindən 5 ədəd daxil edilərək list yaradın. Listin hər bir ədədini 5 vahid 
#artıraraq yeni listə köçürün və çap edin.
"""
List1=[int(input(f"{i+1}.  "))for i in range(5)]
List2=[]
for j in List1:
    List2+=[(j+5)]
print("List1",end=" = ")
print(List1)
print("List2",end=" = ")
print(List2)
"""

#4 İstifadəçi tərəfindən 5 ədəd daxil edilərək list yaradın. Listin tərkibindəki cüt ədədləri 
#listdən çıxarmaqla qalan elementləri yeni listə yığıb, çap edən proqram yazın.
"""
List1=[int(input(f"{i+1}.  ")) for i in range(5)]
List2=[]
for j in List1:
    if j%2!=0:
        List2+=[j]
print("List1",end=" = ")
print(List1)
print("List2",end=" = ")
print(List2)
"""

#5 Listi [0, 10] intervalı arasında təsadüfi ədədlərlə doldurun (ədədlərin sayı = 7) və bütün 
#elementlərin a) cəmini, b) hasilini, c) ədədi ortasını, d) ən böyüyünü və onun indeksini, 
#e) ən kiçiyini və ounu indeksini tapan proqram yazın (Heç bir hazır funksiyadan istifadə 
#etmək olmaz!)
"""
from random import *
List = [randint(1,10) for i in range(7)]
Cem=0
Hasil = 1
c=0

for j in List:
    c+=1
    Cem+=j
    Hasil*=j
    Ededi_orta = Cem/c

def maxs(List):
    Max_num=List[0]
    for i in List:
        if i>Max_num:
            Max_num=i
    return Max_num

def mins(List):
    Min_num=List[0]
    for i in List:
        if i<Min_num:
            Min_num=i
    return Min_num

max_in=0
min_in=0
for z in List:
    if z!=maxs(List):
        max_in+=1
    else:
        break

for c in List:
    if c!=mins(List):
        min_in+=1
    else:
        break


print(List)
print(f" Cem = {Cem}      Hasil={Hasil}     Ededi orta = {Ededi_orta}")
print(f" En boyuk eded  =  {maxs(List)}  ,  indeks = {max_in}")
print(f" En kicik eded = {mins(List)}   ,    indeks = {min_in}")
"""


#6 Massivi [0, 100] intervalında olan təsadüfi ədədlərlə doldurun (ədədlərin sayı = 10). 50
#dən kiçik olan və 50-dən böyük bərabər olan elementlərinin ədədi ortasını çap edən 
#proqram yazın.
"""
from random import *
List = [randint(1,100) for i in range(10)]
sum1=0
c1=0
sum2=0
c2=0
for i in List:
    if i<50:
        c1+=1
        sum1+=i
        avg1=sum1/c1
    else:
        c2+=1
        sum2+=i
        avg2=sum2/c2
print(List)
print(f" [0,50) aralaginda ededi orta = {avg1}")
print(f" [50,100) aralaginda ededi orta = {avg2}")       
"""


#7  1 ilə 15 arasında olan ədədlərin kvadratlarından təşkil olunmuş listdə ilk 5 və son 5 
#elementləri çap edən proqram yazın.
"""
List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
print(List[0:5])
print(List[10:])
"""

#8 Verilmiş iki listin ortaq elementi varsa True, yoxdursa False nəticəsi verən funksiya 
#yazın.
"""
List1 = [1, 2, 3]
List2 = [2, 4, 6]
var=False
for i in List1:
    for j in List2:
        if i==j:
            var=True
"""

#9 2 listdə eyni indeksdə yerləşən eyni elementləri və onların sayını ekrana çıxaran 
#proqram yazın.
"""
List1 = [11, 22, 33, 44, 55] 
List2 = [12, 23, 33, 45, 55]
ls=[]
count=0
n=len(List1)
for i in range(n):
    if List1[i]==List2[i]:
        count+=1
        ls+=[List1[i]]
print("List1",end=" = ")
print(List1)
print("List2",end=" = ")
print(List2)
print("Tekrarlanan elementler:",end=" " )
print(*ls)
print(f"Eyni indeksde yerleshen eyni elemntlerin sayi = {count}")
"""

#10
"""
from random import *
List1 = [randint(1,100)for i in range(5)]
List2=[]
for i in range(1,len(List1)):
    List2+=[List1[i]]
List2+=[List1[0]]
print(f"List1 = {List1}       List2 = {List2}")
"""

#11
"""
List1 = ['A', 'B', 'C'] 
List2 = [1, 2, 3]
Yeni_list=[]
for i in range(len(List1)):
    Yeni_list+=[[List1[i],List2[i]]]
print(Yeni_list)
"""
#12 . Listin ilk cüt ədədinə rastlayana qədər bütün tək ədədlərin cəmini tapan kod yazın.
"""
List = [5, 7, 5, 9, 2, 6, 4, 3, 2, 5, 6]
sums=0
for i in List:
    if i%2!=0:
        sums+=i
    else:
        break
print("List",end=" = ")
print(List)
print(f"Listin ilk cut ededine qeder olan cem:  {sums}")
"""


#13  N ölçülü listin içərisini [10, 50] intervalında təsadüfi ədədlərlə doldurun. Həmin 
#ədədlərdən müəyyən ədədin kvadratı olan ədədləri başqa listə köçürün və nəticəni çap 
#edin.
"""
from random import *
from math import *
List1 = [randint(10,50) for i in range(15)]
List2=[]
c=0
for i in List1:
    c+=1
    if sqrt(i)%1==0:
        List2+=[i]
print(f" Listin olcusu N:  {c}")
print("List1",end=" = ")
print(List1)
print("List2",end=" = ")
print(List2)
"""


#14 . N ölçülü listin içərisini [100, 999] aralığında təsadüfi ədədlərlə doldurun. Ədədlərin 
#sayı istifadəçi tərəfindən daxil edilir. Listin içərisində son iki rəqəminin modul fərqi və 
#cəmi tək olan ədədləri başqa listə yığın.
"""
from random import *
N=int(input("enter N:"))
List1=[randint(100,999)for i in range(N)]
def checker(List1):
    List2=[]
    for i in List1:
        c=0
        n=0
        c=i%10
        n=i//10%10
        d=abs(c-n)
        q=abs(c+n)
        if d%2!=0 and q%2!=0:\
           List2+=[i]
    return List2

print("Ededlerin sayi N: {N}")   
print("List1",end=" = ")
print(List1)
print("List2",end=" = ")
print(checker(List1))
"""


#15  Massivi [0, 100] intervalı arasında olan təsadüfi ədədlərlə doldurun. Ədədlərin sayı 
#istifadəçi tərəfindən daxil edilir. Həmin massivdən sadə ədədləri seçib digər massivə 
#köçürün. Ədədin sadə ədəd olub-olmadığını təyin edən məntiqi funksiyadan istifadə 
#edin.
"""
from random import *
N=int(input("enter N:"))
A=[randint(0,100) for i in range(N)]
B=[]

def sade(j):
    sad=False
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        sad=True
    return sad

for j in A:
    if sade(j)==True:
        B+=[j]

print(f" Ededlerin sayi N: {N}")
print(f" A = {A}        B = {B}")
"""

#16 Massivi [-10, 10] parçasında dəyişən təsadüfi ədədlərlə doldurun (ədədlərin sayı = 10) 
#və həmin massivdən cüt və mənfi ədədləri seçib digər massivə köçürün.
"""
from random import *
N=int(input("enter N:"))
A = [randint(-10,10) for i in range(N)]
B=[]
for i in A:
    if i<0 and i%2==0:
        B+=[i]
print(f" A = {A}")
print(f" B = {B}")
"""

#17  Mənfi olmayan tam ədədləri massivdən çıxarıb yeni massivə əlavə edin.
"""
List1 = [1, 2, 'aasf', '1', '123', 123]
List2=[]
for i in List1:
    if type(i) is int and i>0:
        List2+=[i]
print(f"List1 = {List1}")
print(f"List2 = {List2}")
"""


#18  . İstifadəçi tərəfindən daxil edilən müsbət tam ədədin bütün uyğun bölənlərini bir listə 
#yığıb çap edən proqram yazın.
"""
a=int(input("Musbet tam eded: "))
List=[]
for i in range(1,a+1):
      if a%i==0:
          List+=[i]
print(f" List = {List}")
"""


#19
"""
from math import *
n=int(input("enter n:"))
N=[int(input(":"))for i in range(n)]
List=[]
for i in N:
    c=0
    z=0
    res=0
    for j in range(1,i+1):
        c+=4*sin(n)+2*n
        z+=log(9*n,3)*(2**n)
        res+=c/z
        print(c,z,res)
    List+=[res]
print(f" N = {N}")
print(f"List = {List}")
"""


#20
"""
from math import *
n=int(input("enter n:"))
N=[int(input(":"))for i in range(n)]
List=[]
res=0
for i in N:
    c=0
    z=0
    for j in range(1,i+1):
        c+=cos((n**2+1)**n)**n
        z+=log(8,3)*((n+n**2)**n)
        res+=c/z
    List+=[res]
print(f" N = {N}")
print(f"List = {List}")
"""    


#21
"""
from random import *
n=int(input("enter n:"))
A=[randint(-100,100)for i in range(n)]
B=[]
ls_p=[]
ls_n=[]
c=0
for z in A:
    if z>0 :
        c+=1
        ls_p+=[z]
    elif z==0:
        ls_p+=[z]
    else:
        ls_n+=[z]
B+=ls_p+ls_n
print(f"A = {A}")
print(f"B = {B}")
print(f"Musbet ededlerin sayi : {c}")
"""


#22
"""
from random import *
f1=0
f2=1
f_sum=0
f_list=[]
while f1<=100:
    f_list+=[f1]
    f_sum=f1+f2
    f1=f2
    f2=f_sum

n=int(input("enter n:"))
List1=[randint(0,100)for i in range(n)]
List2=[]
var=True
for i in List1:
    if i in f_list:
        var=True
        if var:
            List2+=[i]
      
print(f"List1 = {List1}")
print(f"List2 = {List2}")
"""


#23  Listdəki 2-ci minimum və 2-ci maksimum ədədi tapan proqram yazın. (min2????)
"""
from random import *
from math import *
n=int(input("enter the length:"))
a=[randint(10,99)for i in range(n)]
print(a)

def max_min(a):
    maxx=float("-inf") #menfi sonsuzluq
    minn=float("inf")
    for i in range(len(a)):
        if maxx<a[i]:
            maxx=a[i]
            idx1=i #max indeks
        if minn>a[i]:
            minn=a[i]
            idx2=i #min indeks
    return maxx,idx1,minn,idx2
sec=[]
max1=max_min(a)[0] #ilk max cunki sirada max birincidi
min1=max_min(a)[2] #ilk min cunki sirada ikincidi
i1=max_min(a)[1]
i2=max_min(a)[3]
for i in range(len(a)):
    if (a[i]!=max1 ) and (a[i]!=min1) : #indeks ferqli qoysaq tekrarlanan eded qalacaq
        sec+=[a[i]]
print(sec)

max2=max_min(sec)[0] #
min2=max_min(sec)[2] #
i3=max_min(sec)[1]
i4=max_min(sec)[3]
print(f"ilk max {max1}, indeksi {i1},  \
ikinci max {max2}, indeksi {i3}")
print(f"ilk min {min1}, indeksi {i2},  \
ikinci min {min2}, indeksi {i4}")
"""

#24 laviaturadan massivi daxil edin və bir gedişdən istifadə etməklə maksimal qiymətə 
#malik olan elementlərin sayını tapın
"""
from math import *
n=int(input(":"))
c=0
a=[]
maxx=float("-inf")
for i in range(n):
    b=int(input("enter b:"))
    a+=[b]
    if b>maxx:
        maxx=b
        c=1 #ilk defe maximum gorende sayi birdi
    elif b==maxx:
        c+=1
print(a)
print(f"Maksimal giymet {maxx}")
print(f"Elementlerin sayi {c}")
"""



#25  Klaviaturadan massivi daxil edin və bir gedişdən istifadə etməklə maksimal qiymətə 
#malik olan elementlərin sayını tapın.
"""
n=int(input("Umumi element sayi daxil edin:"))
List=[int(input(":"))for i in range(n)]
count=0
def maxi(List):
    maxs=List[0]
    for i in List:
        if i>maxs:
            maxs=i
    return maxs

for z in List:
    if z==maxi(List):
        count+=1
print(*List)
print(f"Maksimal qiymet {maxi(List)}")
print(f"Elemntlerin sayi {count}")
"""


#26
"""
from random import *
n=int(input("enter the number:"))
List1=[randint(100,200)for i in range(n)]

def ekob(a,b):
    ebob=0
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            ebob=i
    ekob=a*b/ebob
    return ekob

ls=[]
for i  in List1:
    s=0
    while i>0:
        b=i%10
        i=i//10
        s+=b**3
    ls+=[s]
print(ls)

List1_EKOB=[]
for x in range(0,len(ls)-1,2):
    List1_EKOB+=[ekob(ls[x],ls[x+1])]
   
print(f"List1={List1}")
print(f"List1_EKOB={List1_EKOB}")
"""




#27. Massivdə cüt sayda element var. Massivi təsadüfi elementlərlə doldurun. Massivin 1
#ci və 2-ci yarısı üçün ayrı-ayrılıqda inversiya əməliyyatını yerinə yetirin
"""
from random import *
n=int(input("Enter n:"))
E = [randint(0,100)for i in range(n)]
p1=[]
p2=[]
n1=int(n/2)
for i in E[0:n1]:
    p1+=[i]

for j in E[n1 :]:
    p2+=[j]
    
P1=[]
P2=[]
P=[]
for a in p1[::-1]:
    P1+=[a]
    
for b in p2[::-1]:
    P2+=[b]
P=P1+P2
print("Massiv :  E")
print(E)
print("Half-inverted")
print(P)
"""

#28
"""
from random import *
article_list = ["the", "a", "one", "some", "any"] 
noun_list = ["boy", "girl", "dog", "town" , "car"] 
verb_list = ["drove", "jumped", "ran", "walked" , "skipped"]  
preposition_list = ["to", "from", "over", "under" , "on"]
def length(x):
    count=-1
    for i in x:
        count+=1
    return count
for i in range(5):
    random_cumle=[]
    random_cumle+=[article_list[randint(0,length(article_list))]]
    random_cumle+=[noun_list [randint(0,length(noun_list ))]]
    random_cumle+=[verb_list [randint(0,length(verb_list ))]]
    random_cumle+=[preposition_list[randint(0,length(preposition_list ))]]
    random_cumle+=[article_list[randint(0,length(article_list ))]]
    random_cumle+=[noun_list [  randint(0,length(noun_list ))]]
    print(*random_cumle)
print()
"""
#29
"""
c=[]
print("0-100 arasinda qiymetlerinizi daxil edin:")
print("fizika imtahanin qiymeti:")
f=int(input())
print("riyazziyat imtahanin qiymeti:")
r=int(input())
print("kimya imtahanin qiymeti:")
k=int(input())
print("ingilis dili imtahanin qiymeti:")
i=int(input())
print("ana dili imtahanin qiymeti:")
a=int(input())
c+=f,r,k,i,a
print(f"cavablariniz: {c}")

A=0
B=0
C=0
D=0
k=0
for i in c:
    if i>90:
        A+=1
    elif i>80:
        B+=1
    elif i>70:
        C+=1
    elif i>60:
        D+=1
    else:
        k+=1
print("sizin qiymetleriniz:")
print(f"{A} eded A,")
print(f"{B} eded B,")
print(f"{C} eded C,")
print(f"{D} eded D,")
print(f"{k} eded kesriniz var ")
"""

#30
"""
List=[]
print("fizika imtahanini kecdiniz mi? he/yox")
a=input()
print("riyazziyat imtahanini kecdiniz mi? he/yox")
b=input()
print("kimya imtahanin imtahanini kecdiniz mi? he/yox")
c=input()
print("ingilis dili imtahanin imtahanini kecdiniz mi? he/yox")
d=input()
print("ana dili imtahanin imtahanini kecdiniz mi? he/yox")
e=input()
List+=a,b,c,d,e
cn=0
v=""
for i in  List:
    if i=="he":
        cn+=1
if cn>=4:
    v+="elaci"
elif cn>=3:
    v+="yaxshi"
elif cn>=2:
    v+="kafi"
else:
    v+="pis"
print(f"cavablariniz:   {List}")
print("Sizin tedris veziyyetiniz beledir:")
print(v)
"""



