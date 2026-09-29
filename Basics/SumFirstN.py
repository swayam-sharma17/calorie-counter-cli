
# made the program for n numbers so if we need to sum till 10 just put n=10 during the input 

#sum using while loop
n=int(input("Enter a number n: "))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
    
print("Sum of the first 10 digits are: ",sum)


