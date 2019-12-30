import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')                     # helps in importing the function from utility

# importing monthly_payment from utility
from Utility.utility import monthly_payment                                     

if __name__ == '__main__':                                                      
    while True:                                                                 
        try:                                                                    
            #taking principal, rate of interest and time period from user
            principal = float(input("Enter Principal value : "))                
            rate = float(input("Enter rate of interest per year : "))           
            time_period = int(input("Enter time period : "))                    
            
            # using them as argument for monthly_paymentfunction
            pay = monthly_payment(principal, rate, time_period)                 
            print("Your Monthly payment is : Rs. {0}".format(pay))
            break                                                               

        except:
            print("Please Enter a valid input")                                 