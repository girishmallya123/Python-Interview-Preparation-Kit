class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    # Add a value to the end of our linked list
    def append(self, val):
        ptr = self.head

        while(ptr.next):
            ptr = ptr.next
        ptr.next = Node(val)

    '''
    method to delete a node in linked_list, with a parameter pos
    if pos is not given, it defaults to deleting the first element in the list.
    if pos is negative, it deletes the last element.
    '''
    def delete(self, pos=0):
        if pos==0:
            return self.delete_at_front()
        if pos<0:
            return self.delete_at_back()
        
        tmp = self.head
        n = 0
        while(tmp.next):
            if n == pos:
                tmp.next = tmp.next.next

            n+=1
            tmp = tmp.next

    def delete_at_back(self):
        tmp = self.head
        if not tmp.next:
            return None

        while(tmp.next.next):
            tmp = tmp.next
        tmp.next = None

    def delete_at_front(self):
        tmp = self.head
        if not self.head.next:
            return None

        self.head = self.head.next
        del tmp

    # reverse the linkedlist in place
    def reverse(self):
        prev = None
        curr = self.head
        
        if not curr:
            return self.head
        if not curr.next:
            return self.head
        
        next = curr.next
        
        while(next):
            tmp = next.next
            next.next = curr
            curr.next = prev
            prev = curr
            curr = next
            next = tmp
            
        self.head = curr

    # Add a value to the front of our linked list
    def insert_at_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    """
    Insert at a specified position (0 indexed) in our list.
    > if n is out of bounds, it just appends to the end of the list.
    > if n is 0 or our list has only one node, we just call the append method
    on the linked list class. 
    """
    def insert_at_position(self, val, n):
        if n == 0:
            self.insert_at_front(val)
            return
        
        if self.head.next == None:
            self.append(val)
            return

        curr = self.head.next
        prev = self.head
        position = 1

        while(curr):
            if position == n:
                break
            curr = curr.next
            prev = prev.next
            position +=1

        if not curr:
            prev.next = Node(val)
            return 

        if not curr.next:
            curr.next = Node(val)
            return

        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr



# Method that traverses the Linked List and prints the nodes.
def print_list(head):
        while(head):
            print(head.val, end = "")
            if head.next:
                print(" ->", end = "")    
            head = head.next


def main():
    MyAwesomeLinkedList = LinkedList()
    MyAwesomeLinkedList.head = Node(1)
    MyAwesomeLinkedList.append(2)
    MyAwesomeLinkedList.append(3)
    MyAwesomeLinkedList.insert_at_front(25)
    MyAwesomeLinkedList.insert_at_position(33, 25)
    #MyAwesomeLinkedList.delete(2)
    print("Printing before reversing!")
    print_list(MyAwesomeLinkedList.head)
    print("\nAfter reversing\n")
    MyAwesomeLinkedList.reverse()

    print_list(MyAwesomeLinkedList.head)

if __name__ == "__main__":
    main()
