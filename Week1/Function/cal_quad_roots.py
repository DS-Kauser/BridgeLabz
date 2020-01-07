import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                 # helps in importing function from utility
# importing cal_quad_roots from utility
from Week1.Utility.utility import cal_quad_roots                                  

def calculate_roots():
    try:                                                                
        # taking coefficient from user input
        a = int(input("Enter coefficient of x^2 i.e. A : "))            
        b = int(input("Enter coefficient of x i.e B: "))                
        c = int(input("Enter constant C : "))                           
        
        # using coefficient as argument for cal_quad_roots function
        root1, root2 = cal_quad_roots(a, b, c)                                
        print("Roots are {0} and {1}".format(root1, root2)) 
    except: 
        print("Enter a valid input")  

if __name__ == '__main__':                                                  
    calculate_roots()