class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
llist = LinkedList()

for element in (1, 5, 7, 3, 8, 2, 3):
    llist.append(element)

current = llist.head
index = 0
while current:
    if current.data == 7:
        print("Index of 7:", index)
        break
    current = current.next
    index += 1
