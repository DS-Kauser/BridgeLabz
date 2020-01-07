import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility
# importing find_leap_year from utility
from Week1.Utility.utility import find_leap_year                          

def is_leap_year():
    try:
        # taking year from user input                                                        
        year = int(input("Enter year : "))                      
        
        # passing year as argument in find_leap_year
        find_leap_year(year)                                    

    except:
        print("Enter Valid Input")                              

if __name__ == '__main__':                                          
    is_leap_year()