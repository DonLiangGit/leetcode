public class Solution {
    public int reverse(int x) {
        Boolean Flag = FALSE;
        if(x == 0) {
        	return 0;
        }
        if(x < 0) {
        	x = -x;
        	Flag = TRUE;
        }

        int res = 0;
        while(x > 0) {
        	int left = x % 10;
        	x = x / 10;
        	res = res * 10 + left;
        }
        if(Flag == TRUE) {
        	res = -res;
        }
        return res;
    }
}