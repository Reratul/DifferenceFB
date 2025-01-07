from subprocess import call

def open_pyfile():
    call(["python", "ForwarDiff.py"])
def open_pyfile1():
    call(["python", "BackwardDiff.py"])

def open_pyfile2():
    call(["python", "print.py"])

# Functions for each option
def option_1():
    print("\nOption 1: Forward Difference")
    open_pyfile()


def option_2():
    print("\nOption 2: Backward Difference")
    open_pyfile1()


def option_3():
    print("\nOption 3: Pascal's Triangle")
    open_pyfile2()


def option_4():
    print("\nOption 4: Exit the Program")
    print("Goodbye!")
    exit()


# Main function to display options and take user input
def main():
    while True:
        print("\nChoose one of the following options:")
        print("1. Forward Difference")
        print("2. Backward Difference")
        print("3. Pascal's Triangle")
        print("4. Exit")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '4':
            option_4()
        else:
            print("Invalid input! Please choose a valid option.")


# Run the main program
if __name__ == "__main__":
    main()

