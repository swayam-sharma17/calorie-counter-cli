
#i is used for changing rows
#j is used for spacing
#k is used for printing stars

n=int(input("Enter how long the pattern should be: "))
for i in range(1,n+1):

    for j in range(1,n+1-i):

        print("",end="")

    for k in range(1,2*i):
        print("*",end="")

    print() #changing the lines 
