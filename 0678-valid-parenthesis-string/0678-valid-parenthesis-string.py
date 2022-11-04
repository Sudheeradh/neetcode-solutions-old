class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for i in s:
            if i == "(":
                left_min += 1
                left_max += 1
            elif i == "*":
                left_min = max(0, left_min - 1)
                left_max += 1
            else:
                left_max -= 1
                left_min = max(0, left_min - 1)
                if left_max < 0:
                    return False
        return left_min == 0
            