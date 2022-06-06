
import mysql.connector

 
bogdanData = mysql.connector.connect(
    host="localhost", user="root", password="Alina90*",database="mydatabase")

mycursor = bogdanData.cursor()

class Fields:
    def __init__(self):
        pass
    
class Employer(Fields):
    def __init__(self):
        super().__init__()
          

class Departments(Fields):
    def __init__(self,name,users):
        super().__init__()
        self.name = name
        self.users = users



def Add_Employee():
 
    Id = input("Enter Employee Id : ")
     
    if(check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
         
    else:
        Name = input("Enter Employee Name : ")
        LastName = input("Enter Employee Last Name : ")
        Age = input("Enter Employee Ages : ")
        Job = input("Enter Employee Job : ")
        Salary = input("Enter Employee Wage : ")
        Bonus = input("Enter Employee Bonus : ")
        TotalSalary = input("Enter Employee TotalSalary : ")
        data = (Id, Name, LastName,Age,Job, Salary,Bonus,TotalSalary)
     
    
        sql = 'insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s)'
        c = bogdanData.cursor()
    
        c.execute(sql, data)
         
        bogdanData.commit()
        print("Employee Added Successfully ")
        menu()
 

def Remove_Employee():
    Id = input("Enter Employee Id : ")
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        sql = 'delete from employees where id=%s'
        data = (Id,)
        c = bogdanData.cursor()
        c.execute(sql, data)
        bogdanData.commit()
        print("Employee Removed")
        menu()
 
 

def check_employee(employee_id):    
    sql = 'select * from employees where id=%s'    
    c = bogdanData.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)  
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 

def Display_Employees():
    sql = 'select * from employees'
    c = bogdanData.cursor()
    c.execute(sql)
     
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("Employee Bonus : ", i[5])
        print("---------------------\
        -----------------------------\
        ------------------------------\
        ---------------------")
         
    menu()

#to be a method it should have been in a class.
def ApplyBonus():
    Id = input("Enter Employee Id : ")
    if(check_employee(Id) == False):
        menu()
    else: 
        Bonus = input("Enter Employee Bonus : ")
        sql = 'UPDATE employees SET Bonus = %s where Id=%s'      
        data = (Bonus, Id)
        c = bogdanData.cursor()
        c.execute(sql,data)        
        
        bogdanData.commit()
        print("Employee's Bonus Updated")
        menu()

   
 
def menu():
    print("Welcome to Employee Management Databse System")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Display Employee")
    print("4 to Apply Bonus")
    print("5 to Exit")
 
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employee()
    elif ch == 2:
        Remove_Employee()
    elif ch == 3:
        Display_Employees() 
    elif ch == 4:
        ApplyBonus()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()
 
menu()