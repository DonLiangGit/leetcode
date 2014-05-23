class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        m = x
        a = 0
        while m != 0:
            a = m % 10 + a * 10
            m = m / 10
        if x == a:
            return True
        else:
            return False   