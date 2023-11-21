nb = int ( input ( " enter a number between 10 and 20 : " ) )
while nb>20 or nb<10:
    
    if nb>20:
         print("BIGGER !")
    else:
         print("SMALLER !")
    nb = int(input("enter a number betwen 10 and 20 : "))
print("GOOD ! NUMBER IS CORRECT")

N = int(input("enter a number N>1 : "))
while N<=1 :
     N = int(input("enter a number N>1 : "))
s=0
i=112

while i<=N: #for i in N: 
     s=s+i
     i=i+1
print(s)