import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility

# importing insertion_sort function
from Week1.Utility.utility import insertion_sort                          

if __name__ == '__main__':                                          
    
    try:
        # taking list and sorting it using insertion sort                                                            
        num_of_element = int(input("Enter number of element in your list : "))
        alist = []
        for i in range(num_of_element):
            temp = int(input("Enter your number : "))
            alist.append(temp)
                                      
        alist = insertion_sort(alist)                               
        print(alist)                                                

    except:                                                         
        print("oops! something went wrong")                         