class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length == 0:
            return 0
        if length == 1:
            return 1
        index = 0
        for i in A[1:]:
            if i != A[index]:
                index += 1
                A[index] = i
        return index + 1