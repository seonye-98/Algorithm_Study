'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.
'''

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        curr = head
        _list = []
        while curr:
            _list.append(curr.val)
            curr = curr.next
            
        if len(_list) == 1:
            return True
        else:
            if len(_list) %2 == 0:
                l_list = _list[:len(_list)//2]
                r_list = _list[len(_list)//2:]
            else:
                l_list = _list[:len(_list)//2+1]
                r_list = _list[len(_list)//2:]
            
            if l_list == r_list[::-1]:
                return True
            else:
                return False