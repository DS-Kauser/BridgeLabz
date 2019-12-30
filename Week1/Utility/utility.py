"""
 ******************************************************************************
 *  Purpose: utils for functions programs and algorithms
 *
 *  @author  Md Kauser Ansari
 *  @version 3.7
 *  @since   20/12/2019
 ******************************************************************************
"""

import numpy as np
from math import sqrt
from itertools import permutations
import random
from datetime import datetime



# Permutation of string
"""
taking a string
calculating all permutaion of string
adding it to list
returning that list
"""
def get_permutations(string):                       
    a = list(permutations(string))                                          
    c = []                                                                  
    for i in range(len(a)):                                     
        c.append(''.join(a[i]))                                             
    print("All permutation of string : {0}".format(c), end = '\n\n')        
    unique = []                                                             
    for i in c:
        if i not in unique:                                                 
            unique.append(i)                                                
    print("All Unique Permutations : {0}".format(unique))                   




# Binary Search
"""
taking list, starting index, end index, and word to be search
using recursive method to search the word
"""
def binary_search(lst, start, end, word):           
     
    if end >= start:                                                                
        mid = start + (end-start) // 2                                              
        if lst[mid].lower() == word.lower():                                        
            print("{0} is present at index {1}".format(word.lower(), mid))
            return None
        elif lst[mid] > word:                                                       
            return binary_search(lst, start, mid, word)                           

        else:                                                                       
            return binary_search(lst, mid+1, end, word)
        
    else:                                                                           
        print('{0} is not found'.format(word))
        return None                                      



#Insertion sort
"""
taking a list 
sorting it with insertion sort method
return that list
"""
def insertion_sort(alist):                          
    for i in range(1,len(alist)):                                   
        item_to_insert = alist[i]                                   
        j = i-1                                                     
        while j >= 0 and alist[j] > item_to_insert:                 
            alist[j+1] = alist[j]                                   
            j -= 1                                                  
        alist[j+1] = item_to_insert                                 
    return alist                                                    



# Bubble sort
"""
taking a list 
sorting it using bubble sort method
return that list
"""
def bubble_sort(alist):                             
    success = True                                                  
    while success:                                                  
        success = False                                             
        for i in range(len(alist)-1):                               
            if alist[i] > alist[i+1]:                               
                alist[i], alist[i+1] = alist[i+1], alist[i]         
                success = True                                      
    return alist                                                    



# Merge Sort
"""
taking alist
sorting that list using merge sort
returning that list
"""
def merge_sort(alist):                              
    if len(alist) > 1:                              
        mid = len(alist)//2                         
        left = alist[ : mid]                        
        right = alist[mid : ]                       
        
        merge_sort(left)                            
        merge_sort(right)                           
        
        i=j=k=0                                     
        while i < len(left) and j < len(right):     
            if left[i] < right[j]:                  
                alist[k] = left[i]                  
                i += 1
                
            else:
                alist[k] = right[j]                 
                j += 1
            k += 1                          
            
            
        while i < len(left):                        
            alist[k] = left[i]                      
            i += 1
            k += 1
            
        while j < len(right):                       
            alist[k] = right[j]                     
            j += 1
            k += 1
            
    return alist                                    



# Anagram Detection
"""
taking two words
checking the letters of the word are same or not
if same thery are anagram
"""
def anagram_detection(a, b):                        

    if len(a) == len(b):                                                    
        c = [x for x in a if x in b]                                        
        d = [x for x in b if x in a]                                        
        if len(c) == len(d):                                                
            print("Given inputs {0} and {1} are Anagram".format(a, b))
        else:
            print("Given inputs are not Anagram")
    else:
        print("Given inputs are not Anagram")



# Find Prime Numbers
"""
taking the end point till user wants a prime number
calculating prime number till that point
return the list containing prime numbers
"""
def find_prime(end):                                
    alist = [2, 3, 5]                               
    
    for i in range(7, end+1):                       
        c = 0                                       
        for j in alist:                             
            if i%j != 0:                            
                c += 1                              
                
        if c == len(alist):                                         
            alist.append(i)                         
    return alist



# Find Pelindrome
"""
taking a list 
checking for pelindrome for each element in the list
return pelindrome list
"""
def find_pelindrome(alist):                         
    pelindrome = []                                 
    for i in alist:                                 
        if str(i) == str(i)[::-1]:                  
            pelindrome.append(i)                    
    
    return pelindrome                               



