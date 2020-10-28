# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, inorder(root.right))

    # A utility function to insert a new node with given key in BST


def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

        # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

        # return the (unchanged) node pointer
    return node


# Given a non-empty binary search tree, return the node
# with minum key value found in that tree. Note that the
# entire tree does not need to be searched
def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

            # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


# Driver program to test above functions
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("\nInorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("\nInorder traversal of the modified tree")
inorder(root)


# def delete(self, key, root=None):
#     if root is None:
#         root = self._root
#     if root is None:
#         return None
#
#     if key.value < root.value:
#         root.left = self.delete(key, root.left)
#     elif key.value > root.value:
#         root.right = self.delete(key, root.right)
#     else:
#         if root.left is None:
#             tempTree = root.right
#             root.value = None
#             return tempTree
#         elif root.right is None:
#             tempTree = root.left
#             root.value = None
#             return tempTree
#
#         tempTree = self.findLeftMost(root.right)
#         root.value = tempTree.value
#         root.right = self.delete(tempTree.value, root.right)
#
#     return root

# def delete(self, key, root=None):
#     if root is None:
#         root = self._root
#     if root is None:
#         return None
#
#     if key.value < root.value:
#         root.left = self.delete(key, root.left)
#     elif key.value > root.value:
#         root.right = self.delete(key, root.right)
#     else:
#         if root.left is None:
#             tempTree = root.right
#             root.value = None
#             return tempTree
#         elif root.right is None:
#             tempTree = root.left
#             root.value = None
#             return tempTree
#
#         tempTree = self.findLeftMost(root.right)
#         root.value = tempTree.value
#         root.right = self.delete(tempTree.value, root.right)
#
#     return root


def delete(self, key, root=None):
    if root is None:
        root = self._root
    if root is None:
        return None

    parent = self._root
    current = parent

    if key.value < root.value:
        parent = current
        current = parent.left
        root.left = self.delete(key, root.left)
    elif key.value > root.value:
        parent = current
        current = parent.right
        root.right = self.delete(key, root.right)
    else:
        import copy
        node = current
        delnode = copy.copy(node)
        # If node has no children, we need to update the parent reference
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            if parent.right == node:
                parent.right = None
            if node == self._root:
                self._root = None
            node = None
        elif node.right:
            if node.right.left is None:
                node.value = node.right.value
                node.right = node.right.right
            else:
                temptree = BinaryTree(node.right)
                mintempnode = temptree.deleteMin()
                node.value = mintempnode.value
        elif node.left:
            if parent.left == node:
                parent.left = node.left
            elif parent.right == node:
                parent.right = node.left

    return root

'''  
# Gammel kode

def delete(self, key):
    #
    # Finding node ... with parent reference ...
    # Need the parent reference to update tree references
    parent = self._root
    current = parent
    while True:
        if key < current.value:
            parent = current
            current = parent.left
        elif key > current.value:
            parent = current
            current = parent.right
        elif key == current.value:
            node = current
            break
        else:
            return None
    # using a shallow copy of the original node to maintain deleted node while reassigning it
    import copy
    delnode = copy.copy(node)
    # If node has no children, we need to update the parent reference
    if not node.left and not node.right:
        if parent.left == node:
            parent.left = None
        if parent.right == node:
            parent.right = None 
        if node == self._root:
            self._root = None               
        node = None
    elif node.right:
        if node.right.left is None:
            node.value = node.right.value 
            node.right = node.right.right
        else: 
            temptree = BinaryTree(node.right)
            mintempnode = temptree.deleteMin()
            node.value = mintempnode.value
    elif node.left:
        if parent.left == node:
            parent.left = node.left
        elif parent.right == node:
            parent.right = node.left  
    return delnode    
    '''