import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import deque

def create_rev_deque(word):
    deque_list = deque()
    for item in word:
        deque_list.add_rear(item)
    return deque_list

def get_word(deque_list):
    deque_word = ''
    cur_node = deque_list.head
    while cur_node is not None:
        deque_word = deque_word + cur_node.data
        cur_node = cur_node.next
    return deque_word

def check_pelindrome(word, rev_word):
    if word == rev_word:
        print("Given input {0} is pelindrome".format(word))
        return 
    print("Given input {0} is not pelindrome".format(word))
    return

if __name__ == "__main__":
    word = input("Enter a word to check : ")
    deque_list = create_rev_deque(word)
    rev_word = get_word(deque_list)
    check_pelindrome(word, rev_word)    