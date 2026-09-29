
#input from user

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

#checking which among the 3 numbers is greatest

if num1>=num2 and num1>=num3:
        greatest=num1
elif num2>=num1 and num2>num3:
        greatest=num2
else:
        greatest=num3

        #printing final result

print("The grestest number among the given is", greatest)