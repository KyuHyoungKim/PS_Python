nums = list(map(int,input().split()))
res = 0
for i in range(len(nums)):
    res += nums[i]*nums[i]
print(res%10)
