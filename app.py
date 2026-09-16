import os 
import json
import re

FILE_NAME = 'students.json'

def load_data():
    
    if os.path.exists(FILE_NAME):
        
        with open(FILE_NAME, "r") as file:
            
            data = file.read().strip()
            
            if data == "":
                return {}
    
            return json.loads(data)
            
    else:
        with open(FILE_NAME, "w") as file:
            json.dump({}, file, indent=4)
        
        return {}
    
def save_data(student):
    
    with open(FILE_NAME, "w") as file:
        json.dump(student, file, indent=4)
        
def add_student(student):
    
    try:
        name = input("Enter Name : ").title().strip()
        
        if not name:
            print("\nEnter Valid Name!")
            
        id = input("Enter ID : ").upper()
        marks = int(input("Enter Marks : "))
        
        if 35 <= marks <= 100:
            result = "PASS"
            
        else:
            result = "FAIL"
            
        if re.fullmatch(r"[A-Z0-9]+", id):
            
            student[name] = {
                "Marks": marks,
                "ID": id,
                "Result": result
            }
            
            save_data(student)

            print("\nStudent Successfully Added!")
            print(f"Name : {name}")
            print(f"Id : {id}")
            print(f"Marks : {marks}")
            print(f"Result : {result}")
        
        else:
            print("\nIn-Valid ID!")    
        
    except Exception as e:
        print(f"\nError - {str(e)}")
        
def search_student(student):
    
    name = input("Enter Name : ").title().strip()
    
    if name in student:
        
        print("\nStudent Record:")
        print(f"Name : {name}")
        print(f"ID : {student[name]["ID"]}")
        print(f"Marks : {student[name]["Marks"]}")
        print(f"Result : {student[name]["Result"]}")
        
    else:
        print("\nStudent Not Found!")
      
def delete_student(student):
    
    name = input("Enter Name : ").title().strip()
    
    if name in student:
        
        print("\nStudent Record:")
        print(f"Name : {name}")
        print(f"ID : {student[name]["ID"]}")
        print(f"Marks : {student[name]["Marks"]}")
        print(f"Result : {student[name]["Result"]}\n")
        
        con = input("Do you wan't to delete this student? (Yes / No) : ").strip()
        
        if con == "Yes" or con == "y":
            del student[name]
            
            save_data(student)
            
            print("\nStudent Deleted Successfully!")
            
        elif con == "No" or con == "n":
            pass
        
        else:
            print("\nEnter Yes or No!")
            
    else:
        print("\nStudent Not Found!")
            
def correct_student(student):
    
    name = input("Enter Student Name : ").title().strip()
    
    if name in student:
        
        print("\nCurrent Record:")
        print(f"Name : {name}")
        print(f"ID : {student[name]["ID"]}")
        print(f"Marks : {student[name]["Marks"]}")
        print(f"Result : {student[name]["Result"]}")
        
        print("\nOption")
        print("1. Name")
        print("2. Marks")
        print("3. ID")
        print("4. Both")
        
        c = input("Enter your choice (1-4) : ")
        
        if c in ["1", "4"]:
            new_name = input("Enter New Name : ").title().strip()
            
            if new_name in student:
                print("\nThis name already exist!")
                return
            
            else:
                
                student[new_name] = student.pop(name)
                name = new_name
                
                save_data(student)      
                
                print("\nStudent name has been changed!")  
                
        if c in ["2", "4"]:
            
            try:
                
                marks = int(input("Enter Marks : "))
                student[name]["Marks"] = marks
                
                if 35 <= marks <= 100:
                    result = "PASS"
                    
                else:
                    result = "FAIL"
                    
                student[name]["Result"] = result
                
                save_data(student)
                print("\nMarks has been changed!")
                
            except ValueError:
                print("❌ Please enter valid marks!")
        
        if c in ["3", "4"]:
            
            new_id = input("Enter New ID : ").upper()
            
            if re.fullmatch(r"[A-Z0-9]+", new_id):
                student[name]["ID"] = new_id
                save_data(student)
                
                print("\nID has been changed!")
            
            else:
                print("\nEnter Valid ID!")
                return
            
        else:
            print("Enter choice beetwen 1-4!")
            return
        
        print("\nNew Record:")
        print(f"Name : {name}")
        print(f"ID : {student[name]["ID"]}")
        print(f"Marks : {student[name]["Marks"]}")
        print(f"Result : {student[name]["Result"]}\n")
    
    else:
        print("\nStudent Not Found!")
        
def main(student):
    
    while True:
        
        print("\n" + "=" * 41)
        print("      Student Management System")
        print("=" * 41)
        
        print("\n      Option")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Correct Student")
        print("5. Exit\n")
        
        c = input("Enter your Choice : ")
        
        if c == "1":
            add_student(student)
            
        elif c == "2":
            delete_student(student)
            
        elif c == "3":
            search_student(student)
            
        elif c == "4":
            correct_student(student)
            
        elif c == "5":
            print("\nProgram closing!")
            break
        
        else:
            print("\nEnter Choice beetwen 1-5!")
    
student = load_data()
        
main(student)