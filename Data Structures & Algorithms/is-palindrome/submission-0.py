class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'\W+', '', s).lower()
        return cleaned == cleaned[::-1]