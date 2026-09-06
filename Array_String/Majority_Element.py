#1
class Solution(object):
    def majorityElement(self, nums):
        c={}
        for i in nums:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1
            if c[i]> len(nums)//2:
                return(i)
#2
class Solution(object):
    def majorityElement(self, nums)
        return sorted(nums)[len(nums) // 2]
