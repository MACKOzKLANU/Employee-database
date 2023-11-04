
import sys
import os

# Add the parent directory to the Python path
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, ".."))

# Import the EmployeeDatabase class from src.employee_database module
from src.employee_database import EmployeeDatabase

def main():
    # Create an instance of EmployeeDatabase with the desired file name
    db = EmployeeDatabase("employees.json")

    while True:
        print("\nEmployee Database Menu:")
        print("1. Add Employee")
        print("2. Get Employee")
        print("3. Remove Employee")
        print("4. Update Employee")
        print("5. Show Employees")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            db.add_employee(name)
            print(f"{name} added to the database.")
        
        elif choice == "2":
            employee_id = int(input("Enter employee ID: "))
            db.get_employee(employee_id)
        
        elif choice == "3":
            employee_id = int(input("Enter employee ID to remove: "))
            db.remove_employee(employee_id)
            print(f"Employee with ID {employee_id} removed.")
        
        elif choice == "4":
            employee_id = int(input("Enter employee ID to update: "))
            new_name = input("Enter the new name: ")
            db.update_employee(employee_id, new_name)
            print(f"Employee with ID {employee_id} updated to {new_name}.")
        
        elif choice == "5":
            db.show_employees()
        
        elif choice == "6":
            print("Exiting the Employee Database.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
