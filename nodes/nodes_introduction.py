"""  
NODES INTRODUCTION --------------------------------------------------------->
In this example, the node's data will be specified when creating the node
and immutable. The link will be optional at initialization and can
be updated.

At the end of a node path, the link to the next node is null because there
are no more nodes left. In Python, this means it's set to None
"""

# Create the Node class below:
class Node:
  
  def __init__(self, value, link_node = None):
    self.value = value
    self.link_node = link_node




