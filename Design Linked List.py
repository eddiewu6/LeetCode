#Design Linked List
class LinkListNode(object):
    def __init__(self,num):
        self.val = num
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        
        if index > self.length - 1:
            return -1
        i = 0
        cur = self.head
        while i < index:
            cur = cur.next
            i += 1
        #print("getValByIndex",index,cur.val)
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        
        newHead = LinkListNode(val)
        newHead.next = self.head
        self.head = newHead
        self.length += 1
        if self.length == 1:
            self.tail = self.head
        #Print log and linkList 
        #print("addhead",self.head.val)
        #self.printLinkedList()

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        
        newTail = LinkListNode(val)
        if self.length > 0:
            self.tail.next = newTail
            self.tail = self.tail.next
        elif self.length == 0:
            self.tail = newTail
            self.head = self.tail
        self.length += 1
        #Print log and linkList 
        #print("addAtTail",self.tail.val)
        #self.printLinkedList()

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            i = 1
            pre = self.head
            cur = pre.next
            while i < index:
                pre = pre.next
                cur = cur.next
                i += 1
            newNode = LinkListNode(val)
            pre.next = newNode
            newNode.next = cur
            self.length += 1
        #Print log and linkList    
        #print("addAtIndex",index, val)
        #self.printLinkedList()
    
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < self.length and index >= 0:
            if index == 0:
                self.head = self.head.next
                if self.length == 1:
                    self.tail = None
                self.length -= 1
            else:
                if self.length == 1 and index == 0:
                    self.head = None
                    self.tail = None
                    self.length = 0
                else:
                    i = 1
                    pre = self.head
                    cur = pre.next
                    while i < index:
                        pre = pre.next
                        cur = cur.next
                        i += 1
                    if i == self.length-1:
                        self.tail = pre
                    cur = cur.next
                    pre.next = cur
                    self.length -= 1
        #Print log and linkList    
        #print("deleteAtIndex",index)
        #self.printLinkedList()
    
    def printLinkedList(self):
        #Print log and linkList 
        res = ""
        head = self.head
        while head != None:
            res = res + str(head.val)+"->"
            head = head.next
        print("LinkList:"+res[:len(res)-2])
        print("head:"+str(self.head.val))
        print("tail:"+str(self.tail.val))
        print("length:"+str(self.length))
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)