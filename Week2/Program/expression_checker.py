import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import stack

def check_exp():
    dummy_stack = stack()
    expression = input("Enter your expression : ")
    for element in expression:
        if element == '(':
            dummy_stack.push(element)
        if element == ')':
            if dummy_stack.is_empty() == True:
                print("Expression is not balanced")
                return
            dummy_stack.pop()
    if dummy_stack.is_empty() == True:
        print("Expression is balanced")
        return
    print("Expression is not balanced")

if __name__ == "__main__":
    check_exp()