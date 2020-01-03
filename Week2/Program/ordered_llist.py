import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import node
from Week2.Utility.utility import ord_linked_list

if __name__ == '__main__':
    while True:
        try:

            file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/number.txt'


            list1 = ord_linked_list()
            f = open(file_path, 'r')
            for line in f:
                for num in line.split():
                    list1.list_add(int(num))
            f.close()
            
            number = int(input("Enter a number : "))
            position = list1.pos(number)
            if position is None:
                list1.list_add(number)
                
            else:
                list1.del_at(position)

            file_op = open(file_path,'w')
            cur_node = list1.head
            while cur_node is not None:
                file_op.write("{0}\n".format(cur_node.data)) 
                cur_node = cur_node.next
            file_op.close()
            break
    
        except:
            print("Invalid input")