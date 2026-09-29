
a=float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("Enter c: "))

# assuming the eqaution is in the for ax**2+b*x+c=0
d=(b**2)-(4*a*c)

if(d>0):
    root1= (-b+d**0.5)/(2*a)
    root2= (-b+d**0.5)/(2*a)
    print("The roots of the given equaiton are: ",root1, root2)

elif(d==0):
    root1=-b/(2*a)
    print("The root of the given equaiton is  : ",root1)

else:
        real=-b/(2*a)
        img=(-d)**0.5/(2*a)
        print(f"The roots of the given equaiton are: {real}+{img}i and {real}-{img}i")

