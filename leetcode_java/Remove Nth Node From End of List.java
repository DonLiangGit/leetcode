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
//     public ListNode removeNthFromEnd(ListNode head, int n) {
//         if (head == null) {
//         	return head;
//         }

//         ListNode forwardPointer = head;
//         ListNode removePointer = head;
//         ListNode returnPointer = head;
//         int step = 0;

//         while ( n > 1 ) {
//         	forwardPointer = forwardPointer.next;
//         	n--;
//         }

//         while (forwardPointer != null) {
//         	forwardPointer = forwardPointer.next;
//         	step++;
//         }
//         while (step>1) {
//         	removePointer = removePointer.next;
//         	step--;
//         }
//         if (removePointer.next != null) {
//         	removePointer.next = removePointer.next.next;
//         } else {
//         	removePointer.next = null;
//         }
//         return returnPointer;
//     }
// }
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
// runtime error: nullpointer based on this line:removePointer.next = removePointer.next.next;
// solution:
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
        	return head;
        }

        ListNode prePointer = new ListNode(0);
        prePointer.next = head;
        head = prePointer;

        ListNode forwardPointer = head.next;
        ListNode removePointer = head.next;

        while (n > 1){
        	forwardPointer = forwardPointer.next;
        	n--;
        }

        while (forwardPointer.next != null) {
        	forwardPointer = forwardPointer.next;
        	prePointer = prePointer.next;
        	removePointer = removePointer.next;
        }
        prePointer.next = removePointer.next;
        return head.next;
    }
}