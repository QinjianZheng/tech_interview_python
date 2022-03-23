# Problem
# You have a fence with N posts of varying heights. The height of the i-th post is H[i].
# You want to create an obstacle course for your pet frogs!
# In particular, you will select three fence posts to create the obstacle course,
# where the middle post is strictly higher than the other two.
# The frogs will jump up from the left post to the middle post, then jump down from the middle post to the right post.
# The three posts do not have to be next to each other as frogs can jump over other fence posts,
# regardless of the height of those other posts. The order of the fence posts cannot be changed.
# The difficulty of an obstacle course is the height of the first jump plus the height of the second jump.
# The height of a jump is equal to the difference in height between its two fence posts.
# What is the most difficult obstacle course you can make, given an array of fence heights?
# Input Format
# The first line contains the integer N - the number of posts.
# The second line contains N integers: the array H - the heights of the N posts.
# Output Format
# Output a single integer: the difficulty of the most difficult obstacle course possible.
# You are guaranteed that at least one valid obstacle course exists.
# Sample Input
# 8/ 6 7 3 5 4 6 2 1
# Sample Output
# 8
# Explanation
# 6 7 3 5 4 6 2 1
# The best course uses the 3rd, 6th and 8th posts (shown in bold), for a difficulty of (6-3) + (6-1) = 8.
# Bounds
# 3 <= N <= 100000
# All heights are between 1 and 100000.
from typing import List


class Solution:
    @staticmethod
    def mostDifficultObstacle(posts: List[int]) -> int:
        smallestToLeft = [1e9]
        smallestToRight = [1e9]
        for i in range(1, len(posts)):
            if posts[i - 1] < smallestToLeft[i - 1]:
                smallestToLeft.append(posts[i - 1])
            else:
                smallestToLeft.append(smallestToLeft[i - 1])
        print(smallestToLeft)
        for i in range(len(posts)-1, 1):
            if posts[i+1] < smallestToRight[i+1]:
                smallestToRight.insert(0, )

if __name__ == '__main__':
    Solution.mostDifficultObstacle([6, 7, 3, 5, 4, 6, 2, 1])
