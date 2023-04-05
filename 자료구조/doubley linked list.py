class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        res_str = "|"

        iterator = self.head
        while iterator:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str

    def find_node_at(self, index):
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        iterator = self.head
        result = None
        while iterator is not None:
            if iterator.data == data:
                result = iterator
                break
            iterator = iterator.next
        return result