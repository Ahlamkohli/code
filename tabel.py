A=int(input("enter a number: "))
while A<1 or A>10:
    A=int(input("enter a number: 2"))
i=0
while i<=10:
    m=A*i
    print(A, "*" ,i, "=" ,m)
    i=i+1