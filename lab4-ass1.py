#implement binary search with user functions
def binarySearch(p,l,r,x):
    if(r>=1):
        mid=1+(r-1)//2
        if p[mid] == x:
            return mid
        elif p[mid] > x:
            return binarySearch(p,1,mid-1,x)
        else:
            return binarySearch(p,mid+1,r,x)
    else:
        return -1
p = [20,40,80,100]
x = (int)(input("Enter the element"))
s = binarySearch(p,0,len(p)-1,x)
if (s!=-1):
    print("Element is present at index % d" % s)
else:
    print("Element is not present in array")
    
