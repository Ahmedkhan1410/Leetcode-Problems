class Solution:
    def scoreOfString(self, s: str) -> int:
        addition = 0
        for i in range(len(s) - 1):
            addition += abs(ord(s[i]) - ord(s[i+1]))
        return addition