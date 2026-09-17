"""

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""

#the anagram can be itslef if it's alone, or an empty string


strs = ["act","pots","tops","cat","stop","hat"]


class Solution:
    def Anagram(self, strs:list) -> list:
        temp = []
        for i in strs:
            sortedstr = "".join(sorted(i))
            temp.append(sortedstr)
#output for temp rightnow is ['act', 'opst', 'opst', 'act', 'opst', 'aht']
        visited = [False] * len(strs)
        res =[]

        for i in range(len(temp)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True
            for j in range(i + 1, len(temp)):
                if not visited[j] and temp[i] == temp[j]:
                    group.append(strs[j])
                    visited[j] = True
            res.append(group)
        res.sort(key=len)
        return res


p = Solution()
print(p.Anagram(strs))