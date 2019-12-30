import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                 # helps in importing function from utility

# importing cal_quad_roots from utility
from Week1.Utility.utility import cal_quad_roots                                  

if __name__ == '__main__':                                                  
    while True:                                                             
        
        try:                                                                
            # taking coefficient from user input
            a = int(input("Enter coefficient of x^2 i.e. A : "))            
            b = int(input("Enter coefficient of x i.e B: "))                
            c = int(input("Enter constant C : "))                           
            
            # using coefficient as argument for cal_quad_roots function
            r1, r2 = cal_quad_roots(a, b, c)                                
            print("Roots are {0} and {1}".format(r1, r2))               
            break                                                           
            
        except: 
            print("Enter a valid input")                                    