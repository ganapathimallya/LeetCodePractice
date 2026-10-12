class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stri=[]
        stri=s.split()
        m=len(stri[-1])
        return m