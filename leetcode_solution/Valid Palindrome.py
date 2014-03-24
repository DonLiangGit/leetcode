class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        if len(s) == 1:
            return True
        anotherS = s.lower()
        newString = []
        for i in anotherS:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                newString.append(i)
        if not newString:
            return True
        head = 0
        tail = len(newString) - 1
        while head < tail:
            if newString[head] != newString[tail]:
                return False
            else:
                head += 1
                tail -= 1
        return True
			