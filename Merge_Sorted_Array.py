#88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = 0
        for num in nums2:
            for i in range(start,len(nums1)):
                if nums1[i] == 0 and i>=m:
                    nums1[i] = num
                    start =i
                    m+=1
                    break
                
                if nums1[i] >= num:
                    nums1.insert(i,num)
                    nums1.pop()
                    start=i+1
                    m+=1
                    break
                
