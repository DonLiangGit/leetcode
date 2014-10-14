public class Solution {
    public boolean isPalindrome(int x) {
    	int original = x;
    	int result = 0
        if(x < 0) {
        	return false;
        }

        while(x!=0) {
        	result = result * 10;
        	result = result + x%10;
        	x = x/10;
        }
        return result == original;
    }
}