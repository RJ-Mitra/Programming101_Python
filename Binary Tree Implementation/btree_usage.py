from TreeNode import *

node1 = TreeNode(1)
node10 = TreeNode(10)
root = TreeNode(5, node1, node10)


def search(value, node):
    if node is None or node.value == value:
        return node
    elif node.value < value:
        return search(value, node.right)
    else:
        return search(value, node.left)


def insert(value, node):
    if value < node.value:      #If value already exists (value == node.value), then no need to insert it again
        if node.left is None:   #If no node exists to the left, add it
            node.left = TreeNode(value)
        else:                   #If a node exists to the left, recurse one level down to add to proper position
            insert(value, node.left)
    elif value > node.value:
        if node.right is None:
            node.right = TreeNode(value)
        else:
            insert(value, node.right)



def lift(node, nodeToDelete):
    if node.left: #if node exists to the left
        node.left = lift(node.left, nodeToDelete) #recurse down till no nodes exist to the left
        return node
    else:
        nodeToDelete.value = node.value # if node has hanging right child, plugs that right child in place of deleted node
        return node.right #makes it new value of the node being deleted


def delete(value, node):
    if node is None: #Base case
        return None
    elif value < node.value: #Goes to left child of root
        node.left = delete(value, node.left)
        return node
    elif value > node.value: #Goes to right child of root
        node.right = delete(value, node.right)
        return node
    elif value == node.value: #Node to delete is found (#If it has no left or right child, it is handled by base case)
        if node.left is None: #If it has no left child, return right child and its sub-tree
            return node.right
        elif node.right is None: #If it has no right child, return left child and its sub-tree
            return node.left
        else:#Has both left and right child
            node.right = lift(node.right, node) #If current node has both left and right child, lift function changes current node value to that of its successor node
    return node

print(insert(10, root))
print(search(10, root))