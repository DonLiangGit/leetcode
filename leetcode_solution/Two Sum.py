class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        seen = {}
        for i in range(len(num)):
            remainder = target - num[i]
            if remainder not in seen:
                seen[num[i]] = i+1
            else:
                return seen[remainder], i+1