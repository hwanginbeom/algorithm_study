N = int(input())
nums = list(map(int, input().split()))

result = 0
late = 0
if N == 1:
    print(nums[0])
else:
    nums.sort()
    for i in range(N):
            result += (nums[i] + late)
            late += nums[i]
print(result)

