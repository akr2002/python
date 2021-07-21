class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    # Add data elements
    def push(self, newVal):
        newNode = Node(newVal)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    # Print
    def printList(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    # Insert
    def insert(self, prevNode, newVal):
        if prevNode is None:
            return

        newNode = Node(newVal)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode

        if newNode.next is not None:
            newNode.next.prev = newNode

    # Append
    def append(self, newVal):
        newNode = Node(newVal)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode 
        newNode.prev = last
        return
