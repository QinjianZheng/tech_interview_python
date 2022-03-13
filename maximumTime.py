class Solution:
    def maximumTime(self, time: str) -> str:
        # time format hh:mm
        hh, mm = time.split(':')

        if hh[0] == '?' and hh[1] != '?':
            maximum_hh = '2' + hh[1] if int(hh[1]) < 4 else '1' + hh[1]
        elif hh[0] != '?' and hh[1] == '?':
            maximum_hh = hh[0] + '9' if int(hh[0]) < 2 else hh[0] + '3'
        elif hh[0] != '?' and hh[1] != '?':
            maximum_hh = hh
        else:
            maximum_hh = '23'

        maximum_mm = ('5' if mm[0] == '?' else mm[0]) + ('9' if mm[1] == '?' else mm[1])
        # if mm[0] == '?' and mm[1] != '?':
        #     maximum_mm = '5' + mm[1]
        # elif mm[0] != '?' and mm[1] == '?':
        #     maximum_mm = mm[0] + '9'
        # elif mm[0] != '?' and mm[1] != '?':
        #     maximum_mm = mm
        # else:
        #     maximum_mm = '59'

        return maximum_hh + ':' + maximum_mm


if __name__ == '__main__':
    s = Solution()
    examples = ["?4:5?", "23:5?", "2?:22", "??:??"]
    for e in examples:
        print(s.maximumTime(e))
