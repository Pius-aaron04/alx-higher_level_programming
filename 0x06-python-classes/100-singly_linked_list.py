#!/usr/bin/python3
"""
This Module contains definition of Node and SinglyLinkedLists classes.
Author - Pius Aaron
"""


class Node:
    """
    This is a Node class that stores an integer.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes node attributes.
        """

        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def data(self):
        """
        Retrieves the data of the node.
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets or updates the data of node.
        """

        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node.
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets or updates the next_node attribute.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This is a singly linked list class.
    """

    def __init__(self):
        """
        intiailizes the linked list attributes.
        """

        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts or adds a node to the list in ascending order.
        """

        head = self.__head
        new_node = Node(value)

        if head is None:
            self.__head = new_node
            return

        current = self.__head
        next_ = current.next_node
        if value < current.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        while next_:
            if value < next_.data:
                new_node.next_node = next_
                current.next_node = new_node
                return
            current = next_
            next_ = next_.next_node
        current.next_node = new_node

    def __repr__(self):
        """
        String representation of linked list object.
        """

        rep = ""
        node = self.__head

        while node:
            if node.next_node is not None:
                rep += str(node.data) + '\n'
            else:
                rep += str(node.data)
            node = node.next_node
        return rep
