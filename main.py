from student import studentdetail
print("Welcome to Deerexpress Management System")

def main():

    print('Select the optinsss....')
    print('1. Student Login')
    print('2. Member Login')
    print('3. Exit')
    try:
        option = int (input('Use numbers: '))
    except ValueError:
        print('Use numbers for choosing')
        exit()

    match (option):
        case 1:
            # funtion imported from student.py
            studentdetail()
        case 2:
            print('You have choosen Member login')
        case 3:
            print('Thank you for using Deerexpress Management System')
        case _:
            print('Choose the given options')

if __name__ == '__main__':
    main()