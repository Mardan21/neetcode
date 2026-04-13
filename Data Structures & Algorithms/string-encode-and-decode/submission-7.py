class Solution:

    def encode(self, strs: List[str]) -> str:
        # init an empty result string -> ""
        # go through the list of words:
        #   append each word and after each word add non-ascii char -> ä
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "@" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


