import collections


class Solution:
    def numSplits(self, s: str) -> int:
        # naive, time complexity too high
        if len(s) < 2 or s is None:
            return 0
        if len(s) == 2:
            return 1
        res = 0
        for i in range(1, len(s)):
            if len(set(s[i:])) == len(set(s[:i])):
                res += 1
        return res

    def numSplits2(self, s: str) -> int:
        # https://leetcode.com/problems/number-of-good-ways-to-split-a-string/discuss/754719/Some-hints-to-help-you-solve-this-problem-on-your-own/1002958
        if len(s) < 2 or s is None:
            return 0
        if len(s) == 2:
            return 1
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        pre_set = set()
        suf_set = set()
        for i in range(0, n):
            pre_set.add(s[i])
            suf_set.add(s[n - 1 - i])
            prefix[i] = len(pre_set)
            suffix[n - 1 - i] = len(suf_set)
        res = 0
        for i in range(0, n - 1):
            if prefix[i] == suffix[i + 1]:
                res += 1
        return res

    def numSplits3(self, s: str) -> int:
        # https://leetcode.com/problems/number-of-good-ways-to-split-a-string/discuss/755264/Python-O(N)-Sliding-Window
        res = 0
        left_counter = collections.Counter()
        right_counter = collections.Counter(s)
        for c in s:
            left_counter[c] += 1
            right_counter[c] -= 1
            if right_counter[c] == 0:
                del right_counter[c]
            if len(left_counter) == len(right_counter):
                res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSplits3("aacaba"))
