

n=int(input("Enter a number: "))
a=n
b=0
while a!=0:
    x=a%10
    b:int=(b*10)+x
    a=a//10
print (b)

