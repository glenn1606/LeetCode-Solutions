
strs = ["act","pots","tops","cat","stop","hat"]


class Solution:
    def Anagram(self, strs:list) -> list[list[str]]:
        res = {}


        for s in strs:
            count = [0] *26
            for c in s:
                count[ord(c) - ord("a")] +=1
            
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)
        return res.values()
s = Solution()
print(s.Anagram(strs))