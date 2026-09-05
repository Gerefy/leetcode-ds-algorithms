class Solution(object):
    def transpose(self, matrix):
        C=len(matrix)#строки
        R=len(matrix[0])#столбики
        c0=0#строки
        otv=[]
        while c0!=R:
            res=[]
            c1=0#столбики
            while c1!=C:
                res.append(matrix[c1][c0])
                c1+=1
            otv.append(res)
            c0+=1
        return(otv)
