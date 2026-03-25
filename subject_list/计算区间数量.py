
class Solution:
    def count_intervals(self, records, length_range, threshold):
        n = len(records)
        if n == 0:
            return 0
        min_len, max_len = length_range
        count = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + records[i]
        for length in range(min_len, max_len + 1):
            if length > n:
                continue
            for i in range(n - length + 1):
                total = prefix[i + length] - prefix[i]
                if total >= threshold * length:
                    count += 1
        return count
    
a = Solution()
records = [2, 0, 2, 0, 2]
length_range = [2, 4]
threshold = 1
print(a.count_intervals(records=records, length_range=length_range, threshold=threshold))