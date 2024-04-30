nums = [ 3,1,9,8,0,4,7,2]


nums.sort()
res=-90000
if nums[0]==0:
    for i in range(1,len(nums)):
        j=nums[i]-1
        while j>nums[i-1]:
            if j in nums:
                j-=1
            else:
                res=j
                if res-nums[i-1]==1:
                    break
        if res !=-90000:
            break

else:
    res=nums[0]-1

if res != -90000:
    print(res)
else:
    print(" no such number")








