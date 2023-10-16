a=[1,2,3,4,5]
b=[5,6,7,8,9]
print(zip(a,b))
print(list(zip(a,b)))
print(enumerate(a))
print(list(enumerate(a)))
for i in enumerate(a):
    print(i)
for i,j in enumerate(a):
    print(i)
for i,j in enumerate(a):
    print(i,j)
for i in [range(1,10),range(10,1,-1),range(0,20,2)]:
    print(i)
for i in [range(1,10),range(10,1,-1),range(0,20,2)]:
    print(list(i))