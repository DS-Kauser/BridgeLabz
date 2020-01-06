import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility

# importing insertion_sort function
from Week1.Utility.utility import insertion_sort                          

if __name__ == '__main__':                                          
    
    try:
        # taking list and sorting it using insertion sort                                                            
        num_of_element = int(input("Enter number of element in your list : "))
        a_list = []
        for i in range(num_of_element):
            temp = int(input("Enter your number : "))
            a_list.append(temp)
                                      
        a_list = insertion_sort(a_list)                               
        print(a_list)                                                

    except:                                                         
        print("Please check your input")                         