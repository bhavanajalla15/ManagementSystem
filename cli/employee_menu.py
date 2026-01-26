from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali

#this object of employee repo
emp_db= EmployeeDB()
#emp auth
emp_auth = EmployeeAuthentication(emp_db)

def employeeSignup():
    print("Employee Signup")
    name = input("enter your name :")
    email = input("enter your email :")
    if email_vali(email=email) is not None:
        password = input("enter your password")
        emp_auth.createEmployee(name,email,password)
    else:
        print('''Email id should be having minimum length 5 character''')

def employeeLogin():
    print("Employee Login")
    