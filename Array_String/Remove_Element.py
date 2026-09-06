class Solution(object):
    def removeElement(self, nums, val):
        k=0
        nums[:]=[x for x in nums if x!=val]
        k=len(nums)
        return(k)
