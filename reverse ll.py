class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def reverse(self):
        prev=None
        temp=self.head

        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next

        self.head=prev

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
n4=node(40)
n3.next=n4
n5=node(50)
n4.next=n5
print("Before")
l.display()
l.reverse()
print("After")
l.display()