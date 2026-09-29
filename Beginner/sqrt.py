"square root of 2 without libraries/funcitons"
a=float(input("Enter a number: "))

n=a/2

for i in range(10):
    n=(n+a/n)/2
print(f"square root of {a} is {n}")