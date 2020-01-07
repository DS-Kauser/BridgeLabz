import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility
# importing merge_sort from utility
from Week1.Utility.utility import merge_sort                             

def merge_sort_list():
    #try:
        #taking a list and sorting it using merge sort                                                             
        num_of_element = int(input("Enter number of element in your list : "))
        alist = []
        for i in range(num_of_element):
            temp = int(input("Enter your number : "))
            alist.append(temp)
        start = 0
        end = len(alist)
        alist = merge_sort(alist, start, end)                                   
        return alist
    #except:
        #print("Check your input")

# adding a main method
if __name__ == '__main__':                                          
    print(merge_sort_list())