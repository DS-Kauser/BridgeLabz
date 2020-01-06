import sys                                                          
sys.path.append('/home/user/Desktop/BridgeLabz')             # help in importing function from utility
from Week1.Utility.utility import anagram_detection                           

def detect_anagram():
    try:                                                            
        # taking two user input
        first_word = str(input("Enter first word : "))                   
        second_word = str(input("Enter second word : "))
        # checking anagram
        anagram_detection(first_word, second_word)                                                                         
    except:                                                         
        print("Enter a valid input")    

if __name__ == '__main__':                                              
    detect_anagram()                                