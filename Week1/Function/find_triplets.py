import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                     # helps in importing function from utility

# importing find_triplets from utility
from Week1.Utility.utility import find_triplets                                       

if __name__ == '__main__':                                                      
    while True:                                                                 
        try:         
            # taking elements into list                                                           
            alist = input("Enter intergers separated by space : ").split()      
            
            # converting element into integers
            alist = list(map(lambda x : int(x), alist))                         
            
            # passing list as argument to calculate triplets
            triplet, num_of_trip = find_triplets(alist)                         
            print("Triplets present : ", triplet)
            print("Number of triplets : {0}".format(num_of_trip))
            break                                                               
        
        except:                                                         
            print("Enter a valid input")                                        