import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import find_anagram
from Week2.Utility.utility import prime

def prime_anagram():
    start = 0
    end = 1000
    a = prime(start, end)
    array = []
    array.append(find_anagram(a))
    not_anag = []
    for i in a:
        if i not in array[0]:
            not_anag.append(i)
    array.append(not_anag)
    return array

if __name__ == "__main__":
    print(prime_anagram())
