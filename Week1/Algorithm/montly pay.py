import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                     # helps in importing the function from utility
# importing monthly_payment from utility
from Week1.Utility.utility import monthly_payment                                     

def payment():
    try:                                                                    
        #taking principal, rate of interest and time period from user
        principal = float(input("Enter Principal value : "))                
        rate = float(input("Enter rate of interest per year : "))           
        time_period = int(input("Enter time period : "))                    
        
        # using them as argument for monthly_paymentfunction
        pay = monthly_payment(principal, rate, time_period)                 
        return pay
    except:
        print("Please Enter a valid input")              

if __name__ == '__main__':                                                   
    monthly_pay = payment()
    print("Your monthly payment is Rs.{0}".format(monthly_pay))