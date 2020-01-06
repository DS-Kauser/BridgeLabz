import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

#from Week2.Utility.utility import node
from Week2.Utility.utility import linked_list

def search_hash(number):
    try:
        dic = dict()
        for i in range(11):
            dic[i] = linked_list()

        file_path = '/home/user/Desktop/BridgeLabz/Week2/Utility/hasing_number.txt'
        file_op1 = open(file_path, 'r')
        for line in file_op1.readlines():
            for num in line.split():
                slot = int(num)%11
                for i in dic:
                    if slot == i:
                        dic[i].insert_end(int(num))
        file_op1.close()

        #print(dic[8].print_list())
        #number = int(input("Enter your number : "))
        c = False
        for i in dic:
            cur_node = dic[i].head
            while cur_node is not None:
                if number == cur_node.data:
                    position = dic[i].pos(number)            
                    dic[i].del_at(position)
                    print("Removed from the data")
                    c = True
                    break
                cur_node = cur_node.next

        if c == False:
            file_op2 = open(file_path,'a')
            file_op2.write("{0}\n".format(number))
            print("Added to the data")
            file_op2.close()
        elif c == True:
            file_op3 = open(file_path, 'w')
            for i in dic:
                cur_node = dic[i].head
                while cur_node is not None:
                    file_op3.write("{0}\n".format(cur_node.data))
                    cur_node = cur_node.next
            file_op3.close()
    except:
        print("oops! something went wrong")

if __name__ == "__main__":
    try:
        number = int(input("Enter your number : "))
        search_hash(number)
    except:
        print("Invalid Input")