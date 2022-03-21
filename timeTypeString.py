from time import time


class Solution:
    @staticmethod
    def timeTypeString(keyboard: str, text: str) -> int:
        start = time()
        current_index = 0
        total_time = 0
        for char in text:
            next_index = keyboard.find(char)
            total_time += abs(current_index - next_index)
            current_index = next_index
        end = time()
        print("time taken", (end - start) * 1000, "ms")
        return total_time

    @staticmethod
    def timeTypeString2(keyboard: str, text: str) -> int:
        start = time()
        current_index = 0
        total_time = 0
        keyboard_map = {c: i for i, c in enumerate(keyboard)}
        for char in text:
            next_index = keyboard_map[char]
            total_time += abs(current_index - next_index)
            current_index = next_index
        end = time()
        print("time taken", (end - start) * 1000, "ms")
        return total_time


if __name__ == '__main__':
    print(Solution.timeTypeString("abcdefghijklmnopqrstuvwxyz", "cba") == 4)
    print(Solution.timeTypeString2("abcdefghijklmnopqrstuvwxyz", "cba") == 4)