#Create a node class below
class Node:
    def __init__(self, value, link_node='None'):
        self.value = value
        self.link_node = link_node
        
    def get_value(self):
        return self.value
    
    def get_link_node(self):
        return self.link_node
    
    def set_link_node(self, link_node):
        self.link_node = link_node
    
#Outside of Node, instantiate three nodes.
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

#yacko can keep track of dot and dot can keep up with wacko. wacko can’t keep track of anything though.
yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)

