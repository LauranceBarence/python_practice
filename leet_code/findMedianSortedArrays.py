import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            return (nums1[int(len(nums1) / 2 - 1)] + nums1[int(len(nums1) / 2)]) / 2
        else:
            print(len(nums1) / 2)
            return nums1[math.ceil(len(nums1) / 2) - 1]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [6]
    nums2 = [1, 2, 3, 4, 5]
    result = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(result)
