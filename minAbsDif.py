# https://leetcode.com/discuss/interview-question/356433/Google-or-OA-2018-or-Min-Abs-Difference-of-Server-Loads
from typing import List


class Solution:
    def min_abs_dif(self, loads: List[int]) -> int:
        num = len(loads)
        capacity = sum(loads) // 2
        results = [None] * (capacity + 1)

        def KS(n, c):
            if results[c] is not None:
                return results[c]
            if n < 0 or c == 0:
                result = 0
            elif loads[n - 1] > c:
                result = KS(n - 1, c)
            else:
                temp1 = KS(n - 1, c)
                temp2 = loads[n - 1] + KS(n - 1, c - loads[n - 1])
                result = max(temp1, temp2)
            results[c] = result
            return result

        first_server_loads = KS(num, capacity)
        print(results)
        second_server_loads = sum(loads) - first_server_loads
        return abs(first_server_loads - second_server_loads)

    def min_abs_dif2(self, loads: List[int]) -> int:
        # something is wrong with this solution
        num = len(loads)
        capacity = sum(loads) // 2
        results = [[0] * (capacity + 1)] * (num + 1)
        first_server_loads_content = set()
        for i in range(1, num + 1):
            for j in range(1, capacity + 1):
                if loads[i - 1] <= j:
                    temp1 = results[i - 1][j]
                    temp2 = loads[i - 1] + results[i - 1][j - loads[i - 1]]
                    if temp1 > temp2:
                        results[i][j] = temp1
                    else:
                        results[i][j] = temp2
                else:
                    results[i][j] = results[i - 1][j]
        print(results)
        print(first_server_loads_content)
        first_server_loads = results[-1][-1]
        second_server_loads = sum(loads) - first_server_loads
        return abs(first_server_loads - second_server_loads)


if __name__ == '__main__':
    s = Solution()
    print(s.min_abs_dif2([1, 2, 3, 4, 5]))
    print(s.min_abs_dif([1, 2, 3, 4, 5]))
    print(s.min_abs_dif([3, 9, 7, 3]))
    print(s.min_abs_dif2([3, 9, 7, 3]))
    print(s.min_abs_dif([31, 26, 33, 21, 40]))
    print(s.min_abs_dif2([31, 26, 33, 21, 40]))
