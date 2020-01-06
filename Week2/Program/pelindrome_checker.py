import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import deque

def check_pelindrome(word):
    try:
        
        deque_list = deque()
        for i in word:
            deque_list.add_rear(i)

        deque_word = ''
        cur_node = deque_list.head
        while cur_node is not None:
            deque_word = deque_word + cur_node.data
            cur_node = cur_node.next

        if word == deque_word:
            print("Given input {0} is pelindrome".format(word))
        else:
            print("Given input {0} is not pelindrome".format(word))
    except:
        print("Invalid input")

if __name__ == "__main__":
    word = input("Enter a word to check : ")
    check_pelindrome(word)