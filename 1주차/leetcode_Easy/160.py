'''
160. Intersection of Two Linked Lists

오답

'''

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        intersectVal = 0
        listA = []
        listB = []
        
        curr = headA
        while curr:
            listA.append(curr.val)
            curr = curr.next
        
        curr = headB
        while curr:
            listB.append(curr.val)
            curr = curr.next
            
        print(listA, listB)
        first_come = ListNode(0)
        listA = listA[::-1]
        listB = listB[::-1]
        
        for idx, num in enumerate(listA):
            if num != listB[idx]:
                first_come.val = listA[idx-1]
                print(listA[idx-1],'different')
                
        return first_come