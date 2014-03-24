class Solution:
    # @return an integer
    def reverse(self, x):
        output = 0
        flag = False
        if x < 0:
            flag = True
            x = -x
        
        while x > 0:
            number = x - x/10 * 10
            output = output * 10 + number
            x = x/10
        
        if flag == True:
            output = -output
        return output
        
        