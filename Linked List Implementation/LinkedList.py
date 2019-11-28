#Importing the node class
from Node import *


class LinkedList():
    first_node = "" #Initializing first_node

    def __init__(self, first_node):
        self.first_node = first_node

    #Reading the value at a provided index (Find value)
    def read(self, index):
        read_node = "Node does not exist"
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index+=1
        if current_node is not "":
            read_node = current_node.data
        return read_node

    #Find the index of a value (Search operation)
    def find_index(self, search_data):
        index = "Data does not exist in the Linked List"
        current_node = self.first_node
        current_index = 0
        while current_node.next_node is not "":
            if current_node.data == search_data:
                index = current_index
                break
            else:
                current_node = current_node.next_node
                current_index+=1
        return index

    #Inserting a value in the list at specified position
    def insert_at_index(self, index, insert_data):
        current_node = self.first_node
        current_index = 0
        if index == 0: #In case of inserting to the beginning of the array
            new_node = Node(insert_data)
            new_node.next_node = current_node
            self.first_node = new_node #Sets the new node as the first node of the linked list
        else:
            while current_index < index-1: #All other cases
                current_node = current_node.next_node
                current_index+=1
            new_node = Node(insert_data)
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
        return

    #Deleting a node at a specific index
    def delete_at_index(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index-1:
            current_node = current_node.next_node
            current_index+=1
        node_after_deleted_node = current_node.next_node.next_node
        current_node.next_node = node_after_deleted_node
        return
