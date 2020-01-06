import sys
sys.path.append('/home/user/Desktop/BridgeLabz')         # helps in importing function from utility

# importing find_leap_year from utility
from Week1.Utility.utility import gambler

def start_gambling():
    # taking user input
    stake = int(input("Enter your stake : "))
    goal = int(input("Enter your goal value : "))
    trails = int(input("Enter number of trails : "))
    gambler(stake, goal, trails)

# adding main method
if __name__ == "__main__":
    start_gambling()