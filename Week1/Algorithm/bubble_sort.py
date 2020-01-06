import sys
sys.path.append('/home/user/Desktop/BridgeLabz')             # helps in importing function from utility

# importing bubble_sort function
from Week1.Utility.utility import bubble_sort                                 

if __name__ == '__main__':                                              
    while True:                                                         
        try:                                                            
            #sorting with bubble sort
            num_of_element = int(input("Enter number of element in the list : "))
            a_list = []
            for i in range(num_of_element):
                temp = int(input("Enter your integers : "))
                a_list.append(temp)
                              
            a_list = bubble_sort(a_list)                                  
            print(a_list)
            break
        except:                                                         
            print("Invalid Input")                                      