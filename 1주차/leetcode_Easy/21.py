'''
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class Solution(object):
    def node2list(self, _node):
        _list = []
        while _node != None:
            _list.append(_node.val)
            _node = _node.next
        return _list
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        answer = self.node2list(list1) + self.node2list(list2)
        answer.sort()
    
        head = ListNode(-1)
        cursor = head
        
        for item in answer:
            tmp = ListNode(item)
            cursor.next = tmp
            cursor = cursor.next
            
            
        return head.next