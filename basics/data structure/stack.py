from node import Node:
    
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.limit = limit
        self.size = 0
    
    #Define your push method here
    def push(self, value):
        if self.size > 0 and self.size < self.limit:
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
        else:
            print("Stack is empty or the stack is already full")
    
    #Define your pop method
    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            return item_to_remove.get_value()
        else:
            print("Stack is empty")
    
    def peek(self):
        return self.top_item.get_value()