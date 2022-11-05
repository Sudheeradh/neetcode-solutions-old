class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = (bit << (31 - i)) | res
        return res
            