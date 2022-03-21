from functools import reduce
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        all_nums = dict()
        tops_nums = dict()
        bottoms_nums = dict()
        for i in range(0, len(tops)):
            if tops[i] not in tops_nums:
                tops_nums[tops[i]] = 1
            else:
                tops_nums[tops[i]] += 1
            if bottoms[i] not in bottoms_nums:
                bottoms_nums[bottoms[i]] = 1
            else:
                bottoms_nums[bottoms[i]] += 1
            if tops[i] not in all_nums:
                all_nums[tops[i]] = 1
            else:
                all_nums[tops[i]] += 1
            if bottoms[i] not in all_nums:
                all_nums[bottoms[i]] = 1
            elif tops[i] != bottoms[i]:
                all_nums[bottoms[i]] += 1
        print(tops_nums)
        print(bottoms_nums)
        print(all_nums)
        if max(all_nums.values()) < len(tops):
            return -1
        candidate = 0
        for k, v in all_nums.items():
            if v == len(tops):
                candidate = k
                break
        return len(tops) - max(tops_nums[candidate], bottoms_nums[candidate])

    def minDominoRotations2(self, tops: List[int], bottoms: List[int]) -> int:
        all_nums = dict()
        for i in range(0, len(tops)):
            if tops[i] not in all_nums:
                all_nums[tops[i]] = 1
            else:
                all_nums[tops[i]] += 1
            if bottoms[i] not in all_nums:
                all_nums[bottoms[i]] = 1
            elif tops[i] != bottoms[i]:
                all_nums[bottoms[i]] += 1
        print(all_nums)
        if max(all_nums.values()) < len(tops):
            return -1
        candidate = 0
        for k, v in all_nums.items():
            if v == len(tops):
                candidate = k
                break
        return len(tops) - max(tops.count(candidate), bottoms.count(candidate))

    def minDominoRotations3(self, tops: List[int], bottoms: List[int]) -> int:
        interception_set = reduce(set.__and__, (set(d) for d in zip(tops, bottoms)))
        print(interception_set)
        if not interception_set:
            return -1
        candidate = interception_set.pop()
        return min(len(tops) - tops.count(candidate), len(tops) - bottoms.count(candidate))

    def minDominoRotations4(self, tops: List[int], bottoms: List[int]) -> int:
        interception_set = {tops[0], bottoms[0]}
        for i in range(1, len(tops)):
            interception_set &= {tops[i], bottoms[i]}
        if not interception_set:
            return -1
        candidate = interception_set.pop()
        return min(len(tops) - tops.count(candidate), len(tops) - bottoms.count(candidate))


if __name__ == '__main__':
    s = Solution()
    print(s.minDominoRotations4([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]) == 2)
    print(s.minDominoRotations4([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]) == -1)
    print(s.minDominoRotations4([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]) == 0)
