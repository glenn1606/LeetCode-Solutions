class Solution:
    def Solve(self, s: list, k:int) -> list:
        res = {}
        for i in s:
            res[i] = res.get(i, 0) +1
            
        sorted_nums = sorted(res.keys(), key=lambda x: res[x], reverse=True)

        return sorted_nums[:k]
o = Solution()
print(o.Solve(s = [1,2,2,3,3,3] , k = 2))