a=[2,4,1,5,3]
n = len(a)

print("The list before arranging is: ",a)
for i in range(0,n,1):
    for j in range(1,n - i - 1,1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        
print("The modified list is: ",a)
