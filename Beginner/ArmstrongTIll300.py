for i in range (1,301,1):
    sum =0
    d=i
    while (d!=0):
        x=d%10
        cube=x*x*x 
        sum=sum+cube 
        d=d//10

    if (i==sum):
         print("The given number ", i," is an Armstrong Number")
    
