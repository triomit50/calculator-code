#calculator(BODMAS not followed, sequential only)
try:
    def main():
        choice=input("Enter your operator: ")
        res=0
        while(choice!="="):
            if(choice=="+"or choice=="-" or choice=="*" or choice=="/"):
                num=float(input("Enter the number : "))
                while(choice!="="):
                    if(choice=="+"):
                        res=res+num
                        choice=input("Enter the next operator or press '=' to exit: ")
                        break
                    elif(choice=='-'):
                        res=res-num
                        choice=input("Enter the next operator or press '=' to exit: ")
                        break
                    elif(choice=='*'):
                        res=res*num
                        choice=input("Enter the next operator or press '=' to exit: ")
                        break
                    elif(choice=='/'):
                        res=res/num
                        choice=input("Enter the next operator or press '=' to exit: ")
                        break
                    else:
                        print("Invalid choice!!")
                        break
            else:
                break         
        print("The result is: ",res)
except NameError:
    print("Error Detected: Invalid Name detected!!")
except TypeError:
    print("Error Detected: Invalid processing type detected!!")
except IndexError:
    print("Error Detected: Indexing is undefined. Out of bounds!!")
except ValueError:
    print("Error Detected: Invalid value detected!!")
except SyntaxError:
    print("Error Detected: Invalid syntax detected!!")
