"""
 ******************************************************************************
 *  Purpose: utils for data structure program
 *
 *  @author  Md Kauser Ansari
 *  @version 3.7
 *  @since   20/12/2019
 ******************************************************************************
"""

from math import sqrt

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

    def pos(self, element):
        if self.head is None:
            print("List is empty")
            return
        
        else:
            pos = 0
            cur_node = self.head
            while True:
                
                if cur_node.data == element:
                    return pos
                    break
                
                elif cur_node.next == None:
                    return None
                    break

                cur_node = cur_node.next
                pos += 1
    

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
        
    
    def insert_at(self, new_data, position):
        if position < 0 or position >= self.list_len():
            print("Enter a valid input")
            return 

        elif position == 0:
            self.insert_head(new_data)
            return
        
        else:
            new_node = node(new_data)
            cur_node = self.head
            cur_pos = 0
            while True:
                if cur_pos == position:
                    pre_node.next = new_node
                    new_node.next = cur_node
                    break
                pre_node = cur_node
                cur_node = cur_node.next
                cur_pos += 1

    
    def del_head(self):
        if self.head is not None:
            temp_node = self.head
            self.head = self.head.next
            temp_node.next = None
        else:
            print("linked list is empty")
            
    
    def del_end(self):
        if self.head is not None:
            last_node = self.head
            if self.list_len() == 1:
                self.head = None
            else:
                while True:
                    if last_node.next == None:
                        pre_node.next = None
                        break
                    
                    pre_node = last_node
                    last_node = last_node.next
        else:
            print("list is empty")   


    def del_at(self, position):
        if position < 0 or position >= self.list_len():
            print("Enter a valid position")
            return 

        elif position == 0:
            self.del_head()
            return 

        else:
            if self.head is not None:
                cur_node = self.head
                cur_pos = 0
                while True:
                    if cur_pos == position:
                        pre_node.next = cur_node.next
                        cur_node.next = None
                        break
                    pre_node = cur_node
                    cur_node = cur_node.next
                    cur_pos += 1
            
            else:
                print("list is empty")


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



class ord_linked_list(linked_list):
    def __init__(self):
        self.head = None

    
    def list_sort(self):
        
        success = True
        while success:
            success = False
            pre_node = self.head
            cur_node = pre_node.next
            
            while cur_node is not None:
                if pre_node.data > cur_node.data:
                    pre_node.data, cur_node.data = cur_node.data, pre_node.data
                    success = True
                
                pre_node = cur_node
                cur_node = cur_node.next

    
    def sort_add(self, element):
        new_node = node(element)
        if self.head is None:
            self.head = new_node
        
        else:
            cur_node = self.head
            while cur_node is not None:
                if cur_node.data > new_node.data and cur_node is self.head:
                    self.insert_start(element)
                    break
                elif cur_node.data > new_node.data:
                    pre_node.next = new_node
                    new_node.next = cur_node
                    break
                
                pre_node = cur_node
                cur_node = cur_node.next
                
            if cur_node is None:
                pre_node.next = new_node
                    
    
    def del_val(self, value):
        
        if self.head is not None:
            
            cur_node = self.head
            while cur_node is not None:
                
                if self.head.data == value:
                    self.head = self.head.next
                    break
                else:
                    if cur_node.data == value:
                        pre_node.next = cur_node.next
                        cur_node.next = None
                        del cur_node
                        break
                pre_node = cur_node
                cur_node = cur_node.next
                
    

class stack(linked_list):

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        return self.list_len()

    def push(self, element):
        self.insert_head(element)

    def pop(self):
        self.del_head()
    
    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            return None



class queue(linked_list):

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def enqueue(self, item):
        self.insert_end(item)

    def dequeue(self):
        self.del_head()

    def size(self):
        return self.list_len()



class deque(linked_list):
    
    def add_front(self, item):
        self.insert_end(item)

    def add_rear(self, item):
        self.insert_head(item)

    def del_front(self):
        self.del_end()

    def del_rear(self):
        self.del_front()
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        return self.list_len()



def prime(start, end):
    if start == end:
        return []
    
    elif start < end and end == 2:
        return [2]
    
    elif end > start and start >= 0 and end >= 2:
        prime_list = []
        number = start
        #print(type(end))
        while True:
            if number > end:
                break
            #print('again')
            if number == 1:
                number += 1
                continue

            count = 0
            for i in range(2, int(sqrt(number))+1, 1):
                if number%i == 0:
                    count += 1
                
            if count == 0: 
                prime_list.append(number)
            #print(prime_list)
            number = number + 1
        return prime_list
    
    else:
        return []
