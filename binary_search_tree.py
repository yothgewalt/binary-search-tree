# Author: Yongyuth Chuankhuntod

class BinaryTree:
    """BinaryTree class that contains method for create a binary tree.

    Returns:
        `insert_node(value: int)`: for insert node into our binary tree with value parameter.\n
        `delete_node(value: int)`: for delete node in our binary tree with value parameter for refernece to delete.\n
        `inorder_traversal()`: for display in each node and format display `inorder`\n
        `preorder_traversal()`: for display in each node and format display `preorder`\n
        `postorder_traversal()`: for display in each node and format display `postorder`\n
        
    """
    
    class Node:
        """Node class for definition a tree node.
        
        Cons:
            `key (int)`: The key is a value that contain on node.
        """
        
        
        def __init__(self, key: int) -> None:
            self.value: int = key
            self.left_child = None
            self.right_child = None
            
    
    def __init__(self) -> None:
        self.root = None
        
        
    def insert_node(self, value: int) -> None:
        """A method that allow to insert node into our binary tree.

        Args:
            `value (int)`: The value is mean a value of node that's contain in tree node.
        """
        
        
        new_node = BinaryTree.Node(key=value)
        if not self.root:
            self.root = new_node
            
        else:
            target = self.root
            
            while True:
                if value < target.value:
                    if not target.left_child:
                        target.left_child = new_node
                        return
                    
                    target = target.left_child
                    
                else:
                    if not target.right_child:
                        target.right_child = new_node
                        return
                    
                    target = target.right_child
                    
    
    def delete_node(self, value: int) -> bool:
        """A method that allow to delete node in binary tree.

        Args:
            `value (int)`: for target to delete that reference by value parameter.

        Returns:
            `bool`: return boolean variable for implementation outer class.
        """
        
        
        if not self.root:
            return False
        
        # Find the node to be deleted and its parent
        parent = None
        target = self.root
        
        while target and target.value != value:
            parent = target
            if value < target.value:
                target = target.left_child
                
            else:
                target = target.right_child
                
        if not target:
            return False
        
        # Case 1: Node to be deleted has no children
        if (not target.left_child) and (not target.right_child):
            if target != self.root:
                if parent != self.root:
                    if parent.left_child == target:
                        parent.left_child = None
                        
                    else:
                        parent.right_child = None
                
                else:
                    self.root = None
        
        # Case 2: Node to be deleted has one child
        elif (not target.left_child) or (not target.right_child):
            if target.left_child:
                child = target.left_child
                
            else:
                child = target.right_child
            
            if target != self.root:
                if parent.left_child == target:
                    parent.left_child = child
                    
                else:
                    parent.right_child = child
                    
            else:
                self.root = child
        
        # Case 3: Node to be deleted has two children
        else:
            # Find the inorder successor (leftmost child of right subtree)
            parent = target
            successor = target.right_child
            
            while successor.left_child:
                parent = successor
                successor = successor.left_child
                
            # Replace the node to be deleted with the inorder successor
            target.value = successor.value
            
            # Delete the inorder successor node
            if parent.left_child == successor:
                parent.left_child = successor.right_child
                
            else:
                parent.right_child = successor.right_child
                
        return True
    
    
    def _inorder(self, node: Node) -> list[int]:
        """A format display in binary tree that called `inorder`

        Args:
            `node (Node)`: A collection of number that contain in binary tree.

        Returns:
            `list[int]`: return list (contains integer) variable for implementation outer class.
        """
        
        
        if not node:
            return []
        
        result = self._inorder(node.left_child)
        result.append(node.value)
        result += self._inorder(node.right_child)
        
        return result
    
    
    def _preorder(self, node: Node) -> list[int]:
        """A format display in binary tree that called `preorder`

        Args:
            `node (Node)`: A collection of number that contain in binary tree.

        Returns:
            `list[int]`: return list (contains integer) variable for implementation outer class.
        """
        
        
        if not node:
            return []
        
        result = [node.value]
        result += self._preorder(node.left_child)
        result += self._preorder(node.right_child)
        
        return result
    
    
    def _postorder(self, node: Node) -> list[int]:
        """A format display in binary tree that called `postorder`

        Args:
            `node (Node)`: A collection of number that contain in binary tree.

        Returns:
            `list[int]`: return list (contains integer) variable for implementation outer class.
        """
        
        
        if not node:
            return []
        
        result = self._postorder(node.left_child)
        result += self._postorder(node.right_child)
        result.append(node.value)
        
        return result
    
    
    def inorder_traversal(self):
        """A method that implement from private method that can format display that's `inorder`

        Returns:
            `_inorder()`: that called private method to display with format inorder.
        """
        
        
        return self._inorder(self.root)
    
    
    def preorder_traversal(self):
        """A method that implement from private method that can format display that's `preorder`

        Returns:
            `_preorder()`: that called private method to display with format preorder.
        """
        
        
        return self._preorder(self.root)
    
    
    def postorder_traversal(self):
        """A method that implement from private method that can format display that's `postorder`

        Returns:
            `_postorder()`: that called private method to display with format postorder.
        """
        
        
        return self._postorder(self.root)
    
    
if __name__ == "__main__":
    tree = BinaryTree()
    
    numeric_nodes: list[int] = [
        5, 3, 7, 1, 9, 10, 8,
        12, 20, 14, 17, 16, 15
    ]
    for numeric in numeric_nodes:
        tree.insert_node(numeric)
    
    print("\nInorder Traversal:")
    print(tree.inorder_traversal())
    
    tree.delete_node(17)
    
    print("\nPreorder Traversal:")
    print(tree.preorder_traversal())
    
    tree.delete_node(16)
    
    print("\nPostorder Traversal:")
    print(tree.postorder_traversal(), end="\n\n")
