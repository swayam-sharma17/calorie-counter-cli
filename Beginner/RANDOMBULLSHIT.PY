
n=int(input("Enter a number :"))

while n>=0:
    print(n,end='')
    n=n-1
print()
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))    
s=0
while(a<=b):
    s=s+a
    b+=1
print("sum=",s)