class Element(object):
    def __init__(self,value):
        self.value= value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,object):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = object
        else:
            self.head = object

    def tailAppend(self, object):
        if self.tail:
            self.tail.next = object
            self.tail = self.tail.next
        else:
            self.head = object
            self.tail = self.head
        
        
        

    def printElements(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)
         


l = LinkedList()
e1 = Element(5)
e2 = Element(6)
e3 = Element(7)
e4 = Element(8)

l.tailAppend(e1)
l.tailAppend(e2)
l.tailAppend(e3)
l.tailAppend(e4)

l.printElements()

