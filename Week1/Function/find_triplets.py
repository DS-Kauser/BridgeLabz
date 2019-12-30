import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                     # helps in importing function from utility

# importing find_triplets from utility
from Week1.Utility.utility import find_triplets                                       

if __name__ == '__main__':                                                      
    while True:                                                                 
        try:         
            # taking elements into list                                                           
            num_of_element = int(input("Enter number of element in the list : "))
            alist = []
            for i in range(num_of_element):
                temp = int(input("Enter your numbers : "))
                alist.append(temp)      
            
            # passing list as argument to calculate triplets
            triplet, num_of_trip = find_triplets(alist)                         
            print("Triplets present : ", triplet)
            print("Number of triplets : {0}".format(num_of_trip))
            break                                                               
        
        except:                                                         
            print("Enter a valid input")                                        