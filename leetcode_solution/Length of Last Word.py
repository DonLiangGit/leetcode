class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s:
            return 0
                
        i = len(s) - 1
        
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        lastLength = 0
        while i >= 0 and s[i] !=' ':
            lastLength += 1
            i -= 1
        
        return lastLength