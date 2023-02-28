# from linked_list import Node

# class BinaryNode:
#     def __init__(self,data) -> None:
#         self.left=None
#         self.right=None
#         self.data=data
# class TreeNode:
#     def __init__(self) -> None:
#         self.root=None
        
#     def insert_node(self,parent_node,value):
#         if parent_node==None:
#             self.root=BinaryNode(value)
#             print(f'node with data {value} created')
#         else:
#             if value<parent_node.data:
#                 if parent_node.left==None:
#                     parent_node.left=BinaryNode(value)
#                     print(f'node with data {value} created')
#                     print(f'node {parent_node.data} updated with left of {self.left_right_checker(parent_node.left)} and a right of {self.left_right_checker(parent_node.right)}')
#                 else:
#                     self.insert_node(parent_node.left,value)
#             else:
#                 if parent_node.right==None:
#                     parent_node.right=BinaryNode(value)
#                     print(f'node with data {value} created')
#                     print(f'node {parent_node.data} updated with left of {self.left_right_checker(parent_node.left)} and a right of {self.left_right_checker(parent_node.right)}')
#                 else:
#                     self.insert_node(parent_node.right,value)
#     def left_right_checker(self,value):
#         if value==None:
#             return"None"
#         else:
#             return value.data

#     #need more testing

#     def search_for_node(self,value):
#         if value==self.root:
#             pass
#         if self.root.right==None or self.root.left==None:
#             print('not found')
#         else:
#             if value<self.root.data:
#                 if value!=self.root.left.data:
#                     self.root=self.root.left
#                     self.search_for_node(value)
#                 else :
#                     print('found')
#             else :
#                 if value!=self.root.right.data:
#                     self.root=self.root.right
#                     self.search_for_node(value)
#                 else:
#                     print('found')

class BinaryNode:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
        self.root=None
    def pre_order(self,list_of_values):
        for item in list_of_values:
            self.insert_node(item)
    def ordered(self,list_of_values):
        values_list=list_of_values.sort()
        for item in values_list:
            self.insert_node(item)
    def insert_node(self,value):
        if value==self.data:
            print(f'node with data {value} created')
        elif value<self.data:
            if self.left==None:
                self.left=BinaryNode(value)
                print(f'node with data {value} created')
                print(f'node {self.data} updated with left of {self.left_right_checker(self.left)} and a right of {self.left_right_checker(self.right)}')
            else:
                self.left.insert_node(value)
        else:
            if self.right==None:
                self.right=BinaryNode(value)
                print(f'node with data {value} created')
                print(f'node {self.data} updated with left of {self.left_right_checker(self.left)} and a right of {self.left_right_checker(self.right)}')
            else:
                self.right.insert_node(value)
    def left_right_checker(self,value):
        if value==None:
            return"None"
        else:
            return value.data

    #need more testing

    def search_for_node(self,value):
        if self.right==None or self.left==None:
            print('not found')
        else:
            if value<self.data:
                print('direction: left')
                if value!=self.left.data:
                    self.left.search_for_node(value)
                else :
                    print('found')
            else :
                print('direction: right')
                if value!=self.right.data:
                    self.right.search_for_node(value)
                else:
                    print('found')