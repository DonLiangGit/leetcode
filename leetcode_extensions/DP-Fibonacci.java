// Fibonacci
// Dynamic Programming

public class Solution {

    public int[] Fibonacci(int N) {
    	// if(N < 0) {
    	// 	return nothing;
    	// } else if (N < 2) {
    	// 	return nothing;
    	// }

    	long[] fib = new long[N+1];
    	// base cases
		fib[0] = 0;
		fib[1] = 1;
		
		// bottom-up Dynamic Programming
		for(int n = 2; n <= N; n++) {
			fib[n] = fib[n-1] + fib[n-2];
		} 

		return fib;
    }
}