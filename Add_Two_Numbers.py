#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        inc =0
        value = l1.val+l2.val
        if(value>9):
            value=value%10
            inc=1
        result = ListNode(value)
        temp= result
        l1=l1.next
        l2=l2.next
        
        while l1!=None or l2!= None:
            value=inc
            if l1!=None:
                value+=l1.val
                l1=l1.next
            if l2!= None:
                value+=l2.val
                l2=l2.next
            
            inc=0
            if(value>9):
                value=value%10
                inc=1
            temp.next=ListNode(value)
            temp=temp.next
        if inc==1:
            temp.next= ListNode(inc)
        return result
