from doubly_linked_list import DoublyLinkedList


class RingBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):

        index = self.current % self.capacity

        if index < self.capacity:

            node = self.storage.head

            # move the the node at `index`
            for __ in range(index):
                node = node.next

            # if the node exists, replace its value
            if node:
                node.value = item

            # else, add a new node
            else:
                self.storage.add_to_tail(item)

            self.current += 1

        else:
            # can't do anything
            pass

    def get(self):

        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


############################################################
#   STRETCH
############################################################


class ArrayRingBuffer:

    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
