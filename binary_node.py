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
    
    def pre_ordered(self,root,pre_ordered_list):
        pre_ordered_list=pre_ordered_list
        pre_ordered_list.append(root.data)
        if root.left!=None:
            self.pre_ordered(root.left,pre_ordered_list)
        if root.right!=None:
            self.pre_ordered(root.right,pre_ordered_list)
        return pre_ordered_list
    
    def inorder(self,root,ordered_list):
        ordered_list=ordered_list
        if root.left!=None:
            self.inorder(root.left,ordered_list)
        ordered_list.append(root.data)
        if root.right!=None:
            self.inorder(root.right,ordered_list)
        return ordered_list
    
    def post_order(self,root,post_order_list):
        post_order_list=post_order_list
        if root.left!=None:
            self.post_order(root.left,post_order_list)
        if root.right!=None:
            self.post_order(root.right,post_order_list)
        post_order_list.append(root.data)
        return post_order_list