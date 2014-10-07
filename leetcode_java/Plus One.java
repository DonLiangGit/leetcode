public class Solution {
    public int[] plusOne(int[] digits) {
        if(A.length <= 2) {
        	return A.length;
        }

        int carry = 1
        for(int i = A.length-1; i >= 0, i--) {
        	int digit = (A[i] + carry)%10;
        	carry = (A[i] + carry)/10;
        	digits[i] = digit;
        	if(carry == 0) {
        		return digits;
        	} 
        }
        int[] res = new Int[A.length+1];
        res[0] = 1;
        return res;
    }
}