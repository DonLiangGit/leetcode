/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
// I miss a problem that the cycle is A partially cycle.
public class Solution {
    public boolean hasCycle(ListNode head) {
    	if (head == null) return false;
    	if (head.next == null) return false;

    	ListNode fastPointer = head;
    	ListNode slowPointer = head;

    	while (fastPointer!=null && fastPointer.next!=null) {
    		slowPointer = slowPointer.next;
    		fastPointer = fastPointer.next.next;

    		if (fastPointer == slowPointer){
    			return true;
    		}
    	}
    	return false;
    }
}