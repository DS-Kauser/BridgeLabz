import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')                     # helps in importing function from utility

# importing money_change function from utility
from Utility.utility import money_change                                        

if __name__ == '__main__':                                                      
    
    while True:                                                                 
        
        try:                                                                    
            # taking user input for amount
            amount = int(input("Enter your amount in between (0 - 20000): "))   
            if amount < 0:
                continue
            # calculating changes
            money_change(amount)                                                
            break                                                               

        except:
            print("Enter a valid input")                                        