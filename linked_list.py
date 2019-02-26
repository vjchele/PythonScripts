class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self,head=None):
        self.head = head

    def append(self,object):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = object
        else:
            self.head = object

    def print():
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)


l = LinkedList()
head = Node(5)
