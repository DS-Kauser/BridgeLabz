import sys
sys.path.append("/home/user/Desktop/BridgeLabz")
from Week2.Utility.utility import node
from Week2.Utility.utility import ord_linked_list

def create_ord_list(file_path):
    lst = ord_linked_list()
    file_op = open(file_path, 'r')
    for line in file_op.readlines():
        for num in line.split():
            lst.sort_add(int(num))
    file_op.close()
    return lst

def add_remove(lst, number):
    position = lst.pos(number)
    if position is not None:
        lst.del_at(position)
        print("Removed from the data")
        return lst
    lst.sort_add(number)
    print("Added to the data")
    return lst

def rewrite(file_path,lst):
    #lst.print_list()
    file_op = open(file_path, 'w')
    cur_node = lst.head
    while cur_node is not None:
        file_op.write("{0}\n".format(cur_node.data))
        cur_node = cur_node.next
    return

if __name__ == '__main__':
    try:
        #file_path = input("Give your file location : ")
        file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/number.txt'
        number = int(input("Enter number to search : "))
        ord_list = create_ord_list(file_path)
        ord_list = add_remove(ord_list, number)
        rewrite(file_path, ord_list)
    except:
        print("check your input")