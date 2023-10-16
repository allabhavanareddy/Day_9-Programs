#l=[2,4,8,3,8,1,2,4,7,4]
n=int(input())
l=list(map(int,input().split(",")))  
count=[0 for i in range(len(l))]
for i in range (len(l)):
    count[l[i]]+=1
print(*count )
for i in range(1,len(count)):
    count[i]+=count[i-1]
print(*count,sep=",")
res=[0]*len(l)
for i in range(len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(*res,sep=",")
 