#!/usr/bin/python3

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_start(self, data):
        self.size += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            my_iter = self.head
            while my_iter.next_node is not None:
                my_iter = my_iter.next_node
            my_iter.next_node = new_node
    
    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1
        my_iter = self.head
        if my_iter == self.head:
            self.head = self.head.next_node
        while my_iter.next_node is not None:
            if my_iter.next_node == data:
                my_iter = my_iter.next_node.next_node
                return
            else:
                my_iter = my_iter.next_node


    def out(self):
        my_iter = self.head
        while my_iter is not None:
            print(my_iter.data)
            my_iter = my_iter.next_node


hi = LinkedList()
hi.insert_at_end(4)
hi.insert_at_end(5)
hi.insert_at_start(1)
hi.insert_at_start(2)
hi.insert_at_start(3)
hi.remove(2)
hi.out()