# Find Anagram
"""
taking a list
checking for element which are anagram
appending to alist
returning that list
"""
def find_anagram(alist):                            
    anagram = []                                                
    for i in alist:                                             
        c = False                                               
        for j in alist:                                         
            if j not in anagram:                                
                if i != j:                                      
                    if sorted(str(i)) == sorted(str(j)):        
                        anagram.append(j)                       
                        c = True
        if c == True:
            anagram.append(i)                                   

    return anagram                                              



# Monthly payment
"""
taking principal, rate of interest and time period
calculating monthly payment
returning this payment
"""
def monthly_payment(principal,rate,time_period):     
    n = 12*time_period                                          
    r = rate / (12 * 100)                                       
    payment = round((principal*r)/(1-(1+r)**(-n)), 2)           
    return payment



# Convert to binary
"""
taking a decimal number
dividing it by 2 and taking out remainder
generate binary number
convert binary number to set of four
returning that number
"""
def to_binary(decimal_num):                           
    a = []                                           
    while decimal_num > 0:                           
        a.append(str(decimal_num%2))                 
        decimal_num = decimal_num//2                 
    a.reverse()                                      
    a = ''.join(a)                                   
    nibble = len(a)%4                                
    if nibble == 0:                                  
        return a                                     
    else:
        nibble = 4-nibble                            
        a = '0'*nibble + a                           
        return a                                     
    
    
# Calculate Quadratic roots
"""
taking all coeficents
calculating discriminant
calculating roots for real or imaginary
returning the roots
"""
def cal_quad_roots(a, b, c):                        
    d = b * b - 4 * a * c                                       
    if d > 0:                                                   

        root1 = round(float((-b + sqrt(d)) / (2 * a)), 3)       
        root2 = round(float((-b - sqrt(d)) / (2 * a)), 3)       

    else:                                                       

        d = abs(d)                                              
        real = round(float(-b / (2 * a)), 3)                    
        image = round(float(sqrt(d) / (2 * a)), 3)              
        root1 = complex(real, image)                            
        root2 = complex(real, -image)

    return root1, root2                                         


# Calculate minimun notes
"""
taking money
dividing it into smallest number of notes possible
returning number of notes and note value
"""
def money_change(money):                            
    moneyDict = {'one' : [1], 'two' : [2,3,4], 'five' : range(5,10), "ten" : range(10,50), 'fifty' : range(50,100), 'hundred' : range(100,500), 'five_hundred' : range(500,1000), 'one_thousand' : range(1000,20000)}           
    numeric = {'one' : 1, 'two' : 2, 'five' : 5, 'ten' : 10, 'fifty' : 50, 'hundred' : 100, 'five_hundred' : 500, 'one_thousand' : 1000}                                                                                        
    c = 0                                                                               
    
    while True:                                                                         
        for i in moneyDict:                                                             

            if money in moneyDict[i]:                                                   

                d = numeric[i]                                                          

                while money >= d:                                                       
                    n_note = money // d                                                 
                    money = money % d                                                   
                    print("{0} notes of rupee {1}".format(n_note, d))                   
                    c += n_note                                                         

        if money == 0:                                                                  
            print("Total minimum number of notes = {0}".format(c))                      
            break                                                                       
            
        else:
            continue                                                                    


# Generate coupon number
"""
taking number to coupon required
choosing 3 elements from upper, lower and num
concatinate them to generate one coupon number
generated requuired coupons in similar fashion
"""
def gen_coupon_number(number_of_coupons):               
    coupon = []                                                                                         

    while True:                                                                                         
        lower = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()                           
        upper = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()                           
        num = "0 1 2 3 4 5 6 7 8 9".split()                                                             
        x, y, z = random.choices(lower, k=3), random.choices(upper, k=3), random.choices(num, k=3)      
        dummy_coupon = []                                                                               

        for j in range(0, 3):
            xyz = x[j] + y[j] + z[j]
            dummy_coupon.append(xyz)                                                                    

        dummy_coupon = ''.join(dummy_coupon)                                                            
            
        if dummy_coupon not in coupon:
            coupon.append(dummy_coupon)                                                                 

        if len(coupon) == number_of_coupons:                                                            
            break
    return coupon                                                                                       


