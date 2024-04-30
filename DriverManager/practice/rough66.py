nums= [5,7,7,8,8,8,0]
target=8
i=0
j=len(nums)-1

while i<=j:
    mid=(i+j)//2
    if nums[mid]==target:
        if mid==0 or nums[mid-1]!=target:
            print(mid)
            break
        j=mid-1
    elif nums[mid]>target:
        j=mid-1
    else:
        i=mid+1
i=0
j=len(nums)-1
while i<=j:
    mid=(i+j)//2
    if nums[mid]==target:
        if mid==len(nums)-1 or nums[mid+1]!=target:
            print(mid)
            break
        i=mid+1
    elif nums[mid]>target:
        j=mid-1
    else:
        i=mid+1


