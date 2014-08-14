/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
    	// two boundaries here
    	// if (head==null) { return null; }
    	// if (head.next == null) { return head; }

    	ListNode preNode = new ListNode(0);
    	preNode.next = head;
    	ListNode swapPre = preNode;
    	ListNode swapFirst = head;

    	ListNode temp = null;

    	while (swap1!=null && swap.next!=null) {
    		temp = swapFirst.next.next;
    		swapFirst.next.next = swapPre.next;
    		swapPre.next = swapFirst.next;
    		swapFirst.next = temp;

    		swapPre = swapFirst;
    		swapFirst = swapPre.next;
    	}    		

    	return preNode.next;      
    }
}