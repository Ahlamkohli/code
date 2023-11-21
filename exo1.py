# stop le pgrm dans les number negative 
s= 0 
for i in range(1,9) : #range(8)
    print("enter N",i, " : " ,
           end="")#i+1
    N=int(input())
    if N < 0:
        break
    s= s+N
print("la somme est: ",s)

# ignore les number negative et continue le pgrm

s= 0 
for i in range(1,9) : #range(8)
    print("enter N",i, " : " , end="")#i+1
    N=int(input())
    if N < 0:
        continue
    s= s+N
print("la somme est: ",s)


#import fonctions
#fonctions.fonction1 #fonctions.somme 


#import fonctions
#from fonctions import * (all)



#import fonctions
#from fonctions import fonction1,fonction2... #from fonctions import somme,signe..

#import fonctions as f  f.somme / f.signe....
#from fonctions import somme as s igne as p s(4,5) /p(4,5)....

def multibel(a,b):
    d=a*b
    return d
 
def somme(a,b):
    d= a + b
    return d

def signe (a,b):
    if a*b>0:
        print( a  , "et" , b , "ont la meme signe")
    else:
        print(a  , "et" , b ,"ont pas la meme signe")

def minimum(a,b):
    if a>b: #if global a> global y
        min=b
    else:
        min=a   
    return min 

def maximum(a,b):#argm requis
    if a>b:
        max=a
    else:
        max=b   
    return max   

def soustraction(a=1,b=0):#argm par defaut ms les deux
    c=a-b
    print("a-b=",c)

def sostraction(a,b):#argm par mot cle (a,b)=(b,a)
    c=a-b
    print("a-b=",c)  

a=int(input("enter a :"))
b=int(input("enter b :"))

soustraction()#argm par defaut
sostraction(a=10,b=5)#argm par mot cle


d=multibel(a,b)
print(a, "*", b ,"=",d)

d=somme(a,b)
print(a, " + ", b ,"=",d)

signe(a,b)
print("le minimum entre ",a ,"et", b, "est:",minimum(a,b))
print("le maximum entre ",a ,"et", b, "est:",maximum(a,b))


g="7"
g=g+"0"
f=int(g)+3
print(float(f))