import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz')                             # helps in importing function from utility

# importing find_prime,find_pelindrome, find_anagram function
from Week1.Utility.utility import find_prime                                                  
from Week1.Utility.utility import find_pelindrome                                             
from Week1.Utility.utility import find_anagram                                                

if __name__ == '__main__':                                                              
    while True:                                                                         
        try:                                                                            
            # taking the end point and calculating prime numbers till that point
            end = int(input("Enter the end point till you want prime number : "))       
            prime = find_prime(end)                                                     
            print("Prime number in between 0 to {0} : ".format(end))
            print(prime, end = '\n\n')

            # from prime number list finding pelindrome number
            pelind = find_pelindrome(prime)                                             
            print("Pelindrome number in these prime numbers list : ")
            print(pelind, end = '\n\n')

            # from prime number list finding anagram
            anag = find_anagram(prime)                                                  
            print("Anagram in these prime number list : ")
            print(anag, end = '\n\n')

            # calculating prime number which is anagram and pelindrome both
            pelind2 = find_pelindrome(anag)                                             
            print("Number which is pelindrome as well as anagram in prime number list : ")
            print(pelind2)
            break
        
        except:
            print("Invalid Input")                                                      # if any error is found