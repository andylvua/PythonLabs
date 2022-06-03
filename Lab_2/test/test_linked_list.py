import pytest

from Lab_2.linked_list import CircularLinkedList
from Lab_2.node import Node


@pytest.fixture
def circular_linked_list():
    linked_list = CircularLinkedList()

    linked_list.insert(Node("AX-122", "Voltmeter", 2000, 10)) \
        .insert(Node("BG-3", "Ammeter", 2010, 10)) \
        .insert(Node("JFD-32", "Voltmeter", 1985, 15)) \
        .insert(Node("S-12", "Multimeter", 1999, 10)) \
        .insert(Node("KL-768", "Multimeter", 2020, 60))

    return linked_list


def test_insertion():
    linked_list = CircularLinkedList()

    linked_list.insert(Node("AX-122", "Voltmeter", 2000, 10))

    to_list = linked_list.to_list()

    assert to_list
    assert isinstance(to_list[0]["next"], Node)


def test_nodes(circular_linked_list):
    to_list = circular_linked_list.to_list()

    for item in to_list:
        assert isinstance(item["next"], Node)


def test_order(circular_linked_list):
    to_list = circular_linked_list.to_list()

    list_of_manufacture_years = list()

    for item in to_list:
        list_of_manufacture_years.append(item["manufacture_year"])

    assert list_of_manufacture_years == sorted(list_of_manufacture_years)


def test_measurement_limit(circular_linked_list):
    limit = 10
    items = circular_linked_list.get_by_measurement_limit(measurement_limit=limit)

    set_of_manufacture_years = set()

    for item in items:
        set_of_manufacture_years.add(item.measurement_limit)

    assert len(set_of_manufacture_years) == 1
    assert limit in set_of_manufacture_years
