def sum(l,lb,ub):
    if lb==ub:
        return l[lb]
    if lb>ub:
        return -1
    mid=(lb+ub)//2
    return sum(l,lb,mid)+sum(l,mid+1,ub)
l=list(map(int,input().split()))
res=sum(l,0,len(l)-1)
print(res)


