class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                c = s2[j]
                count2[c] = 1 + count2.get(c, 0)
                if count1.get(c, 0) < count2[c]:
                    break
                if count1.get(c, 0) == count2[c]:
                    cur += 1
                if cur == need:
                    return True
        
        return False