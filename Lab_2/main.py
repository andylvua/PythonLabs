from linked_list import CircularLinkedList
from node import Node


def main() -> None:
    linked_list = CircularLinkedList()

    linked_list.insert(Node("AX-122", "Voltmeter", 2000, 10)) \
        .insert(Node("BG-3", "Ammeter", 2010, 10)) \
        .insert(Node("JFD-32", "Voltmeter", 1985, 15)) \
        .insert(Node("S-12", "Multimeter", 1999, 10)) \
        .insert(Node("KL-768", "Multimeter", 2020, 60))

    items = linked_list.get_by_measurement_limit(15)

    for item in items:
        print(item)


if __name__ == '__main__':
    main()
