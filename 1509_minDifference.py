from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 5:
            return 0
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))


A = [5, 3, 2, 4]
B = [1, 5, 0, 10, 14]
s = Solution()
print(s.minDifference(A))
print(s.minDifference(B))
