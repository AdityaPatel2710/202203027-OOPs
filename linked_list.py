class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        current_node = self.head
        self.head = current_node.next
        current_node = None

    def delete_at_end(self):
        if self.head is None:
            return
        current_node = self.head
        previous_node = None
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        if previous_node is None:
            self.head = None
        else:
            previous_node.next = None

    def delete_node(self, key):
        current_node = self.head
        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node is not None and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
my_list = LinkedList()

# Insert some nodes at the beginning and end of the list
my_list.insert_at_beginning(3)
my_list.insert_at_end(5)
my_list.insert_at_beginning(1)

# Print the current list
my_list.print_list()  # Output: 1 -> 3 -> 5

# Delete the first and last nodes
my_list.delete_at_beginning()
my_list.delete_at_end()

# Print the updated list
my_list.print_list()  # Output: 3