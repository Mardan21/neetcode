class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        if digits:
            backtrack(digits, digitMap, res, "", 0)
        
        return res

def backtrack(digits, digitMap, res, cur, i):
    if i >= len(digits):
        res.append(cur)
        return
    
    curDigit = digits[i]
    chars = digitMap[curDigit]

    for c in chars:
        backtrack(digits, digitMap, res, cur + c, i + 1)
