import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility

# importing get_permutations from utility
from Week1.Utility.utility import get_permutations                        

def permutation():
    try: 
        word = input("Enter string to get permutations : ")
        get_permutations(word)
    except:
        print("Enter a valid input")

if __name__ == "__main__":
    permutation()