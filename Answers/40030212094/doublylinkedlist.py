import gc
class Node:
    def __init__(self, data=None):
          
        self.data = data
        # reference to next node in DLL
        self.next = None  
        # reference to previous node in DLL
        self.prev = None
 
# Create DoublyLinkedList class
class DoublyLInkedList:
 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0;  

    # Create method to insert at begin
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
     
    # Create method to delete at begin
    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
 
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        curr = Node()
        curr = self.head
 
        while(curr != None):
            print(curr.data,end="  ")
            curr = curr.next
 
        
 
    def push(self, new_data):

    # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data=new_data)

    # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

    # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

    # 5. move the head to point to the new node
        self.head = new_node
    def deleteNode(self, dele): 
          
        # Base Case 
        if self.head is None or dele is None: 
            return 
          
        # If node to be deleted is head node 
        if self.head == dele: 
            self.head = dele.next
  
        # Change next only if node to be  
        # deleted is NOT the last node 
        if dele.next is not None: 
            dele.next.prev = dele.prev 
      
        # Change prev only if node to be  
        # deleted is NOT the first node 
        if dele.prev is not None: 
            dele.prev.next = dele.next
  
        # Finally, free the memory occupied  
        # by dele 
        # Call python garbage collector 
        gc.collect() 

    def pop_back(self):
        if(self.head != None):
          if(self.head.next == None):
            self.head = None
          else:
            temp = self.head
            while(temp.next.next != None):
              temp = temp.next
            lastNode = temp.next
            temp.next = None
            lastNode = None

    def searchNode(self, value):    
        i = 1;    
        flag = False;    
        #Node current will point to head    
        current = self.head;    
            
        #Checks whether the list is empty    
        if(self.head == None):    
            print("List is empty");    
            return;    
                
        while(current != None):    
            #Compare value to be searched with each node in the list    
            if(current.data == value):    
                flag = True;    
                break;    
            current = current.next;    
            i = i + 1;    
                
        if(flag):    
            print("Node is present in the list at the position : " + str(i));    
        else:    
            print("Node is not present in the list");    



    def get_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    



    def rotateList(self, n):  
        #Initially, current will point to head  
        current = self.head;  
          
        #n should not be 0 or greater than or equal to number of nodes present in the list  
        if(n == 0 or n >= self.size):  
            return;  
        else:  
            #Traverse through the list till current point to nth node  
            #after this loop, current will point to nth node  
            for i in range(1, n):  
                current = current.next;  
                  
            #Now to move entire list from head to nth node and add it after tail  
            self.tail.next = self.head;  
            #Node next to nth node will be new head  
            self.head = current.next;  
            #Previous node to head should be None  
            self.head.prev = None;  
            #nth node will become new tail of the list  
            self.tail = current;  
            #tail's next will point to None  
            self.tail.next = None;  
  


    def reverse_recursive(self):
        def reverse_util(current):
            if current is None:
                return

            next_node = current.next
            current.next = current.prev
            current.prev = next_node

            if current.prev is None:
                self.tail = current

            reverse_util(next_node)

        reverse_util(self.head)
        self.head, self.tail = self.tail, self.head

    def reverse_non_recursive(self):
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node

            if current.prev is None:
                self.tail = current

            current = next_node

        self.head, self.tail = self.tail, self.head

    def make_doubly(self, singly_linked_list):
        current = singly_linked_list.head
        while current is not None:
            new_node = Node(current.data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

            current = current.next




    def print_backward(self):
        if self.head is None:
            return

        current = self.tail
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.prev

        print(' '.join(result))









   
head = DoublyLInkedList()
head.insert_at_begin(10)
head.insert_at_begin(11)
head.insert_at_begin(11)
head.delete_at_begin()
head.push(3)
head.push(6)
head.pop_back()
head.searchNode(11)
print(head.get_size())
head.reverse_recursive()
head.print_list()
print()
head.reverse_non_recursive()
DoublyLInkedList().rotateList(1)


print("List ")
head.print_list()
print("backward")
head.print_backward()