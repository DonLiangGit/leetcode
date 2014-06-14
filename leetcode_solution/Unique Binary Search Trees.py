# Time limited exceed
# Solution: 
#class Solution:
    #def numTrees(self, n):
        #if n == 0 or n == 1:
        	#return 1
        #else:
            #Solution.sum = 0
            #return self.uniBST(n)
    #def uniBST(self,n):
        #if n == 0 or n == 1:
            #return 1
    	#for k in xrange (1,n+1):
	        #left = self.uniBST(k-1)
	        #right = self.uniBST(n-k)
	        #Solution.sum += left*right
        #return Solution.sum

class Solution:
    # @return an integer
    def numTrees(self, n):
        num = [0 for i in range(n+1)]
    	num[0] = 1

    	for j in xrange(1,n+1):
    		for k in xrange(j):
    			num[j] += num[k]*num[j-k-1]
    	return num[n]