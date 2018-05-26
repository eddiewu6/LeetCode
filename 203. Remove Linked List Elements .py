#Idea, three situations, multiple val from head, val in the middle of linked list, val at the end
#O(n) in time, O(1) in space
#AC in 117ms


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        #Remove all the head vals
        while head.val == val:
            head = head.next
            #Deal with [1,1,1,1] 1 situation
            if head == None:
                return None

        prev = head
        cur = head.next
        while cur != None:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
                
            else:
                cur = cur.next
                prev = prev.next
        return head