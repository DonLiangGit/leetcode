public class Solution {
    public int climbStairs(int n) {
        if(n <= 2) {
        	return n;
        }

        int firstElement = 1;
        int secondElement = 2;
        int temp = 0;
        for(int next = 3; next < n; next++) {
        	temp = firstElement + secondElement;
        	firstElement = secondElement;
        	secondElement = temp;
        }

        return temp;
    }
}