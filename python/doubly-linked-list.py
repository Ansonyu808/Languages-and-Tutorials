#!/usr/bin/python3


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_start(self, data):
        self.size += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            second_node = new_node.next_node
            second_node = self.head
            self.head = new_node
            new_node.next_node = second_node
            second_node.previous_node = new_node

    def insert_at_end(self, data):
        self.size += 1
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            second_node = new_node.previous_node
            second_node = self.tail
            self.tail = new_node
            new_node.previous_node = second_node
            second_node.next_node = new_node

    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1
        my_iter = self.head
        if data == my_iter.data:
            self.head = self.head.next_node
            self.head.previous_node = None
        elif data == self.tail.data:
            self.tail = self.tail.previous_node
            self.tail.next_node = None
        while my_iter.next_node is not None:
            if my_iter.next_node.data == data:
                my_iter.next_node = my_iter.next_node.next_node
                my_iter.next_node.previous_node = my_iter
                return
            else:
                my_iter = my_iter.next_node

    def out(self):
        forward = self.head
        backwards = self.tail
        while forward is not None:
            print(forward.data)
            forward = forward.next_node
        print()
        while backwards is not None:
            print(backwards.data)
            backwards = backwards.previous_node



list = LinkedList()
list.insert_at_end(3)
list.insert_at_end(4)
list.insert_at_start(2)
list.insert_at_start(1)
list.remove(4)
list.out()

#     def insert_at_end(self, data):
#         self.size += 1
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             my_iter = self.head
#             while my_iter.next_node is not None:
#                 my_iter = my_iter.next_node
#             my_iter.next_node = new_node
#     
# 
