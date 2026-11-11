class Solution(object):
    def canJump(self, nums):
        m=0
        for i, jump in enumerate(nums):
            if i>m:
                return False
            m=max(m, i+jump)
            if m>= len(nums)-1:
                return True
        return True
#открыл для себя "enumerate()", она позволяет одновременно получать и индекс элемента, и сам элемент во время цикла
# m- самая дальняя точка, до которой можем дотянуться
# 35ms 12.76MB
