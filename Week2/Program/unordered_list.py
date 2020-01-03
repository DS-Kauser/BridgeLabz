import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import node
from Week2.Utility.utility import unord_linked_list


if __name__ == '__main__':
    while True:
        try:
            file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/text.txt'

            open_file = open(file_path, 'r')

            list1 = unord_linked_list()
            for line in open_file:
                for word in line.split():
                    list1.insert_end(word)
            open_file.close()
            #l1.print_list()
            word = input("Enter the word to search : ")
            word_pos = list1.pos(word)

            if word_pos is None:
                list1.insert_end(word)
                filew = open(file_path, 'a')
                filew.write('{0}\n'.format(word))

            else:
                list1.del_at(word_pos)
                open_file = open(file_path, 'w')
                cur_node = list1.head
                while True:
                    if cur_node is None:
                        open_file.close()
                        break
                    open_file.write('{0}\n'.format(cur_node.data))
                    cur_node = cur_node.next
            break
        
        except:
            print("Enter a valid input")