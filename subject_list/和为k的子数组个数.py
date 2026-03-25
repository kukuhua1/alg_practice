def subarraySum(nums, k):
    from collections import defaultdict
    preSum = 0
    cnt = defaultdict(int)
    cnt[0] = 1  # 关键：前缀和0初始出现1次
    res = 0
    
    for num in nums:
        preSum += num
        # 找前面有多少个 preSum - k
        res += cnt.get(preSum - k, 0)
        cnt[preSum] += 1
    return res

a = [-1, 9, 6, 4, -6, 3, -7, 5, 7, 8]
k = 1
print(subarraySum(a, k))