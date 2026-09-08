1
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

2
class Solution(object):
    def rotate(self, nums, k):
        c=len(nums)
        k=k%c
        def rev(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        rev(0,c-1)
        rev(0,k-1)
        rev(k,c-1)


3
class Solution(object):
    def rotate(self, nums, k):
        c=len(nums)
        k=k%c
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
