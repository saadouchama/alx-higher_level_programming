#!/usr/bin/python3

"""Module that defines a Node class and a SinglyLinkedList class."""


class Node:
    """
    Node class for singly linked list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a Node.
        Args:
            data (int): data stored in node.
            next_node (Node): next node in singly linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data stored in the node.
        Args:
            value (int): data to be stored in the node.
        Raises:
            TypeError: data must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next node in the singly linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the singly linked list.
        Args:
            value (Node): next node in the singly linked list.
        Raises:
            TypeError: next_node must be a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.
    """

    def __init__(self):
        """Initializes a singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.
        Args:
            value (int): data stored in the Node.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None:
                if current.next_node.data > value:
                    break
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the singly linked list in a specific format.
        Returns:
            Formatted string representing the singly linked list.
        """
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]


if "__main__" == __name__:
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
