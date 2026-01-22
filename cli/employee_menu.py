from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB

#this object of employee repo
emp_db= EmployeeDB()
#emp auth
emp_auth = EmployeeAuthentication(emp_db)

def employeeSignup():
    print("Employee Signup")
    name = input("enter your name :")
    email = input("enter your email :")
    password = input("enter your password")
    emp_auth.createEmployee(name,email,password)

def employeeLogin():
    print("Employee Login")
    