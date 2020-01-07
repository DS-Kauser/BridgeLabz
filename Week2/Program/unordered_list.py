import sys
sys.path.append("/home/user/Desktop/BridgeLabz")
from Week2.Utility.utility import LinkedList

def create_linked_list(file_path):
    open_file = open(file_path, 'r')
    lst = LinkedList()
    for line in open_file:
        for word in line.split():
            lst.insert_end(word)
    open_file.close()
    return lst

def add_remove(word, lst):
    position = lst.pos(word)
    if position is not None:
        lst.del_at(position)
        return lst
    lst.insert_end(word)
    return lst

def rewrite(file_path, lst):
    open_file = open(file_path,'w')
    cur_node = lst.head
    while cur_node is not None:
        open_file.write("{0}\n".format(cur_node.data))
        cur_node = cur_node.next
    return

if __name__ == '__main__':
    file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/text_unordered.txt'
    word = input("Enter a word to search : ")
    lst = create_linked_list(file_path)
    lst = add_remove(word, lst)
    rewrite(file_path, lst)