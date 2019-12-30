import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                 # helps in importing function from utility

# importing to_binary function
from Week1.Utility.utility import to_binary                                       

if __name__ == '__main__':                                                  
    while True:                                                             
        try:                                                                
            # taking decimal number and converting it into binary
            num = int(input("Enter any decimal number : "))                 
            binary = to_binary(num)                                         
            print("Binary conversion for {0} is : {1}".format(num, binary))
            
            # breaking the loop
            break                                                           
        except:
            print("Please Enter a valid input")                             