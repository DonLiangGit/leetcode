public class Solution {
    public int removeElement(int[] A, int elem) {
        int loopPointer = 0;
        int newLengthPointer = 0;

        while (loopPointer < A.length) {
        	if(A[loopPointer] != elem) {
        		A[newLengthPointer] = A[loopPointer];
        		newLengthPointer ++;
        	}
        	loopPointer ++;
        }
        return newLengthPointer;
    }
}