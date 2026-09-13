s="racecar"
t="carrace"

class Solution:
    def Vanagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)

o = Solution()
print(o.Vanagram(s,t))