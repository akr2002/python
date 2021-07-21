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

    # Insert between two nodes
    def inBetween(self, middleNode, newData):
        if middleNode is None:
            print("The mentioned node is absent")
            return 

        NewNode = Node(newData)
        NewNode.nextVal = middleNode.nextVal 
        middleNode.nextVal = NewNode

    # Remove a node
    def removeNode(self, removeKey):
        headval = self.headval 

        if headval is not None:
            if headval.dataVal = removeKey:
                self.headval = headval.nextVal
                headval = None
                return

        while headval is not None:
            if headval.dataVal == removeKey:
                break 
            prev = headval
            headval = headval.nextVal

        if headval == None:
            return

        prev.nextVal = headval.nextVal
        headval = none
