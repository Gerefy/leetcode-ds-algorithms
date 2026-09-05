class Solution(object):
    def twoSum(self, nums, target):
        a = nums
        for i in range(0, len(nums) - 1):
            for s in range(i + 1, len(a)):
                if (a[i] + a[s]) == target:
                    return [i, s]
