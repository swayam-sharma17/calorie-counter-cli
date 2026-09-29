A=[10,20,30,40,50,60,70,80,90,100]
print(A[2:6])
print(A[:5])
print(A[5:])
print(A[-4:])
print(A[:-4])
print(A[::2])
print(A[1::2])
print(A[::-1])
print(A[7:2:-1])
print(A[8:1:-2])    
print(A[1])
print(A)
A.insert(1,15)
print(A)
copy=A[:]
print(copy)
print(A[:1:-1])
fruits=["apple","banana"]
print(fruits)

numbers = [10, 20, 30, 40]
numbers[1:4] = [200]
print(numbers)
numbers = [10, 20, 30, 40, 50]
numbers[1:4] = []
print(numbers)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[::2])