def maxSum(nums, k):
    # 先算第一个窗口和
    cur = sum(nums[:k])
    res = cur
    
    # 滑动：右边进一个，左边出一个
    for i in range(k, len(nums)):
        cur += nums[i] - nums[i-k]
        res = max(res, cur)
    return res


a = [2, 3, 5, 1, 3, 3, 4, 5, 2, 1, 6, 7]
k = 2
print(maxSum(a, k))