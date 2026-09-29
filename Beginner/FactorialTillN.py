
n=int(input("Enter a number n whose factorial you want to find: "))

prod=1
i=n

for i in range(1,n+1,1):
    prod=prod*i
print("The factorial of the given number is: ",prod)