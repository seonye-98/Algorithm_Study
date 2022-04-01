'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        _list = []
        
        if head is None:
            return head 
        
        while curr:
            _list.append(curr.val)
            curr = curr.next
            
        _list = _list[::-1]
        
        reverse_head = ListNode(_list[0])
        curr = reverse_head
        
        for idx in range(1,len(_list)):
            tmp = ListNode(_list[idx])
            curr.next = tmp
            curr = curr.next
            
        return reverse_head