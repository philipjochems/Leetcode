#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        combined = []
        length=0
        while True:
            if i>=len(nums1) and j>=len(nums2):
                break
            if i>=len(nums1):
                combined.append(nums2[j])
                j+=1
                length+=1
                continue
            if j>=len(nums2):
                combined.append(nums1[i])
                i+=1
                length+=1
                continue

            if nums1[i]<nums2[j]:
                combined.append(nums1[i])
                length+=1
                i+=1
            else:
                combined.append(nums2[j])
                length+=1
                j+=1
        if length %2 != 0:
            return combined[length//2]
        else:
            return (combined[length//2] +combined[length//2-1])/2
