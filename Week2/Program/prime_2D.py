import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import prime

def prime_2D():
    array = []
    start = 0
    end = 100
    for i in range(10):
        array.append(prime(start,end))
        start += 100
        end += 100
    return array

if __name__ == "__main__":
    arr = prime_2D()
    print(arr)