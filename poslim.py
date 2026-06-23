class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_pos(self, pos, data):
        newnode = node(data)
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            return
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode

    def display(self):
        if self.head is None:
            print("empty linked list")
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
l.insert_pos(3,35)
l.display()