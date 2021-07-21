class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nestVal = None 

class SLinkedList:
    def __init__(self):
        self.headval = None 

    def listPrint(self):
        printVal = self.headval 
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal
