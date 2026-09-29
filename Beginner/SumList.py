a=[10,20,30,40,50]
sum1=0
sum2=0

for i in range(0,len(a),1):
    sum1=sum1+a[i]

print("The sum of the elements using for is: ",sum1)

j=0
while(j!=len(a)):
    sum2=sum2+a[j]
    j=j+1

print("The sum of the elements using while is: ",sum2)
