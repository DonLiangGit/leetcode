public class Solution {
    public double pow(double x, int n) {
        if(n < 0) {
        	return 1/power(x,-n);
        } else {
        	return power(x,n);
        }
    }

    public double power(double x, int n) {
    	if(n == 0) {
    		return 1;
    	}
    	double returnValue = power(x,n/2);
    	if(n%2 == 0) {
    		return returnValue * returnValue;
    	} else {
    		return returnValue * returnValue * x;
    	}
    }
}