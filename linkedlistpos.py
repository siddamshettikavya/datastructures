class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new

    def add_beg(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def add_pos(self, pos, data):
        if pos <= 0:
            print("Invalid position")
            return
        new = Node(data)
        if pos == 1:
            new.next = self.head
            self.head = new
            return
        itr = self.head
        for i in range(pos-2):
            if itr is None:
                print("Position out of range")
                return
            itr = itr.next
        if itr is None:
            print("Position out of range")
            return
        new.next = itr.next
        itr.next = new

    def remove_pos(self, pos):
        if pos <= 0 or self.head is None:
            print("Invalid position or empty list")
            return
        if pos == 1:   
            self.head = self.head.next
            return
        itr = self.head
        for i in range(pos-2):   
            if itr is None or itr.next is None:
                print("Position out of range")
                return
            itr = itr.next
        if itr.next is None:
            print("Position out of range")
            return
        itr.next = itr.next.next
            
    def remove_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")


ll = LinkedList()
ll.add_end(50)
ll.add_end(150)
ll.add_end(200)
ll.add_end(250)
ll.add_end(300)
ll.add_beg(10)
ll.add_pos(3, 99)   
ll.add_pos(4,455)
ll.remove_pos(3)
ll.display()
ll.remove_end()     # 
ll.display()
