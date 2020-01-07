import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                         # hepls in importing function from utility
# importing coupon_number function
from Week1.Utility.utility import gen_coupon_number                                           

def get_coupons():
    try:                                                                        
        # user-input for number of coupons required
        num_of_coupons = int(input("Enter number of coupons you need : "))      
        
        # passing argument in function
        coupons = gen_coupon_number(num_of_coupons)                                 
        print(coupons)                                                                   
    except:
        print("Enter a valid input")                                            

if __name__ == '__main__':                                                          
    get_coupons()                                                                     
        