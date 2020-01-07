import sys
sys.path.append("/home/user/Desktop/BridgeLabz")
from Week2.Utility.utility import find_anagram
from Week2.Utility.utility import prime
from Week2.Utility.utility import stack

def stack_prime():
    prime_stack = stack()
    start = 0
    end = 1000
    for i in find_anagram(prime(start,end)):
        prime_stack.push(i)
    prime_stack.print_list()

if __name__ == "__main__":
    stack_prime()
