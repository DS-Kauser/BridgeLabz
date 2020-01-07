import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                     # helps in importing function from utility
# importing money_change function from utility
from Week1.Utility.utility import money_change                                        

def min_change():
    while True:
        try:                                                                    
            # taking user input for amount
            amount = int(input("Enter your amount in between (0 - 20000): "))   
            if amount < 0 or amount > 20000:
                continue
            # calculating changes
            money_change(amount)                                                
            # while loop exit 
            break                                                               
        except:
            print("Enter a valid input")     

if __name__ == '__main__':                                                      
    min_change()