from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password

#this object of employee repo
emp_db= EmployeeDB()
#this emp auth
emp_auth = EmployeeAuthentication(emp_db)

def employeeSignup():
    print("Employee Signup")
    name = input("enter your name :")
    email = input("enter your email :")
    if email_vali(email=email) is not None:
        password = getpass("Enter your password :")
        if password_vali(password):
            password = password_hasher(password)
            emp_auth.createEmployee(name,email,password)
        else:
            print('''password is not valid
                  password should minimum length of 5
                  password should contain  atleast uppercase character ex:A B J ..
                  password should contain   atleast special character ex: @ # $ % * !....
                  password should contain atleast one digit ex: 7 4 6 ..''')
            employeeSignup()
    else:
        print('''Email id is not valid!!!!''')
        employeeSignup()

def employeeLogin():
    print("Employee Login")
    email = input("Enter your email id :")
    password = getpass("Enter your password :")
    hashed_pw = emp_auth.empLogin(email)
    if check_password(password,hashed_pw):
        print("login successfull!!")
    else:
        print("login failed")
