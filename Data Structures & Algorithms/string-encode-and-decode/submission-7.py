class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "No Value"
        elif len(strs) == 1:
            return "**" + "".join(strs)
        
        return "._.".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "No Value":
            return []
        elif s.startswith("**"):
            return [s[2:]]
            
        return s.split("._.")
