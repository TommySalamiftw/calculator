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

            a = input("Enter yes/no to carry on using the calculator")
            if a == "yes":
                            continue
            elif a == "no":
                            break
            else:
                print("Enter either yes/no")

main()