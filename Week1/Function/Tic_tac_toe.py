import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')         # helps in importing function from utility 

from Utility.utility import play_tic_tac_toe                        # importing play_tic_tac_toe function from utility

if __name__ == '__main__':                                          # cresting main method
    while True:                                                     # to run the code again if any error is found
        try:                                                        # to catch error
            play_tic_tac_toe()                                      # playing tic-tac-toe
            break                                                   # breaking the while loop

        except:
            print("Enter a valid Input")                            # if any error is found