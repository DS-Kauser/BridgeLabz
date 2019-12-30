import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz')         # helps in importing function from utility

# importing insertion_sort function
from Week1.Utility.utility import insertion_sort                          

if __name__ == '__main__':                                          
    
    try:
        # taking list and sorting it using insertion sort                                                            
        
        alist = [5,1,2,6,4,3,10,7,9,8]                              
        alist = insertion_sort(alist)                               
        print(alist)                                                

    except:                                                         
        print("oops! something went wrong")                         