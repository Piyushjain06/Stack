
def menu():
    print(
        """\n          M E N U
    _____________________________
    Choice    --->       Function
    --------  --->      ----------
    1         --->     PUSH an element
    2         --->     POP an element 
    3         --->   EXIT the program"""
    )

def push(l):

    still = "y"
    while still == "y":
        l.append(None)
        top = int(input("\nEnter the Elements which you would like to push: "))
        for i in range(len(l) - 1, 0, -1):
            l[i] = l[i - 1]
        l[0] = top
        try:
            print('\n',l[0],"<-----Top ")
            for i in range(1, len(l)):
                print('\n',l[i])
        except IndexError:
            print("\nUnderflow!!!!!!")
        still = input("\nWould you like to push an another element? 'Y/N' ").lower()

def pop_stk(l):
    still = "y"
    while still == "y":
        if l!=[]:
            try:
                print("\nYou Just popped ", l.pop(0))
                if l==[]:
                    print("The Current stack is Empty [Underflow]")
                    break
                else:
                    print('\n',l[0],"<-----Top ")
                    for i in range(1, len(l)):
                       print('\n',l[i])
            except IndexError:
                print("\nUnderflow!!!")
                break
            else:
                still = input("\nWould You like to pop an another element? 'Y/N' ")
        else:
            print("UnderFlow!!!!!")
            break



# Main
l = []
while True:
    menu()
    choice = int(input("\nEnter Choice (1-4): "))
    if choice == 1:
        push(l)
    elif choice == 2:
        pop_stk(l)
    elif choice == 3:
        print("\nThanks for using!!!")
        exit()
    else:
        print("Enter a Valid value!!")
        continue
