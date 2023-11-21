
#number = 20
#day = 12.6
#first_name = "ahlam"
#is_onlin = False
#print(number)
#print(day)
#print(first_name)
#print(is_onlin)
#name = input("what is your name? ")
#print("hello " + name)
#birth_year = input("enter your birth year : ")
#age = 2023 - int(birth_year)
#print("your age is ", age)
#n1 = input("first :") #float( input("first :"))
#n2 = input("second :")#float( input("second :"))
#sum = float(n1) + float(n2) # sum = float(first) + float(second) sum = first + second
#print("sum: " + str(sum))
#course = "everything gonna be alright"
#print(course.upper()) #majuscule
#print(course.find('a'))
#print(course.replace('be','bi'))
#print('python' in course) # find 'python' in course and return true or false
# / , // عدد القسمة, % mod , ** ^
# x =  12 , x= x+2 == x += 2 
# logical operators (and or not )
#temperature = float(input("what is the temperature ? "))
#if temperature > 50:
   # print("it's a hot day")
#elif temperature < 10:
   # print("it's a cool day")
#else:
   # print("it's a normal day ")

#for i in range(10): for i in 10 or number [range start with 0] 
  #  print(i)
#k=0
#while k<= 100:
   # print(k * '*')
   # k=k+1
#names =["ahlam","abdou","iman","zaki"]
#print(names[2]) (-1 is zaki....)
#print(names[0:3])
#number=[1,2,3,4,5]
#number.append(6) add in the end
#number.insert(0 ,-1) add in the start
#number.remove(3)
#number.clear () clear all the list
#print(len(number)) number of list
#numbers=range(5,10,2) 2 is the step
#for number in numbers: for number in range(1,10,2)
 #   print(number)

#les liste:
#names=['ahlam','iman','zaki','abdou'] 
#l= [ 12,45, 'pomme', True, 3+8, 6 ]
#print(names,l)

#date=list((12,98,'home',False))
#print(date)

#for i in range(16):
   # m=[i]
   # print(m)

#j=list(range(5,16))
#print(j)




lettre=['h','a','m','l']
print(lettre[1],lettre[0],lettre[-1],lettre[1],lettre[-2],sep='')

u=int(input('enter number : '))
while u <1 :
    u=int(input('enter number : '))

l1=list(range(1,u+1))
print(l1)
l2=list(range(0,u+1,2))
l3=list(range(1,u+1,2))
print(l2)
print(l3)

p=list(range(16))
print(p)
print(p[6:16],p[0:5])#slicing p[6:]
print(p[::-1])

#concatenation
 #l=l1+l2
#repetition
 #l=l*n
#comparaison
 #x=l1>l2  == != <= >= < > 

 #nomliste.append(n) add in the end
 #nomliste.insert(index,n)index avant 
 # nomliste.extend(liste2) in the end
 #nomliste.remove(element) remove element from list
 #nomliste.pop(index) remove last item of a list
 #nomliste.clear() delete all items
 #del nomliste[:] delete all items
 #len(nomliste) taille de liste
 #sum(nomliste)
l=list(range(2,101,2))
print (max(l),min(l),sum(l),len(l))
w=list(['ahlam','abdou'])
print(max(w))
e=list('python')
print(min(e))
#nomlista.count(element)
o=[5,6,7,8,5,4,3,2,1,5]
print(o.count(5))
#nomliste.reverse()

y=o.reverse()
print(y)
#nomliste.sort() sort alphabetically
l.sort()#croissant
print(l) 
l.sort(reverse=True)#decroissant
print(l)
#l.sort(key=str.upper) tous les alphabe sont majs
#l.sort(key=str.lower) tous les alphabe sont mins
#l.sort(reverse=True, key=len) longueur mot
f=['Python','c++','Java','PHP','C#']
print(f)
g = sorted(f , reverse=False ,key=str.lower)   ##ordonne par ordre croissant et mins
h = sorted(f , reverse= True ,key=str.lower)    ###ordonne par ordre decroissant et mins
f.sort(reverse=True, key=len)
print(g)
print(h)
print(f)
#l.index('element',start,end) find element pas ca index
w=[1,2,3,4]
w1=w.copy()#w1 another liste by w
w.append(6)
print("w: ", w,"  w1: ",w1 )

#exo3
p=['Maroc','Algerie','Tunisie','Mali','France']
print(p)
pay1=input('choisir pay1 de ces 5 pays: '  )
pay2=input('choisir pay2 de ces 5 pays: ')
i=p.index(pay1)
j=p.index(pay2)
print(p)
p[i],p[j]=p[j],p[i]
print(p)

#exo4
l1=[10,12,14.5,6,2.5]
l2=[8,6.5,12,14.5,10.5]
l3=[9.5,14,12,15,13.5]
l4=[19,20,10,19,18]
s=sum(l1+l2+l3+l4)
print('la sommes des notes est : ',format(s,'.2f'))
m=s/len(l1+l2+l3+l4)
print('la moyenne des notes est : ',format(m,'.2f'))
mx=max(l1+l2+l3+l4)
mn=min(l1+l2+l3+l4)
print('la note maximale est : ',format(mx,'.2f'))
print('la note minimale est : ',format(mn,'.2f'))


#exo5
l=list(input('enter un mot: '))
p=l.copy()
l.reverse()
print(l)
print(p)#les deux listes sont differentes

if l==p:
    print ('le mot est palindrome')
