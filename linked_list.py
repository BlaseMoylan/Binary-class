class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def add_node(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node 
            self.tail=new_node 
        else:
            self.tail.next=new_node
            self.tail=self.tail.next

    def find_node(self,value):
        current_node=self.head
        node=True
        while current_node:
            if current_node.value is value:
                return True
            else:
                current_node=current_node.next
        return False