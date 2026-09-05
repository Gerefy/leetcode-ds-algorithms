class Solution(object):
    def diagonalSum(self, mat):
        x=len(mat)
        c0=0
        d1=[]
        d2=[]
        for i in range(x):
            d1.append(mat[i][i])
            d2.append(mat[i][x - 1 - i])
        if x%2==0:
            return(sum(d1)+sum(d2))
        else:
            f=(x//2)
            return(sum(d1) + sum(d2) - mat[f][f])
