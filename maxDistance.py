# Problem
# You are given an array A of length 2N consisting of integers from 1 to N. Each integer appears exactly twice.
# The distance between two indices i, j is |i-j| (that is, the absolute value of the difference between them).
# What is the maximum distance between a pair of distinct indices i, j where A[i] = A[j]?
# Input Format
# The first line contains the integer N.
# The second line contains 2N integers: the array A.
# Output Format
# Output a single integer: the maximum distance between a pair of distinct indices i, j where A[i] = A[j].
# Sample Input
# 5 4214312553
# Sample Output
# 5
# Explanation
# ● The 1s are distance 3 apart
# ● The 2s are distance 5 apart
# ● The 3s are distance 5 apart
# ● The 4s are distance 3 apart
# ● The 5s are distance 1 apart
# Hence the maximum distance between 2 elements of the same value in the given array is 5.
# Bounds
# ● 1<=N<=100000
from typing import List


class Solution:
    @staticmethod
    def maxDistance(array: List[int]) -> int:
        num_map = dict()
        max_distance = 0
        for i in range(0, len(array)):
            if array[i] not in num_map:
                num_map[array[i]] = i
            else:
                num_map[array[i]] = abs(i - num_map[array[i]])
                if max_distance < num_map[array[i]]:
                    max_distance = num_map[array[i]]
        return max_distance


if __name__ == '__main__':
    print(Solution.maxDistance(5, [4, 2, 1, 4, 3, 1, 2, 5, 5, 3]) == 5)
