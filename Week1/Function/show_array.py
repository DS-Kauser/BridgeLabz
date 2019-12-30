import sys
sys.path.append('/home/user/Desktop/BridgeLabz')             # helps in importing function from utility

# importing show_array from utility
from Week1.Utility.utility import show_array                                  

if __name__ == '__main__':                                              
    
    while True:                                                         
        try:
            # taking user-input for rows and columns                                                            
            row = int(input("Enter number of rows : "))                 
            col = int(input("Enter number of columns : "))              
            
            # passing the argument in show_array function
            array2D = show_array(row, col)                               
            print("Your 2D array is \n")
            print(array2D)                                      
            
            # breaking while loop
            break                                                       

        except:
            print("Enter Valid Input")                                  