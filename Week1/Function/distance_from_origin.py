import sys
sys.path.append('/home/user/Desktop/BridgeLabz')             # helps in importing function from utility
# importing distance_from_origin function from utility
from Week1.Utility.utility import distance_from_origin                        

def cal_dist():
    try:
        # taking x and y value from user                                                            
        abcissa = float(input("Enter x-value : "))                  
        ordinate = float(input("Enter y-value: "))                  
        
        # passing the argument in the function to calculate distance
        dist = round(distance_from_origin(abcissa, ordinate), 3)              
        print(dist)
    except:
        print("Enter a valid input")    

if __name__ == '__main__' :                                             
    cal_dist()