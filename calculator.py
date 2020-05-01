def main():
                
    def divide(x, y):
        return x / y

    def subtract(x, y):
        return x-y

    def multiply(x,y):
        return x * y

    def add(x, y):
        return x + y

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    #Start your main loop here

    choice_bool = False

    print("Select What you want to do Calculator made by filip.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while (choice_bool == False):
        choice = input("Enter your choice(1/2/3/4): ")

        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            choice_bool = True
        else:
            print("Cannot be worked out")

        if choice_bool:

            num1_correct = False
            num1 = 0
            counter_num1 = 0

            while (not num1_correct):
                counter_num1 += 1
                num1_inp = input("Enter the first number: ")
                if is_number(num1_inp):
                    num1_correct = True
                    num1 = float(num1_inp)
                else:
                    if (counter_num1 % 3 == 0):
                        print("Fuck you. I'm outta here!")
                    else:
                        print("That was not a number, motherfucker!")

            num2_correct = False
            num2 = 0
            
            while (not num2_correct):
                num2_inp = input("Enter the Second number: ")
                if is_number(num2_inp):
                    num2_correct = True
                    num2 = float(num2_inp)

            if choice == '1':
                print(num1,"+",num2,"=", add(num1,num2))

            elif choice == '2':
                print(num1,"+",num2,"=", subtract(num1,num2))

            elif choice == '3':
                print(num1,"*",num2,"=", multiply(num1,num2))

            elif choice == '4':
                print(num1,"/",num2,"=", divide(num1,num2))

            #create a boolean outside of the 'while' loop to control exit from the loop
            carryOn_correct= False
 
            #enter the 'while' loop 
            #START 'while'
            while(not carryOn_correct):

                #read user input
                a = input("Enter yes/no to carry on using the calculator (y/yes/n/no) ")

                #check the input; change the boolean controlling the 'while' loop accordingly
                if a == 'y' or a == 'yes' or a == 'n' or a == 'no':
                    carryOn_correct = True
                    #pass

            #END 'while'

            if a == "yes" or a == "y":
                main()

main()