class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = []
        res = 0
        for i in tokens:
            if (i == "+"):
                nums.append(nums.pop() + nums.pop())
            elif (i == "-"):
                nums.append( -(nums.pop() - nums.pop()))
            elif (i == "*"):
                nums.append(nums.pop() * nums.pop())
            elif (i == "/"):
                temp = int(nums[-2] / nums.pop())
                nums.pop()
                nums.append(temp)
            else:
                nums.append(int(i))
        return nums[0]
                
        