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

    # Add a value to the front of our linked list
    def insert_at_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    """
    Insert at a random position (0 indexed) in our list.
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

    print_list(MyAwesomeLinkedList.head)

if __name__ == "__main__":
    main()
