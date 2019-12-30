import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility

# importing merge_sort from utility
from Week1.Utility.utility import merge_sort                             

if __name__ == '__main__':                                          
    while True:
        try:
            #taking a list and sorting it using merge sort                                                             
            num_of_element = int(input("Enter number of element in your list : "))
            alist = []
            for i in range(num_of_element):
                temp = int(input("Enter your number : "))
                alist.append(temp)
                                
            alist = merge_sort(alist)                                   
            print(alist)
            break
        
        except:
            print("oops! something wet wrong")                          