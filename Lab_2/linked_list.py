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

    def to_list(self) -> list:
        """
        The to_list function returns a list of the nodes in the linked list.
        The function returns a list of dictionaries, where each dictionary contains information about one node.

        :param self: Reference the object itself
        :return: A list of all the nodes in the linked list
        """
        linked_list = list()

        current_node = self.__head

        linked_list.append(current_node.__dict__)

        current_node = self.__head.next

        while current_node != self.__head:
            linked_list.append(current_node.__dict__)
            current_node = current_node.next
        return linked_list

    def get_by_measurement_limit(self, measurement_limit: float) -> list:
        """
        Returns list containing the information of all nodes in the linked list
        that have a measurement limit equal to the given parameter.
        If no such node exists, it returns the empty list.

        :param self: Access variables that belongs to the class
        :param measurement_limit:float: Specify the measurement limit of the items that will be returned in a list
        :return: A list of items that have the measurement limit specified in the function parameter
        """
        list_of_items = list()

        if self.__head.measurement_limit == measurement_limit:
            list_of_items.append(self.__head)

        current_node = self.__head.next

        while current_node != self.__head:
            if current_node.measurement_limit == measurement_limit:
                list_of_items.append(current_node)
            current_node = current_node.next

        return list_of_items

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
