import sys                                                          
sys.path.append('/home/user/Desktop/BridgeLabz')             # help in importing function from utility

from Week1.Utility.utility import anagram_detection                           

if __name__ == '__main__':                                              
    while True:                                                         
        try:                                                            
            # taking two user input
            first_word = str(input("Enter first word : "))                   
            second_word = str(input("Enter second word : "))
            
            # checking anagram
            anagram_detection(first_word, second_word)                  
            break                                                       

        except:                                                         
            print("Enter a valid input")                                