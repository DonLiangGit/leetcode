//Time Limit Exceeded: because the minus
public class Solution {
    public int removeDuplicates(int[] A) {
        if (A.length <= 1) {
        	return A.length;
        }

        int loopPointer = 1;
        int newArrayPointer = 1;
        while (loopPointer < A.length) {
        	if(A[loopPointer] > A[newArrayPointer-1]) {
        		A[newArrayPointer] = A[loopPointer];
        		newArrayPointer ++;
        		loopPointer = newArrayPointer;
        		// bug
				// loopPointer ++;
				// newArrayPointer = loopPointer;
        	} else {
        		loopPointer ++;
        	}
        }

        return newArrayPointer;
    }
}