else:
    print ("le mot n'est pas palindrome")


#x=element in nomliste (true false)
#x=element not in nomliste
#for element in nomliste:
#     print(note)
info=['anas','mari','mimi','moha']
for val in info:
    print(val) # wahd bwahed 
for i in range(len(info)):
    print('info[',i+1,']',info[i]) 
#for index,element in enumerate (nomliste,start=n)
#    print("index=",index,"element=",element)
for i ,v in enumerate(info,1):
    print('info[',i,']',v)

#for element,element,... in zip (nomliste1,nomliste2,....)
l=['C#','c++','Java','PHP','Python']
d=[2000,1980,1995,1994,1991]
c=['mf','bs','sm','rl','gr']
for e,a,b in zip(l,d,c):
    print(e,' est cree en',d,'par',b)

#exo6
notes=[]
for i in range(318):
   print("donner la note de l'etudiant num ",i+1," : " , end="")
   # n=float(input())
   notes.append(float(input()))
for i,v in enumerate(notes,1):
    print('la note de etudiant numero',i ,'=', v )

#exo7
x=int(input('enter un nomber : '))
l=[]
for i in range(5):
    print("l[",i+1,"]=",end="")
    l.append(int(input()))
if x in l:
    print(x,'le nombre trouve dans l')
else:
    print(x,'le nombre ne trouve pas dans l')

#exo8
noms=[]
notes1=[]
notes2=[]
for j in range(5):
    print(" étudiant num :",i+1)
    noms.append(input('nom'))
    notes1.append(float(input('note 1 : ')))
    notes2.append(float(input('note 2 : ')))

for nom,n2,n1 in zip(noms,notes2,notes1):
    print (nom,'a eu',(n1+n2)/2) 

#liste imbriquee
#l1 = [["A","B"], ["C",6,7,8],"D","ahlam"]
#matric
mat=[]
for i in range(5):
    ligne=[]
    for j in range(8):
        ligne.append(i)
    mat.append(ligne)
#l=[]
#for ligne in l:
#    for element in ligne:
#         print(element ,end='\t')
#    print()
#for i in range(len(l)):
#    for j in range(len(l[i])):
#         print(l[i][j],end='\t')
#    print()

l1 = [["A","B"], ["C",6,7,8],"D","ahlam"]
l1.append('alger')
l1[1].append('svt')
l1[1].reverse()
#exo
n=[]
for i in range(4):
    ligne=[]
    for j in range(5):
        ligne.append(float(input()))
    n.append(ligne)
s=0
for ligne in n:
    s=s+sum(ligne)
m=s/(len(n)*len(n[0]))
print ('somme :', s )
print ('moyenne :', m )

#exo
t=int(input("veuilez saisir la duree en seconde : "))
h=( t //3600)%24 #heures
mn =(t%3600)//60 #minutes
sec =((t %3600)%60)#secondes
print ("le temps est de ", h," heures,", mn ," minutes et " , sec ,' secondes.')

# Demander à l'utilisateur le nombre de photocopies effectuées
nombre_de_photocopies = int(input("Combien de photocopies avez-vous effectuées ? "))

# Calculer le prix des photocopies
prix_des_photocopies = 0
if nombre_de_photocopies <= 10:
    prix_des_photocopies = nombre_de_photocopies * 0.30
elif nombre_de_photocopies <= 30:
    prix_des_photocopies = 10 * 0.30 + (nombre_de_photocopies - 10) * 0.25
else:
    prix_des_photocopies = 10 * 0.30 + 20 * 0.25 + (nombre_de_photocopies - 30) * 0.20

# Afficher la facture
print("Votre facture est de {} DH.".format(prix_des_photocopies))

#exo 
n=int(input("veuillez saisir la valeur de n : "))
while n<=0:
    print("veuillez reessayer !")
    n=int(input("veuillez saisir la valeur de n : "))

print("les diviseurs de ", n , "sont : ")
for i in range(1,n+1):
    if not(n%i==0 ):
        print(i , end=" ")

#exo
age= int(input("veuillez saisir votre age  : "))
s=0
for i in range(1,age+1):
    s=s+(500+(i*3))
print("votre compte  au " ,age,"ieme annivesaire est : " ,s)


#dectionnary={"key":"value"}
dico={ 'nom':'ahlam',"age":15,"ville":"kouba"}
print('nom du joueur : ', dico['nom'])
print('age du joueur : ', dico["age"])
print('ville du joueur : ', dico ["ville"] )
dico["pays"]="algier"
if "nom" in dico:
    print(exist)
else:
    print("n'est exist pas dans ce dictionnaire.")


#fichier:
#f=open("name of fie","mode")
#fichier= open("test.txt", mode='w') #ouverture en ecriture
#print(f.read())
#f.write("welcom.....")
#f.close()

#exo 
import translator
from translate import translate 
lan=translator(from_lang="franch",to_lang="english")
res=lan.translate("bounjour")
print(res)
#translate.translator("hello world", "francais")
#lan.translation("سلام عالمي")
#res=lan.translate(input())

#exo
from gtts import gTTs 
txt="welcom ahlam in my channel"
langue="en"
res=gTTs(text=txt,lang=langue)
res.save("audio.mp3")

from gtts import gTTs
import os
txt = "welcome ahlam in my channel"
lang = "en"
speech = gTTs(text=txt, lang=lang, slow=False)
speech.save("audio.mp3")
os.system("start audio.mp3")





