import sys
import os
os.chdir("/home/user/Desktop/BridgeLabz/Week1/Utility")
sys.path.append('/home/user/Desktop/Mack/BridgeLabz')   

from Week1.Utility.utility import binary_search

if __name__ == '__main__':                                                  # creating main method
    while True:                                                             # to run the code again if any error is found
        try:
            # opening file and reading it
            file1 = (open('text.txt', 'r'))
            alist = file1.read()
            alist = list(alist)
            
            for i in range(len(alist)):
                if alist[i]=='\n'  or alist[i] == ":" or alist[i] == "." or alist[i] == "(" or alist[i] == ")":
                    alist[i]=' '

            alist = ''.join(alist)
            alist = alist.split(' ')
            
            alist = sorted(alist)                                           # sorting that list 
            print("Sorted list : {0}".format(alist))
            start = 0
            end = len(alist)-1
            word = input("Enter word that should be searched : ")           # taking user input word to be searched

            binary_search(alist, start, end, word)                          # searching that word in that list
            break
        except:
            print("Enter a valid input")                                    # if any error is found