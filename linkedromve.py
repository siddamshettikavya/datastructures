class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def dele_beg(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    def dele_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
            
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def display(self):
        if self.head is None:
            print("empty linked list ")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

l = linkedlist()
n1 = node(10)
l.head = n1
n2 = node(20)
n1.next = n2
n3 = node(30)
n2.next = n3
n4 = node(40)
n3.next = n4
n5 = node(50)
n4.next = n5
l.dele_beg()
l.dele_end()
l.display()