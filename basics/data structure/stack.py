from node import Node:
    
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0
    
    #Define your push method here
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("Stack is empty or the stack is already full")
    
    #Define your pop method
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to see here")
    
    def has_space(self):
        if self.limit > self.size:
            return True
    
    def is_empty(self):
        if self.size == 0:
            return True
    