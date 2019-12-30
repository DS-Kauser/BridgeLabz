import sys
sys.path.append('/home/user/Desktop/BridgeLabz/Week1')         # helps in importing function from utility

# importing get_permutations from utility
from Week1.Utility.utility import get_permutations                        

if __name__ == '__main__':                                          
    while True:                                                     
        try:                                                        
            # taking user input string and getting permutations
            string = input("Enter your String : ")                  
            get_permutations(string)                                
            break                                                   

        except:                                                     
            print("Invalid Input")                                  

