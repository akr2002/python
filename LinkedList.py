class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextVal = None 

class SLinkedList:
    def __init__(self):
        self.headval = None 

    # Print
    def printList(self):
        printVal = self.headval 
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

    # Insert at beginning
    def atBeginning(self, newData):
        NewNode = Node(newData);
        # Update the new node's nextVal to existing node
        NewNode.nextVal = self.headval 
        self.headval = NewNode

    # Insert at end
    def atEnd(self, newData):
        NewNode = Node(newData)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while (last.nextVal):
            last = last.nextVal
        last.nextVal = NewNode
