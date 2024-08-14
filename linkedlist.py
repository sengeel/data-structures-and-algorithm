#  CREATING A NODE FOR A SINGLE LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#  CREATING A SINGLE LINKED LIST

class Sll:
    def __init__(self):
        self.head = None

    def transversal(self):
        
        if self.head is None:
            print("Single linked list is empty")
        
        else:
            a = self.head
            while a is not None:
                print(a.data, end="  ")
                a = a.next
    
    def insert_at_beginning(self, data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_at_end(self, data):
        print()
        ne =Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insert_at_specified_node(self, position, data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1, position-1):
            a = a.next 
        nib.next = a.next
        a.next = nib

    def deletion_at_beginning(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None

    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next

        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def deletion_at_particular_node(self, position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1, position-1):
            prev = prev.next
            a = a.next
        prev.next = a.next
        a.next = None

   
        

n1 = Node(5)
sll = Sll()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next =n3
n4 = Node(20)
n3.next = n4



sll.transversal()
sll.insert_at_beginning(2)
sll.transversal()
sll.insert_at_end(25)
sll.transversal()
sll.insert_at_specified_node(4,7)
sll.transversal()
sll.deletion_at_beginning()
sll.transversal()
sll.deletion_at_end()
sll.transversal()
sll.deletion_at_particular_node(3)
sll.transversal()





# CREATING A NODE FOR A DOUBLE LINKED LIST
class Node:
   def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

# CREATING A SINGLE LINKED LIST

class Dll:
    def __init__(self):
        self.head = None


    def forward_transversal(self):
        
        if self.head is None:
            print("Double Link List is empty")
        
        else:
            a = self.head
            while a is not None:
                print(a.data,  end="   ")
                a = a.next
                

    def backward_transversal(self):
        print()
        if self.head is None:
            print("Double Link List is empty")
        
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            while a is not None:
                print(a.data, end="  ")
                a = a.prev
    
    def insertion_at_beginning(self, data):
        print()
        nb = Node(data)
        a = self.head
        a.prev = nb
        nb.next = a
        self.head = nb

    def insertion_at_end(self, data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a

    def insertion_at_specific_node(self, position, data):
        print()
        nib = Node(data)
        prev = self.head
        a = self.head.next

        for i in range(1, position-1):
            a = a.next
            prev = prev.next
        prev.next = nib
        nib.prev = prev
        nib.next = a
        a.prev = nib

    def deletion_at_beginning(self):
        print()
        prev = self.head
        a = self.head.next
        self.head= a
        a.prev = None
        prev.next = None
        

    def deletion_at_end(self):
        print()
        prev = self.head 
        a = self.head.next
        
        while a.next is not None:
            a = a.next
            prev = prev.next
        
        prev.next = None
        a.prev =None

    def deletion__at_specific_node(self, postion):
        print()
        prev = self.head
        a = self.head.next

        for i in range(1, postion-1):
            a = a.next
            prev = prev.next

        prev.next = a.next
        a.next.prev = prev
        a.next = None
        a.prev = None

        

    

  




n1 = Node('Banana')
dll = Dll()
dll.head = n1
n2 = Node('Mango')
n2.prev = n1
n1.next = n2
n3 = Node('Orange')
n3.prev = n2
n2.next =n3
n4 = Node('Grape')
n4.prev = n3
n3.next = n4
dll.forward_transversal()
dll.backward_transversal()
dll.insertion_at_beginning('Guava')
dll.forward_transversal()
dll.backward_transversal()
dll.insertion_at_end('Casava')
dll.forward_transversal()
dll.backward_transversal()
dll.insertion_at_specific_node(4, 'Melon')
dll.forward_transversal()
dll.backward_transversal()
dll.deletion_at_beginning()
dll.forward_transversal()
dll.backward_transversal()
dll.deletion_at_end()
dll.forward_transversal()
dll.backward_transversal()
dll.deletion__at_specific_node(3)
dll.forward_transversal()
dll.backward_transversal()