# Distance from origin
"""
taking x-value and y-value
calculating distance from origin
returning that  distance
"""

def distance_from_origin(x, y):                     
    dist = round(sqrt(x * x + y * y), 3)                      
    return dist                                     


# Find Triplets
"""
taking a list
finding two number sum and taking its negative
seaching this number in list
if found returning these three numbers
"""

def find_triplets(list1):                           
    n = len(list1)
    c = 0                                           
    list2 = []                                      
    for i in range(n - 1):                             
        for j in range(i + 1, n):
            x = -(i + j)                            
            if x in list1:                          
                list2.append([x, i, j])             
                c = c + 1                           
    return list2, c                                 


# Find leap year or not
"""
taking a year
checking for leap year
check for century and leap year
"""
def find_leap_year(year):                           
    if len(str(year)) > 3:                                              

        if year % 4 == 0:                                               
            if year % 100 == 0:                                         
                if year % 400 == 0:                                     
                    print("{0} is a leap year".format(year))            
                else:
                    print("{0} is not a leap year".format(year))        
            else:
                print("{0} is a leap year".format(year))                

        else:
            print("{0} is not a leap year".format(year))                

    else:
        print("Enter a valid year of four digits like '1995'")          


# Show Array
"""
defining a function which takes number of rows and columns as arguments
creating an empty list x
loop for user input element and adding it to the list x
user input for values
adding it to list a
changing shape of list a into array(row , col)
    
"""

def show_array(row, col):                           
    
    elements = row * col                            
    x = []                                          
    print("Enter the values row wise")
    for i in range(1, elements + 1):                
        a = int(input("Enter the values: "))        
        x.append(a)                                 
    x = np.array(x).reshape(row, col)               
    return x


