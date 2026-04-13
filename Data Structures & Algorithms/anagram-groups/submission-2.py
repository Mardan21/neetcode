class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Brute Force
        # res = {}
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS] = res.get(sortedS, [])
        #     res[sortedS].append(s)

        # return list(res.values())

        # Hash Map
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)] = res.get(tuple(count), [])
            res[tuple(count)].append(s)
        return list(res.values())
            
