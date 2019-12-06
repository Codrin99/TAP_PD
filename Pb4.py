def Count(str, n):
    matrix = [[0 for x in range(n)] for y in range(n)]

    P = [[False for x in range(n)] for y in range(n)]
    for i in range(n):
        P[i][i] = True

    for i in range(n - 1):
        if (str[i] == str[i + 1]):
            P[i][i + 1] = True
            matrix[i][i + 1] = 1

    for gap in range(2, n):
        for i in range(n - gap):
            j = gap + i;
            if (str[i] == str[j] and P[i + 1][j - 1]):
                P[i][j] = True
            if (P[i][j] == True):
                matrix[i][j] = (matrix[i][j - 1] + matrix[i + 1][j] + 1 - matrix[i + 1][j - 1])
            else:
                matrix[i][j] = (matrix[i][j - 1] + matrix[i + 1][j] - matrix[i + 1][j - 1])
    print(matrix)
    return matrix[0][n - 1]

class Solution(object):
    def minCut(self, s):
        if s == None or len(s) == 0:
            return 0
        p = [[False] * len(s) for i in range(len(s))]
        mc= []
        mc.append(0)
        for i in range(1, len(s)):
            minCutNum = float('inf')
            for j in range(i, -1, -1):
                if ( (j == i) or (j == i-1 and s[j] == s[i]) or (s[j] == s[i] and p[j+1][i-1]) ):
                    p[j][i] = True
                    if j == 0:
                        curMinCut = 0
                    else:
                        curMinCut = mc[j-1] + 1
                    minCutNum = minCutNum if minCutNum < curMinCut else curMinCut
            mc.append(minCutNum)
        return mc[len(s)-1]+1

str = "abaab"
print(Count(str, len(str)))
print(Solution.minCut(str,str))