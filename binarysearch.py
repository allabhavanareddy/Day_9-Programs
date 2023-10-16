#binary search
def bs(l,lb,ub,search):
    mid=(lb+ub)//2
    if lb>ub:
        return -1
    if l[mid]==search:
        return mid
    if l[mid]<search:
        return bs(l,mid+1,ub,search)
    
    if l[mid]>search:
        return bs(l,lb,mid-1,search)

    
l=list(map(int,input().split()))
search=int(input())
result=bs(l,0,len(l)-1,search)
if result==-1:
    print("Not found")
else:
    print(result)


    
    