
# made the program for n numbers so if we need to sum till 10 just put n=10 during the input 


#sum using for loop 

n=int(input("Enter a number n: "))
sum=0
i=1

for i in range (1,n+1,1):
    sum=sum+i 

print("the sum of th efrist n numbers is: " , sum)
