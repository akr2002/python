class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextVal = None 

class SLinkedList:
    def __init__(self):
        self.headval = None 

    # Print
    def listPrint(self):
        printVal = self.headval 
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

    # Insert
    def AtBeginning(self, newData):
        NewNode = Node(newData);
        # Update the new node's nextVal to existing node
        NewNode.nextVal = self.headval 
        self.headval = NewNode
