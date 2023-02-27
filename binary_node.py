# from linked_list import Node

class BinaryNode:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
class TreeNode:
    def __init__(self) -> None:
         self.root=None
         #self.parent_node=None
    def insert_node(self,parent_node,value):
        if parent_node==None:
            self.root=BinaryNode(value)
            #self.parent_node=BinaryNode(value)
            print(f'node with data {value} created')
        else:
            if value<parent_node.data:
                if parent_node.left==None:
                    parent_node.left=BinaryNode(value)
                    print(f'node with data {value} created')
                    print(f'node {parent_node.data} updated with left of {self.left_right_checker(parent_node.left)} and a right of {self.left_right_checker(parent_node.right)}')
                else:
                    #parent_node=parent_node.left
                    self.insert_node(parent_node.left,value)
            else:
                if parent_node.right==None:
                    parent_node.right=BinaryNode(value)
                    print(f'node with data {value} created')
                    print(f'node {parent_node.data} updated with left of {self.left_right_checker(parent_node.left)} and a right of {self.left_right_checker(parent_node.right)}')
                else:
                    #parent_node=parent_node.right
                    self.insert_node(parent_node.right,value)
    def left_right_checker(self,value):
        if value==None:
            return"None"
        else:
            return value.data
        
    def search_for_node(self,value):
        pass