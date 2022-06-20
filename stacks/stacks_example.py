# Node class
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value


# Building out the Stack class
class Stack:

    def __init__(self, limit = 1000):
        self.top_item = None
        self.size = 0
        self.limit = limit


    def push(self, value):
        if self.limit > self.size:
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print(f"Adding {value} to the stack!")
        else:
            print("All out of space, bud!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print(f"Placing down {item_to_remove.get_value()}")
            return item_to_remove.get_value()
        else:
            print("No more weights! This stack is completely empty, Hero.")
        
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to see here!")
    
    def has_space(self):
        if self.limit > self.size:
            return True
    
    def is_empty(self):
        if self.size == 0:
            return True 


# Defining an empty weight stack
weight_stack = Stack(6)

# Adding weights as they are ready until we have 
weight_stack.push("weight #1")
weight_stack.push("weight #2")
weight_stack.push("weight #3")
weight_stack.push("weight #4")
weight_stack.push("weight #5")
weight_stack.push("weight #6")


weight_stack.push("weight #7")

# Placing weights from the top of the stack down
print("The first weight to pop off is " + weight_stack.peek())
weight_stack.pop()
weight_stack.pop()
weight_stack.pop()
weight_stack.pop()
weight_stack.pop()
weight_stack.pop()
weight_stack.pop()