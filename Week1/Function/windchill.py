import sys
sys.path.append('/home/user/Desktop/BridgeLabz')                     # helps in importing functioni from utility
# importing cal_windchill_speed function from utility   
from Week1.Utility.utility import cal_windchill_speed                                 

def wind_chill_speed():
    try:
        # taking user input for temperature and velocity                                                                    
        t = float(input("Enter temperature in Fahrenheit : "))              
        v = float(input("Enter speed in miles per hour : "))                

        # passing argument in cal_windchill_speed
        speed_windchill = round(cal_windchill_speed(t, v), 3)
        print("Wind chill speed : {0} degrees Fahrenheit".format(speed_windchill))
    except:
        print("Enter a valid input") 

if __name__ == '__main__':                                                      
    wind_chill_speed()                                                                 
                                               