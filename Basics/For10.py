
a={1:"one", 2:"two"}
print(a)

a[1]

a[1]="ONE"
print (a)

a[3]="three"
print(a)

a={1:"ONE",2:"two",3:"three"}
print(1 in a)

print(4 in a )

print(a.items())

print(a.keys())

print(a.values())


print(a)
a.setdefault(3,"three")
print(a)

b={4:"four"}

a.update(b)
print(a)

key=["apple","ball"]
value="for kids"
d=dict.fromkeys(key,value)
print(d)

print(len(a))