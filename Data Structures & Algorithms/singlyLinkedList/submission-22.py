class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next #dummy node points to first node
        count = 0
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current = self.head
        count = 0

        while count < index and current:
            current = current.next
            count += 1
        
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        count = 0
        arr = []

        while current:
            arr.append(current.val)
            current = current.next
            count += 1
        return arr


# [-1]->/ [5]->[2]->[1]->[3]->[4]


        
