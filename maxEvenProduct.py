# Problem 3: Maximum Even Product
# Problem
# You are given an array A of length N consisting of positive integers.
# You wish to select 2 integers from this array, call them x and y, such that x*y is even and as large as possible.
# Input Format
# The first line contains the integer N
# The second line contains N integers: the array A
# Output Format
# Output a single integer: the maximum possible even product.
# You are guaranteed that at least one pair of numbers has an even product.
# Sample Input
# 5 96724
# Sample Output
# 54
# Explanation
# In this case, you can select 9*6 = 54. Note tha 9*7 = 63 is larger, but is not even.
# Bounds
# ● 1<=N<=100000
# ● 1<=K<=N
# ● All integers in the array A are between 1 and 1000000.
from typing import List


class Solution:
    @staticmethod
    def maxEvenProduct(array: List[int]) -> int:
        max_num = 0
        for i in range(0, len(array)):
            if array[i] > max_num and array[i] % 2 == 0:
                max_num = array[i]
        array.remove(max_num)
        return max(array) * max_num


if __name__ == '__main__':
    print(Solution.maxEvenProduct([9, 6, 7, 2, 4]) == 54)
