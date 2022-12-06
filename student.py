import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="!swastik@019", 
  database = 'studentsdatabase'
)
# print(mydb)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE studentsdatabase")
# mycursor.execute("SHOW DATABASES ")
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), DOB VARCHAR(255), address VARCHAR(255), phoneNumber VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)


class User():
    def __init__(self):
        self.fname=""
        self.lname=""
        self.DOB=""
        self.address=""
        self.phoneNumber=""
    
    # encapsulation=> binding data to method for securing
    
    def set_fname(self, fname):
        self.fname = fname
    
    def get_fname(self):
        return self.fname 
    
    def set_lname(self, lname):
        self.lname = lname
    
    def get_lname(self):
        return self.lname 
    
    def set_DOB(self, DOB):
        self.DOB = DOB
    
    def get_DOB(self):
        return self.DOB 
    
    def set_address(self, address):
        self.address = address
    
    def get_address(self):
        return self.address 
    
    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    
    def get_phoneNumber(self):
        return self.phoneNumber 
    
    def __str__(self) -> str:
        name = self.fname + " " + self.lname
        return name
    
    
        

def menu():
    menu = ['1 : View all students', '2 : Search students by ID', '3 : Insert students', '4 : Delete students', '5 : Export to csv', '6 : RETURN']
    for m in menu :
        print(m)
        
class Student(User):
    def __init__(self):
        super().__init__()
        
    def __str__(self) -> str:
        return super().__str__()
        
    
while True:
    students_detail = Student()
    no_id = True
    menu()
    number = int(input('Please select any to proceed...\n'))
    
    if number == 1:
        mycursor.execute("SELECT * FROM students")

        student_data = mycursor.fetchall()

        for x in student_data:
            print(x)
        
      
    
    elif number == 2:
        id = int(input("Provide Id of student \n"))
        
        sql = "SELECT * FROM students WHERE id = %s"
        
        mycursor.execute(sql, (id,))
        student = mycursor.fetchall()
        
        for x in student:
            print(x)
            if x:
                no_id = False
                
        if no_id:
                print('not found..') 
                
            
    elif number == 3:
        while True:           
            if not students_detail.get_fname():
                students_detail.set_fname(input('fname :  '))
                continue
        
            if not students_detail.get_lname():
                students_detail.set_lname(input('lname :  '))
                continue
        
            if not students_detail.get_DOB():
                students_detail.set_DOB(input('DOB :  '))
                continue
        
            if not students_detail.get_address():
                students_detail.set_address(input('address :  '))
                continue
        
            if not students_detail.get_phoneNumber():
                students_detail.set_phoneNumber(input('phoneNumber :  '))
                continue
            
            break
          
       
        data = students_detail.__dict__  
        sql = "INSERT INTO students (fname, lname, DOB, address, phoneNumber) VALUES(%s, %s, %s, %s, %s)" 
        val = (data['fname'], data['lname'], data['DOB'], data['address'], data['phoneNumber'],)

        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
       
       
        
        print('Sucessfully registered !!')
        print('-------------------------------')
        
        
    elif number == 4:
        id = int(input("Provide Id of student you want to delete \n"))
        sql = "SELECT * FROM students WHERE id = %s"
        
        mycursor.execute(sql, (id,))
        student = mycursor.fetchall()
        for s in student:
            print(s)
            if s:
                no_id = False
                confirm = input('Are you sure you want to delete it? y/n \n')
                if confirm == "y":
                    dsql = "DELETE FROM students WHERE id = %s"
                    mycursor.execute(dsql, (id,))
                    mydb.commit()
                    print(mycursor.rowcount, "record(s) deleted")
                    
                elif confirm == "n":
                    continue
        
        if no_id:
                print('not found..')    
    
    elif number == 5:
        mycursor.execute("SELECT * FROM students")

        student_data = mycursor.fetchall()

        with open("student.csv", "w+") as file:
            for x in student_data:
                x=str(x)
                x= x.replace('(','')
                x= x.replace(')','')
                file.write(x)
                file.write('\n')
              
        
    elif number == 6:
        break
        
             
    else:
            print('please provide valid response')   
           
