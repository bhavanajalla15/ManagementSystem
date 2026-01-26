# module for login and signup for employee and admin
# from validation import email_validator

class AdminAuthentication:
    def adminLogin():
        pass
class EmployeeAuthentication:
    def __init__(self,db):
        self.db =db
        
    def createEmployee(self,e_name,e_email,password):
        self.e_name = e_name
        self.e_email = e_email
        self.password = password
        self.db.createEMP(self.e_name,self.e_email,self.password)
