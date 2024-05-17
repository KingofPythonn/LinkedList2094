# Python3 program to show inserting a node
# at front of given Linked List
 
# A linked list node
import sys
import math
 
class Node:
    def __init__(self):
        self.data = None
        self.next = None
 
# Given a reference (pointer to pointer)
# to the head of a list and an int, inserts
# a new node on the front of the list.
 
 
def insertAtFront(head_ref, new_data):
 
    # 1. allocate node
    new_node = Node()
 
    # 2. put in the data
    new_node.data = new_data
 
    # 3. Make next of new node as head
    new_node.next = head_ref
 
    # 4. move the head to point
    # to the new node
    head_ref = new_node
 
    return head_ref
 
def append(head_ref, new_data):
    # Create a new node
    new_node = Node()
    new_node.data = new_data
    # Store the head reference in a temporary variable
    last = head_ref
 
    # Set the next pointer of the new node as None since it
    # will be the last node
    new_node.next = None
 
    # If the Linked List is empty, make the new node as the
    # head and return
    if head_ref is None:
        return new_node
 
    # Else traverse till the last node
    while last.next is not None:
        last = last.next
 
    # Change the next pointer of the last node to point to
    # the new node
    last.next = new_node
 
    return head_ref
# This function prints contents of
# linked list starting from head
def removeFirstNode(head):
    if not head:
        return None
    temp = head
 
    # Move the head pointer to the next node
    head = head.next
    temp = None
    return head
 
def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print("\n")
 

def removeLastNode(head):
    if head == None:
        return None
    if head.next == None:
        head = None
        return None
    second_last = head
    while(second_last.next.next):
        second_last = second_last.next
    second_last.next = None
    return head

def search(head, x):
 
        # Initialize current to head
        current = head
 
        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True  # data found
 
            current = current.next
 
        return False  # Data Not found

def clear(head):
    head=None

def getCount(head):
        temp =  head# Initialise temp
        count = 0  # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

def print_backward(head):
        if head is None:
            return

        current = head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next

        print(' '.join(result[::-1]))

def reverse(head): 
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        head = prev
def reverseUtil( curr, prev): 
  
        # If last node mark it head 
        if curr.next is None: 
            head = curr 
  
            # Update next to prev node 
            curr.next = prev 
            return
  
        # Save curr.next node for recursive call 
        next = curr.next
  
        # And update next 
        curr.next = prev 
  
        reverseUtil(next, curr) 
  
    # This function mainly calls reverseUtil() 
    # with previous as None 
  
def reverse1(head): 
        if head is None: 
            return
        reverseUtil(head, None) 
 
# Driver code
if __name__ == '__main__':
    # Start with the empty list
    head = None
    head = insertAtFront(head, 6)
    head = insertAtFront(head, 5)
    head = insertAtFront(head, 4)
    head = insertAtFront(head, 3)
    head = insertAtFront(head, 2)
    head = append(head, 1)
    head = append(head, 3)

    head = removeFirstNode(head)
    head = removeLastNode(head)
    # head=clear(head)
    # reverse1(head)

    x = 4
 
    print(getCount(head))



    # Function call
    if search(head, 4):
        print("Yes")
    else:
        print("No")

        

    print("After inserting nodes at thier front: ", end="")
    printList(head)
    print_backward(head)