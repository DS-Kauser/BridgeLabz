"""
 ******************************************************************************
 *  Purpose: utils for data structure program
 *
 *  @author  Md Kauser Ansari
 *  @version 3.7
 *  @since   20/12/2019
 ******************************************************************************
"""

"""
adding a node class
creates node with data and refrence to next node
"""
class node():
    def __init__(self, data):
        self.data = data
        self.next = None


"""
creating a class linked_list
adding different method to it
"""

class linked_list():
    def __init__(self):
        self.head = None

    
    def list_len(self):
        length = 0
        curr_node = self.head
        while curr_node is not None:
            length += 1
            curr_node = curr_node.next
        return length

    
    def insert_end(self, new_data):
        new_node = node(new_data)
        
        if self.head is None:
            self.head = new_node
        
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

            
    def insert_head(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
            del temp_node
        
    
    def print_list(self):
        if self.head is None:
            print("list is empty")
        
        else:
            curr_node = self.head
            while True:
                               
                print(curr_node.data)
                curr_node = curr_node.next
                if curr_node is None:
                    break