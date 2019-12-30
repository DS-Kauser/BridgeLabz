import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz')             # helps in importing function from utility

# importing bubble_sort function
from Week1.Utility.utility import bubble_sort                                 

if __name__ == '__main__':                                              
    while True:                                                         
        try:                                                            
            #sorting with bubble sort
            alist = [5,1,2,6,4,3,10,7,9,8]                              
            alist = bubble_sort(alist)                                  
            print(alist)
            break
        except:                                                         
            print("Invalid Input")                                      