class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length or self.length == 0:
            return false
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
        else:
            prev = self.head
            for _ in range (index - 1):
                prev = prev.next
            temp = prev.next
            prev.next = temp.next
            temp = None
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        temp = self.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        return values
