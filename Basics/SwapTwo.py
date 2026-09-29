#swapping by using a temporary variable 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
temp=a
a=b
b=temp
print("The first swapped number is: ",a)
print("The second swapped number is: ",b)