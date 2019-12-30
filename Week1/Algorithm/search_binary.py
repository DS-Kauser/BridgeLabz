import sys
import os
os.chdir("/home/user/Desktop/BridgeLabz/Week1/Utility")
sys.path.append('/home/user/Desktop/BridgeLabz')   

from Week1.Utility.utility import binary_search

if __name__ == '__main__':                                                  # creating main method
    while True:                                                             # to run the code again if any error is found
        try:
            # opening file and reading it
            file1 = open('text.txt', 'r')
            f1 = file1.readlines()
            alist = []
            for line in f1:
                word = line.split()
                alist.extend(word)
            
            alist = sorted(alist)                                           # sorting that list 
            print("Sorted list : {0}".format(alist))
            start = 0
            end = len(alist)-1
            word = input("Enter word that should be searched : ")           # taking user input word to be searched

            binary_search(alist, start, end, word)                          # searching that word in that list
            break
        except:
            print("Enter a valid input")                                    # if any error is found