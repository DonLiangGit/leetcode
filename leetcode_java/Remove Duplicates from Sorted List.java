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
// public class Solution {
//     public ListNode deleteDuplicates(ListNode head) {
        
//     }
// }
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {

		if (head == null || head.next == null) {
			return head;
		} else {
			ListNode headForward = head;
			ListNode compareNode = head.next;

			while (compareNode != null) {
				if (compareNode.val == headForward.val) {
					headForward.next = compareNode;
					compareNode = compareNode.next;
				} else {
					headForward =  compareNode.next;
					compareNode = compareNode.next;
				}
			}
			return head;
		}
    }
}