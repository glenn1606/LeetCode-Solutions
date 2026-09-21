class Solution:
    def Solve(self, s: list, k:int) -> list:
        res = {}
        freq = [[] for i in range(len(s)+1)]
        for i in s:
            res[i] = res.get(i, 0) +1
        for n,c in res.items():
            freq[c].append(n)
        ress = []
        for i in range(len(freq)-1, 0 , -1 ):
            for n in freq[i]:
                ress.append(n)
                if len(ress) == k:
                    return ress
        

o = Solution()
print(o.Solve(s = [1,2,2,3,3,3] , k = 2))