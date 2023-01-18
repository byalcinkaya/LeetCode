class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        x = strs[0]
        y = strs[1]
        z = strs[2]
        for i in range(len(x)):
            for i in range(len(y)):
                for i in range(len(z)):
                    while (x[i] == y[i] and y[i] == z[i]) :
                        result+= x[i]
                        i+=1
                    return(result)
