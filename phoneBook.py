

phoneBook={'rema':'1234567890'}

def func1():
    check= False

    while check == False:
        name = input("enter contact name")
        num = input("enter contact number")
        if type(name) ==str:
            if len(num) == 10:
                check=True
    phoneBook[name]=num


def func2():
    choice1=input("enter 1 for specific contact of 2 for all contacts")
    if choice1 == '1':
        name1=input("enter name")
        x=phoneBook.get(name1)
        if x == None:
            print("contact dose not exist")
        else:
            print(x)
    else:
        print(phoneBook)

while True:
    choice = input("enter 1 for adding new contact or 2 for browsing contact")
    if choice == '1':
        func1()
    else:
        func2()















