import sys
sys.path.append("/home/user/Desktop/BridgeLabz")


from Week2.Utility.utility import find_anagram
from Week2.Utility.utility import prime
from Week2.Utility.utility import queue

def queue_prime():
    prime_queue = queue()
    start = 0
    end = 1000
    for i in find_anagram(prime(start,end)):
        prime_queue.enqueue(i)
    prime_queue.print_list()

if __name__ == "__main__":
    queue_prime()
