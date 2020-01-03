import sys
sys.path.append("/home/user/Desktop/BridgeLabz")

from Week2.Utility.utility import stack

if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter your expression : ")
            dummy_stack = stack()
            c = None
            for i in expression:
                if i == '(':
                    dummy_stack.push(i)
                elif i == ')':
                    if dummy_stack.is_empty() == False:
                        dummy_stack.pop()
                    else:
                        print("Expression is not balanced")
                        c = True
                        break
            
            if c == True:
                break
            
            if dummy_stack.is_empty() == True:
                print("Expression is balanced")
            else:
                print("Expression is not balanced")
            break
        except:
            print("Invalid input")