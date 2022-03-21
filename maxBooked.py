import collections
from typing import List


class Solution:
    def maxBooked(self, bookings: List[str]) -> str:
        res = collections.Counter(bookings)
        print(res)
        return list(res)[0][1:]

    def maxBooked2(self, bookings: List[str]) -> str:
        hotel_book = dict()
        max_room = bookings[0][1:]
        for room in bookings:
            if room[0] == '-':
                continue
            room_num = room[1:]
            if room_num not in hotel_book:
                hotel_book[room_num] = 1
            else:
                hotel_book[room_num] += 1
            if (hotel_book[max_room] == hotel_book[room_num] and room_num < max_room) or hotel_book[max_room] < hotel_book[room_num]:
                # update max or lexico smaller
                max_room = room_num
        print(hotel_book)
        return max_room


if __name__ == '__main__':
    s = Solution()
    a = ["+4Z", "+3A", "-4Z", "+4F", "+4Z", "-3A", "+3A"]
    print(s.maxBooked2(a))
