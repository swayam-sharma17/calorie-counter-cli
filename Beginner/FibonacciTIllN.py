
n = int(input("Enter n: "))

a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

"""
n = int(input("Enter n: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

"""