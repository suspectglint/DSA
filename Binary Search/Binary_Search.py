a=[[1,'simba'],[2,'samba'],[4,'thumba'],[5,'lamba'],[11,'pamba']]

def binarySearch(a,key):
    low=0
    high=len(a)-1
    mid=(low+high)//2
    while low<=high:
        print(low,mid,high,a[low][0],a[mid][0],a[high][0])
        if key==a[mid][0]:
            return a[mid][1]
        elif key>a[mid][0]:
            low=mid+1
            mid=(low+high)//2
        else:
            high=mid-1
            mid=(low+high)//2
    print(low,high,mid)
    return ""

while True:
    key=int(input("Enter a number :"))
    print(binarySearch(a,key))