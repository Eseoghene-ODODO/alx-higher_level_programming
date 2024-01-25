#!/usr/bin/python3
"""
A class Node that defines a node of a singly linked list
"""


class Node:
    """ class body """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        # Initialize head to None on creation
        self.head = None

    def __str__(self):
        values = []
        node = self.head
        # Traverse list and collect string representation of each data
        while node:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        # Create new node with given value
        new_node = Node(value)
        # Special case for empty list or insert at head
        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            # Find insert position that maintains sort order
            while (current.next_node is not None and
                   current.next_node.data < new_node.data):
                current = current.next_node
            # Insert new node
            new_node.next_node = current.next_node
            current.next_node = new_node
