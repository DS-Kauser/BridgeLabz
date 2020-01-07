import sys
sys.path.append("/home/user/Desktop/BridgeLabz")
from Week2.Utility.utility import linked_list

def create_hash(file_path):
    dic = dict()
    for i in range(11):
        dic[i] = linked_list()
    file_op1 = open(file_path, 'r')
    for line in file_op1.readlines():
        for num in line.split():
            pass_in_slot = int(num)%11
            dic[pass_in_slot].insert_end(int(num))
    file_op1.close()
    return dic

def add_remove(dic, number):
    for slot in dic:
        position = dic[slot].pos(number)
        if position is not None:
            dic[slot].del_at(position)
            print("Removed from the data")
            return dic
    pass_in_slot = number%11
    dic[pass_in_slot].insert_end(number)
    print("Added to the data")
    return dic

def rewrite(file_path, dic):
    file_op = open(file_path,'w')
    for slot in dic:
        cur_node = dic[slot].head
        while cur_node is not None:
            file_op.write("{0}\n".format(cur_node.data))
            cur_node = cur_node.next
    return

def search_hash(number,file_path):
    dic = create_hash(file_path)
    dic = add_remove(dic, number)
    rewrite(file_path, dic)

if __name__ == "__main__":
    try:
        #file_path = input("Give file path location :")
        file_path = file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/hasing_number.txt'
        number = int(input("Enter your number : "))
        search_hash(number, file_path)
    except:
        print("Invalid Input")