def play_tic_tac_toe():                             
    a = [" "] * 9
    a = np.array(a).reshape(3, 3)
    print("************* TIC-TAC-TOE ***************")
    print(a)
    print()
    win = 0
    print("User value is X")
    print()
    while True:
        row_u = int(input("Enter row : "))
        col_u = int(input("Enter column : "))
        print()
        if row_u < 4 and col_u < 4 and row_u > 0 and col_u > 0:
            a[row_u - 1][col_u - 1] = 'X'
            print(a)
            break
        else:
            print("Invalid input")
            continue

    while True:
        row_c = random.randint(0, 2)
        col_c = random.randint(0, 2)
        print()
        if a[row_c][col_c] == ' ':
            a[row_c][col_c] = 'O'
            print(a)
            break
        else:
            continue

    while True:
        row_u = int(input("Enter row : "))
        col_u = int(input("Enter column : "))
        print()
        if row_u < 4 and col_u < 4 and row_u > 0 and col_u > 0:
            if a[row_u - 1][col_u - 1] == ' ':
                a[row_u - 1][col_u - 1] = 'X'
                print(a)
                print()
                break
            else:
                print("Space is occupied")
                print()
                continue
        else:
            print("Invalid input")
            continue

    for turn in range(3):

        for i in range(3):

            # computer win
            if a[i][0] == 'O' and a[i][1] == 'O':
                if a[i][2] == ' ':
                    a[i][2] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[i][1] == "O" and a[i][2] == 'O':
                if a[i][0] == ' ':
                    a[i][0] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[i][0] == "O" and a[i][2] == 'O':
                if a[i][1] == ' ':
                    a[i][1] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[0][i] == 'O' and a[1][i] == 'O':
                if a[2][i] == ' ':
                    a[2][i] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[1][i] == 'O' and a[2][i] == 'O':
                if a[0][i] == ' ':
                    a[0][i] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[0][i] == 'O' and a[2][i] == 'O':
                if a[1][i] == ' ':
                    a[1][i] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[0][0] == 'O' and a[1][1] == 'O':
                if a[2][2] == ' ':
                    a[2][2] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[0][0] == 'O' and a[2][2] == 'O':
                if a[1][1] == ' ':
                    a[1][1] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[1][1] == 'O' and a[2][2] == 'O':
                if a[0][0] == ' ':
                    a[0][0] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[2][0] == 'O' and a[1][1] == 'O':
                if a[0][2] == ' ':
                    a[0][2] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

            elif a[2][0] == 'O' and a[0][2] == 'O':
                if a[1][1] == ' ':
                    a[1][1] = 'O'
                    print(a)
                    print("Computer won")
                    win = 2
                    break

            elif a[1][1] == 'O' and a[0][2] == 'O':
                if a[2][0] == ' ':
                    a[2][0] = 'O'
                    print(a)
                    print("Computer Won")
                    win = 2
                    break

        if win == 2:
            break

            # user
        for i in range(3):
            if a[i][0] == 'X' and a[i][1] == 'X':
                if a[i][2] == ' ':
                    a[i][2] = 'O'
                    print(a)
                    print()
                    break

            elif a[i][1] == "X" and a[i][2] == 'X':
                if a[i][0] == ' ':
                    a[i][0] = 'O'
                    print(a)
                    print()
                    break

            elif a[i][0] == "X" and a[i][2] == 'X':
                if a[i][1] == ' ':
                    a[i][1] = 'O'
                    print(a)
                    print()
                    break

            elif a[0][i] == 'X' and a[1][i] == 'X':
                if a[2][i] == ' ':
                    a[2][i] = 'O'
                    print(a)
                    print()
                    break

            elif a[1][i] == 'X' and a[2][i] == 'X':
                if a[0][i] == ' ':
                    a[0][i] = 'O'
                    print(a)
                    print()
                    break

            elif a[0][i] == 'X' and a[2][i] == 'X':
                if a[1][i] == ' ':
                    a[1][i] = 'O'
                    print(a)
                    print()
                    break

            elif a[0][0] == 'X' and a[1][1] == 'X':
                if a[2][2] == ' ':
                    a[2][2] = 'O'
                    print(a)
                    print()
                    break

            elif a[0][0] == 'X' and a[2][2] == 'X':
                if a[1][1] == ' ':
                    a[1][1] = 'O'
                    print(a)
                    print()
                    break

            elif a[1][1] == 'X' and a[2][2] == 'X':
                if a[0][0] == ' ':
                    a[0][0] = 'O'
                    print(a)
                    print()
                    break

            elif a[2][0] == 'X' and a[1][1] == 'X':
                if a[0][2] == ' ':
                    a[0][2] = 'O'
                    print(a)
                    print()
                    break

            elif a[2][0] == 'X' and a[0][2] == 'X':
                if a[1][1] == ' ':
                    a[1][1] = 'O'
                    print(a)
                    print()
                    break

            elif a[1][1] == 'X' and a[0][2] == 'X':
                if a[2][0] == ' ':
                    a[2][0] = 'O'
                    print(a)
                    print()
                    break



        else:
            while True:
                row_c = random.randint(0, 2)
                col_c = random.randint(0, 2)
                print()
                if a[row_c][col_c] == ' ':
                    a[row_c][col_c] = 'O'
                    print(a)
                    print()
                    break
                else:
                    continue

        while True:
            row_u = int(input("Enter row : "))
            col_u = int(input("Enter column : "))
            print()
            if row_u < 4 and col_u < 4 and row_u > 0 and col_u > 0:
                if a[row_u - 1][col_u - 1] == ' ':
                    a[row_u - 1][col_u - 1] = 'X'
                    print(a)
                    print()
                    break
                else:
                    print("Space is occupied")
                    print()
                    continue
            else:
                print("Invalid input")
                print()

        for i in range(3):
            if a[i][0] == a[i][1] and a[i][1] == a[i][2]:
                if a[i][0] == 'X':
                    print("You Won")
                    win = 1
                    break

            elif a[0][i] == a[1][i] and a[1][i] == a[2][i]:
                if a[0][i] == 'X':
                    print("You Won")
                    win = 1
                    break

            elif a[0][0] == a[1][1] and a[1][1] == a[2][2]:
                if a[0][0] == 'X':
                    print("You Won")
                    win = 1
                    break

            elif a[0][2] == a[1][1] and a[1][1] == a[2][0]:
                if a[0][2] == 'X':
                    print("You Won")
                    win = 1
                    break
        if win == 1:
            break

        if win == 2:
            print("Well Played")
            break

    if win == 2:
        print("You Lose")


    elif win == 1:
        print("Well Played")


# Calculate Windchill speed
"""
taking temperatur and velocity
calculating windchill speed
return windchill speed
"""
def cal_windchill_speed(temp, velocity):            
    wind_chill = round(float(35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * pow(velocity, 0.16)), 3)      
    return wind_chill                                                                                        
