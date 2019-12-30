import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz')         # helps in importing function from utility

# importing merge_sort from utility
from Week1.Utility.utility import merge_sort                             

if __name__ == '__main__':                                          
    try:
        #taking a list and sorting it using merge sort                                                             
        alist = [5,1,2,6,4,3,10,7,9,8,12,16,13]                     
        alist = merge_sort(alist)                                   
        print(alist)
    
    except:
        print("oops! something wet wrong")                          