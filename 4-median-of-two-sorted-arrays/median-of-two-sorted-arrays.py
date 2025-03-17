from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 

        # Ensure A is the smaller array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1 

        while True:
            i = (l + r) // 2  # A's partition index
            j = half - i - 2   # B's partition index

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # Check if we found the correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total length
                if total % 2 == 1:
                    return min(Aright, Bright)

                # Even total length
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Adjust binary search range
            elif Aleft > Bright:
                r = i - 1  # Move left
            else:
                l = i + 1  # Move right
