class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0, len(nums)+1):       
        #     if i not in set(nums):
        #         return i
        n=[i for i in range(len(nums)+1)]
        return sum(n)-sum(nums)