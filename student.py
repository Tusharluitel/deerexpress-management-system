class Student:
    def __int__(self, name, roll, batch):
        self.name = name
        self.roll = roll
        self.batch = batch


def studentdetail():
    name = input("Enter your name: ")
    roll = input("Enter your roll number: ")
    batch = input("Enter your batch: ")

    print(f'Hey {name}, do you wanna participate in the next Deerexpress event?')
    choose = input("Press 'y' for yes and 'n' for no: ")
    if choose == 'y':
        print('Thank you for your participant')
    else:
        print('Maybe next time 😕')

