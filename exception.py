#exception: an event that occurs to disrupt the normal flow of operation
# try:
#     age=int(input('Enter age:'))
#     print(age)
# except:
#     print('Please provide numeric value')

# print("Xavier College")

# try:
#     a=int(input("Enter value"))
#     b=int(input("Enter value"))
#     c=a/b
# except ValueError:
#     print('Please provide numeric value')
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print("The value of c is ",c)
def login():
    user1='admin'
    pass1='admin'
    try:
        username=input("Enter username: ")
        password=input("Enter password: ")
        if user1!=username:
            raise ZeroDivisionError
        elif pass1!=password:
            raise ValueError
    except ZeroDivisionError:
        print("Username invalid")
        login()
    except ValueError:
        print("Wrong Password")
        login()
    else:
        print("Login Successful!")
    finally:
        print("Home")
login()

