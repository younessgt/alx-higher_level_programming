#!/usr/bin/python3
""" creating a class called Node that defines node of
singly linked lisid"""


class Node:
    """ Class Node is created """

    def __init__(self, data, next_node=None):
        """ Inisilizing data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retriving data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setting data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ retriving the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setting the next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ defining a singly linked list"""

    def __init__(self):
        """Initizing the linked list"""
        self.__head = None

    def __str__(self):
        """ override the string and make it print
        the data of linked list"""
        string_linked_list = ""
        temp = self.__head
        while temp.next_node is not None:
            string_linked_list += str(temp.data) + "\n"
            temp = temp.next_node
        string_linked_list += str(temp.data)
        return string_linked_list

    def sorted_insert(self, value):
        """creation a sorted singly linked list"""
        new = Node(value)
        """checking if the head in None"""
        if self.__head is None:
            self.__head = new
            return
        else:
            """sorting the data"""
            temp = self.__head
            if (temp.data > new.data):
                new.next_node = self.__head
                self.__head = new
                return
            while temp.next_node is not None\
                    and temp.next_node.data < new.data:
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new
            return
