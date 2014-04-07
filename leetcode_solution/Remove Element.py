class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        index = 0
        for i in range(0,len(A)):
            if A[i] != elem:
                #A.pop([i]) 
                A[index] = A[i]# without becomes wrong answer. [4,5]4input, output[4] instead of [5]
                index += 1
                
        return index