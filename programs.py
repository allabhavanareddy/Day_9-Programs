a=range(1,10,2)
print(a,type(a))
print(list(a),type(a))

def fun(a):
    return str(a)
l=[1,2,3,4]
l=list(map(fun,l))
print(l)

def fun(a):
    return str(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(fun,l))
print(l)

def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(fun,l))
print(l)


def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(lambda a:max(a),l))
print(l)

def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,8,9]]
l=list(map(lambda a:a.sort(),l))
print(l)

def fun(a):
    return sum(a)
l=[[1,2,3],[4,5,6],[7,9,8]]
l=list(map(lambda a:sorted(a),l))
print(l)

def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
a=[2,3,4,5,6]
l=list(filter(lambda a:a%2==0,a))
print(l)

#sorted acc to sum of individual set
def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
l.sort(key=sum)
print(l)

def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
l.sort(key=lambda x:x[0]+x[1])
print(l)


def fun(a):
    return sum(a)
l=[[1,3,2],[8,6,7],[9,0,0]]
print(max(l,key=lambda x:x[0]+x[1]))
print(l)


