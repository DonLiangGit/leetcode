// Input: [1,2,4], Output: 2 is wrong should be 3!
public class Solution {
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length == 0) { return 0; }

        int len = prices.length;
        int maxProfit = 0;
        int min = prices[0];
        for(int i = 1; i < len; i++) {
        	int tempProfit = prices[i] - min;
        	if(maxProfit < tempProfit) {
        		maxProfit = tempProfit;
        	}
        	if(min > price[i]) {
        		min = prices[i];
        	}
        }
        return maxProfit;
    }
}