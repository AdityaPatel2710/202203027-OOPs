class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            return
 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
 
        last_node.next = new_node
 
    def delete_greater_than_25(self):
        current_node = self.head
        prev_node = None
 
        while current_node:
            if current_node.data > 25:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next
 
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
 
llist = LinkedList()
n = int(input("Enter the number of elements in the linked list: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    llist.append(element)

print("Linked list :")
llist.print_list()
 
llist.delete_greater_than_25()
 
print("\nLinked List after deleting nodes with values greater than 25 : ")
llist.print_list()
