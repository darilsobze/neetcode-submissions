class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result = result + "ab+*/" +word
        return result
    def decode(self, s: str) -> List[str]:
        return s.split("ab+*/")[1:]