s="racecar"
t="carrace"

class Solution:
    def Anagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False

        s_sorted=sorted(s)
        t_sorted=sorted(t)

        p1, p2 = 0, 0

        while p1 < len(s_sorted) and p2 < len(t_sorted):
            if s_sorted[p1] != t_sorted[p2]:
                return False
            p1 += 1
            p2 += 1
        return True

o = Solution()
print(o.Anagram(s,t))