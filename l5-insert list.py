#To insert a node at beginning of the list that has been taken already
#class

class Node: 
  
 def __init__(self, data): 
            self.data = data;  
            self.next = None; 
class CreateList:
 def_init_(self):
self.head=Node(None);
self.tail=Node(None);
self.head.next=self.tail;
self.tail.next=self.head;
def addAtStart(self,data):
    newNode=Node(data);
    if self.head.data is None:
        self.head=newNode;
        self.tail=newNode;
        newNode.next=self.head;
        else:
            temp=self.head;
            newNode.next=temp;
            self.tail.next=self.head;
def display(self):
    current=self.head;
    if self.head is None:
        print("List is empty");
        return;
    else:
        print("Adding nodes to the start of the list:");
        print(current.data),
        while(current.next!=self.head):
            current=current.next;
            print(current.data),
            print("\n");
            class CircularLinkedList:
                cl=CreateList();
                cl.addAtStart(95);
                cl.display();
                cl.addAtStart(87);
                cl.display();   #
                cl.addAtStart(19);
                cl.display();
                cl.addAtStart(21);
                cl.display();
                

   

