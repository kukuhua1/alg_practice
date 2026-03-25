def shortest_list(nums, k):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    for length in range(1, len(nums) + 1):
        for i in range(len(nums) - length + 1):
            if prefix[i + length] - prefix[i] >= k:
                return nums[i : i + length]
    return None
        

a = [2, 3, 5, 1, 3, 3, 4, 5, 2, 1, 6, 7]
k = 10
print(shortest_list(nums=a, k=k))


def minSubArrayLen(k, nums):
    n = len(nums)
    preSum = [0] * (n + 1)
    # 1. 先构建前缀和
    for i in range(n):
        preSum[i+1] = preSum[i] + nums[i]
    
    left = 0
    res = float('inf')
    
    # 2. 滑动窗口遍历右端点
    for right in range(1, n+1):
        # 满足条件：缩小左边界，求最短
        while preSum[right] - preSum[left] >= k:
            res = min(res, right - left)
            left += 1
    return res if res != float('inf') else 0
print(minSubArrayLen(k, a))