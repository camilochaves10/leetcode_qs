'''You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their nodes 
contains a single digit. Add the two numbers and return the sum as a 
linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: 
Optional[ListNode]) -> Optional[ListNode]:
        head = prev = ListNode()
        carry  = 0
        while l1 and l2:
            if l1.val + l2.val + carry <10:
                num = l1.val + l2.val + carry
                carry = 0
            else:
                num = (l1.val + l2.val + carry)%10
                carry = 1
            
            head.next = ListNode(num)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            print(l1.val)
            if l1.val + carry <10:
                num = l1.val + carry
                carry = 0
            else:
                num = (l1.val+ carry)%10
                carry = 1
            head.next = ListNode(num)
            head = head.next
            l1 = l1.next
        while l2:
            if l2.val + carry <10:
                num = l2.val + carry
                carry = 0
            else:
                num = (l2.val+ carry)%10
                carry = 1
            head.next = ListNode(num)
            head = head.next
            l2 = l2.next
        if carry == 1:
            head.next = ListNode(1)
            head = head.next

        
        return prev.next
