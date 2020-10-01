#to create a linked list with few sample nodes as static inputs
#class
class Node:
    def __init__(self, data):  
        self.data = data  
        self.next = None
class LinkedList:
    
    def_init_(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("the given previous node must in LinkedList.")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data),
            temp=temp.next
if_name_=='_main_':
    llist=LinkedList()
    llist.append(21)
    llist.push(19);
    llist.push(87);
    llist.append(95)
    llist.insertAfter(llist.head.next,5)
    print('Created linked list is:'),
    list.printList()
            
           
            
    
    
