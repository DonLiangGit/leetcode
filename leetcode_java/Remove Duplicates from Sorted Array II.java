// Follow up for "Remove Duplicates":
// What if duplicates are allowed at most twice?

// For example,
// Given sorted array A = [1,1,1,2,2,3],

// Your function should return length = 5, and A is now [1,1,2,2,3].


// Input:	[1,1,1]
// Output:	[1]
// Expected:	[1,1]
// Solution: need to do in place.

public class Solution {
    public int removeDuplicates(int[] A) {
    	if(A == null) {
    		return 0;
    	}
    	if(A.length <= 2) {
    		return A.length;
    	}

    	int i = 1, count = i;
    	int j = 2;
    	while(j < A.length) {
    		if(A[i] == A[j] && A[i] == A[i-1]) {
    			j ++;
    		}
    		else {
    			i ++;
    			A[i] = A[j];
    			j ++;
    		}
    	}

    	return i+1;
    }
}