# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

# create an empty LinkedList class.

# Define an .__init__() method for the LinkedList. We want to be able to instantiate a LinkedList with a head node, so .__init__() should take value as an argument. Make sure value defaults to None if no value is provided.

# Inside the .__init__() method, set self.head_node equal to a new Node with value as its value.
class LinkedList:
    def __init__(self, value=None, ):
        self.head_node = Node(value) 
    
    def get_head_node(self):
        return self.head_node

# Define an .insert_beginning() method which takes new_value as an argument.

# Inside the method, instantiate a Node with new_value. Name this new_node.
# Now, link new_node to the existing head_node.
# Finally, replace the current head_node with new_node.
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
# Define a .stringify_list() method we can use to print out a string representation of a list’s nodes’ values.

# The method should traverse the list, beginning at the head node, and collect each node’s value in a string. Once the end of the list has been reached, the method should return the string.

# You can use str() to convert integers to strings!

# Be sure to add "\n" between values so that each value prints on a new line.

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value())+"\n"
            current_node.get_next_node()
        return string_list
    
#     At the bottom of script.py, add a .remove_node() method to LinkedList. It should take value_to_remove as a parameter. We’ll be looking for a node with this value to remove.

# In the body of .remove_node(), set a new variable current_node equal to the head_node of the list.

# We’ll use current_node to keep track of the node we are currently looking at as we traverse the list.
        
# ll = LinkedList(5)
# ll.insert_beginning(70)
# ll.insert_beginning(5675)
# ll.insert_beginning(90)
# print(ll.stringify_list())

# Still inside the method body, use an if statement to check whether the list’s head_node has a value that is the same as value_to_remove.

# If it does, we’ve found the node we’re looking for and we need to adjust the list’s pointer to head_node.

# Inside the if clause, set self.head_node equal to the second node in the linked list.

# Add an else clause. Within the else clause:

# Traverse the list until current_node.get_next_node().get_value() is the value_to_remove.

# (Just like with stringify_list you can traverse the list using a while loop that checks whether current_node exists.)

# When value_to_remove is found, adjust the links in the list so that current_node is linked to next_node.get_next_node().

# After you remove the node with a value of value_to_remove, make sure to set current_node to None so that you exit the loop.

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

                    