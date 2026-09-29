

n=int(input("Enter the number you want to check: "))
sum=0
i =n

while (i!=0):
    x=i%10
    cube=x*x*x 
    sum=sum+cube 
    i=i//10
if (n==sum):
    print("The given number ", n," is an Armstrong Number")
else:
    print("The given number ", n," is not an Armstrong number")

'''
iimport math

n = int(input("Enter the number you want to check: "))
sum = 0
i = n

while (i != 0):
    x = i % 10
    cube = math.pow(x, 3)   #raise digit to power = 3
    sum = sum + cube
    i = i // 10

sum = int(sum) #convert back to int since math.pow() returns float

if (n == sum):
    print("The given number", n, "is an Armstrong Number")
else:
    print("The given number", n, "is not an Armstrong number")

'''