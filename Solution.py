class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i,j,k,l,value = 0,0,0,0,0
        hello = []
        temp = []
        while i < numRows:
            while j <= i:
                if(j == 0 or j == i):
                    temp.append(1)
                else:
                    k = i-1
                    value = hello[k][j-1]+hello[k][j]
                    temp.append(value)
                j = j + 1
            i = i + 1
            j = 0
            hello.append(temp)
            temp = []
        return hello
