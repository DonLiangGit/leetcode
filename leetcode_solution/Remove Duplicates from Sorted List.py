# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
		if head == None:
			return None
		if head.next == None:
			return head	
		another = head
		while head.next != None: 
		    while head.val != head.next.val:
		        head.next = head.next
                head = head.next
            head.next = None
		return another
#Error_1 Time Limit Exceeded:
#