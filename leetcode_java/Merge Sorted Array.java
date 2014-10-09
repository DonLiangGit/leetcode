// ArrayIndexOutOfBoundsException
// Last executed input:	[1], []
public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        int mp = m - 1, np = n - 1;
        for(int index = m+n-1; index >=0; index--) {
        	if(mp>=0 && (np < 0||A[mp]>B[np])) {
        		A[index]=A[mp];
        		mp--;
        	} else {
        		A[index]=B[np];
        		np--;
        	}
        }
    }
}