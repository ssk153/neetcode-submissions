class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "LOL"
        return "&&".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "LOL":
            return []
        return s.split("&&")