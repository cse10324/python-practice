from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    #inserting element into the queue
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding "+str(item_to_add.get_value())+ " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
    
    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")
    
    def get_size(self):
        return self.size
    
    def has_space(self):
        return self.size == 0
    