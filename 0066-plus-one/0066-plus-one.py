class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                temp = carry
                carry = (digits[i] + carry + 1) // 10
                digits[i] = (temp + digits[i] + 1) % 10
            else:
                temp = carry
                carry = (digits[i] + carry) // 10
                digits[i] = (temp + digits[i] ) % 10
        
        if carry:
            digits.insert(0, carry)
        
        return digits
        