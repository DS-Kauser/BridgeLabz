import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')                 # helps in importing function from utility

# importing to_binary function
from Utility.utility import to_binary                                       

if __name__ == '__main__':                                                  
    while True:                                                             
        try:                                                                
            # taking decimal number and converting it into binary
            num = int(input("Enter any decimal number : "))                 
            binary = to_binary(num)                                         
            print(binary)
            break                                                           
        except:
            print("Please Enter a valid input")                             