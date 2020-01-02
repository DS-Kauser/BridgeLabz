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
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
creating a class linked_list
adding different method to it
"""

class linked_list:
    def __init__(self):
        self.head = None