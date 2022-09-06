class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        
        while True:
            m = (l + r) // 2
            b_ptr = half - m - 2
            
            A_left = A[m] if m >=0 else float("-infinity")
            A_right = A[m + 1] if m + 1 < len(A) else float("infinity")
            B_left = B[b_ptr] if b_ptr >= 0 else float("-infinity")
            B_right = B[b_ptr + 1] if b_ptr + 1 < len(B) else float("infinity")
            
            if (A_left <= B_right and B_left <= A_right):
                if total % 2:
                    return min(A_right, B_right)
                else:
                    return ((max(A_left, B_left) + min(A_right, B_right)) / 2)
            elif (A_left > B_right):
                r = m - 1
            else:
                l = m + 1
            