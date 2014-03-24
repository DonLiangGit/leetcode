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
        else:
            another = head
            tag = head.next
            while tag.next != None:
                if head.val == tag.val:
                    tag = tag.next
                else:
                    head.next = tag
                    head = tag
                    tag = tag.next
            if tag.next == None:
                if head.val == tag.val:
                    head.next = None
                else:
                    head.next = tag
                
        return another
            
        