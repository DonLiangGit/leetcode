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
    public ListNode deleteDuplicates(ListNode head) {
        
        if (head == null) {return null;}
        if (head.next == null){return head;}

        ListNode preNode = new ListNode(0);
        preNode.next = head;
        head = preNode;

        ListNode stableNode = preNode;
        while (stableNode.next!=null) {
        	ListNode flowNode = stableNode.next;
        	while (flowNode.next!=null && flowNode.val == flowNode.next.val) {
        		flowNode = flowNode.next;
        	}
        	if(stableNode.next != flowNode) {
        		// flowNode.next not flowNode
        		stableNode.next = flowNode.next;
        	} else {
        		stableNode = stableNode.next;
        	}
        }
        return head.next;

    }
}