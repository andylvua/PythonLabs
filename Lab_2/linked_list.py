from __future__ import annotations

from node import Node


class CircularLinkedList:
    def __init__(self) -> None:
        """
        Called automatically every time the class CircularLinkedList is
        instantiated. It sets the head value to None

        :param self: Refer to the object itself
        :return: The object that was created
        """
        self.__head = None

    def print_info(self, measurement_limit: float) -> None:
        """
        Prints the information of all nodes in the linked list
        that have a measurement limit equal to the given parameter.
        If no such node exists, it prints an error message.

        :param self: Access the attributes and methods of the class
        :param measurement_limit: float: Specify the measurement limit of the nodes that are printed
        """
        present = False

        if self.__head.measurement_limit == measurement_limit:
            print(self.__head)
            present = True

        current_node = self.__head.next

        while current_node != self.__head:
            if current_node.measurement_limit == measurement_limit:
                print(current_node)
                present = True
            current_node = current_node.next

        if not present:
            print("Error: nothing's found")

    def insert(self, inserting_node: Node) -> CircularLinkedList:
        """
        Takes a node as an argument and inserts it into the linked list.
        If the head of the list is None, then we set that node to be both head and tail.
        If inserting_node's manufacture year is less than head's manufacture year,
        then we insert it at as the head node.
        If inserting_node's manufacture year is greater than head's manufacture year,
        then we insert it at the last position.
        Otherwise, inserting_node's is being inserted between the current_node and the current_node.next
        at the appropriate position

        :param self: Reference the class instance
        :param inserting_node: Node: Specify the node that is going to be inserted
        :return: CircularLinkedList object
        """
        if self.__head is None:
            self.__head = inserting_node
            inserting_node.next = inserting_node
            return self

        current_node = self.__head

        if inserting_node.manufacture_year < self.__head.manufacture_year:
            while current_node.next != self.__head:
                current_node = current_node.next
                continue
            current_node.next = inserting_node
            inserting_node.next = self.__head
            self.__head = inserting_node
            return self

        while current_node.next != self.__head:
            if inserting_node.manufacture_year < current_node.next.manufacture_year:
                inserting_node.next = current_node.next
                current_node.next = inserting_node
                break
            current_node = current_node.next
        else:
            current_node.next = inserting_node
            inserting_node.next = self.__head

        return self
