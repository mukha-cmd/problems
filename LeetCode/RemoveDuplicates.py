class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        k = 0
        unique_elems = 0
        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                unique_elems += 1
                nums[k] = nums[i]
                k += 1
        if (unique_elems == 0 and len(nums) != 0):
            nums = nums[0]
            return unique_elems + 1
        nums = nums[:k]
        #print(unique_elems)
        #print(nums)
        return len(nums)
        #print(k)
        #print(nums)
print(Solution().removeDuplicates([1, 1, 1, 1]))
