class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            print("middle node:",slow.data)
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
        print("None")


l=linkedlist()
n1=node(10)
l.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n4=node(20)
n3.next=n4
n5=node(50)
n4.next=n5

l.display()
l.middle()