#Importing the linked list
from LinkedList import *

#Creating Node instances
node_1 = Node("Chandler")
node_2 = Node("Monica")
node_3 = Node("Rachel")
node_4 = Node("Ross")

#Setting up links to next nodes
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

#Setting up linked list instance
linkedlist1 = LinkedList(node_1)

#1 Reading a value by index
print(linkedlist1.read(0))

#2 Finding the index of a value
print(linkedlist1.find_index("Rachel"))

#3 Inserting a new value

print("Previous value at index 0: ")
print(linkedlist1.read(0))
#Inserting
linkedlist1.insert_at_index(0, "Joey")
#Check if inserted
print("Current value at index 0: ")
print(linkedlist1.read(0))
print("Current value at index 1: ")
print(linkedlist1.read(1))

#4 Deleting a value

print("Value of index 3 before deletion: ")
print(linkedlist1.read(3))

#Deleting
linkedlist1.delete_at_index(3)

#Checking if deleted
print("Value of index 3 after deletion: ")
print(linkedlist1.read(3))

