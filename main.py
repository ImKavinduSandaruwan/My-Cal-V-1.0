#Coded by Kavindu Sandaruwan
def add(num1,num2):
    print("Answer is :",num1 + num2)

def sub(num1,num2):
    print("Answer is :",num1 - num2)

def mul(num1,num2):
    print("Answer is :",num1*num2)

def div(num1,num2):
    print("Answer is :",num1/num2)

def banner():
    print('\033[1;34m' "███╗   ███╗██╗   ██╗       █████╗  █████╗ ██╗     ")
    print('\033[1;34m' "████╗ ████║╚██╗ ██╔╝      ██╔══██╗██╔══██╗██║     ")
    print('\033[1;33m' "██╔████╔██║ ╚████╔╝ █████╗██║  ╚═╝███████║██║     ")
    print('\033[1;33m' "██║╚██╔╝██║  ╚██╔╝  ╚════╝██║  ██╗██╔══██║██║     ")
    print('\033[1;34m' "██║ ╚═╝ ██║   ██║         ╚█████╔╝██║  ██║███████╗")
    print('\033[1;34m' "╚═╝     ╚═╝   ╚═╝          ╚════╝ ╚═╝  ╚═╝╚══════╝")
    print('\033[1;32m' "_______________________ᴄᴏᴅᴇᴅ ʙʏ Kᴀᴠɪɴᴅᴜ Sᴀɴᴅᴀʀᴜᴡᴀɴ" '\033[0m')
    print()
    print(" [1] ADD")
    print(" [2] SUB")
    print(" [3] MUL")
    print(" [4] DIV")
    print()

def main():
    x = int(input(" [*] Enter Your Choise: "))
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    if x == 1:
        add(num1,num2)
    elif x == 2:
        sub(num1,num2)
    elif x == 3:
        mul(num1,num2)
    elif x == 4:
        div(num1,num2)
    else:
        print("You entered invalid choise....")

banner()
main()
