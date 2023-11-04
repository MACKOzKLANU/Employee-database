import json
import sys
import os

# Add the parent directory to the Python path
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, ".."))

# Import the required modules
from database import *

class EmployeeDatabase:
    def __init__(self, filename):
        # Initialize the EmployeeDatabase with a filename
        self.database = "database/" + filename

    def load(self):
        try:
            # Attempt to read JSON data from the given file
            with open(self.database, "r") as file:
                self.employees = json.load(file)
        except FileNotFoundError:
            # Handle the case when the file is not found
            self.employees = []
        except json.JSONDecodeError:
            # Handle the case when the JSON data in the file is invalid
            self.employees = []

        return self.employees

    def show_employees(self):
        employees = self.load()
        if not employees:
            print("No employees found in the database.")
        else:
            print("Employee List:")
            for employee in employees:
                print(f"ID: {employee['id']}, Name: {employee['name']}")
    
    def save(self, data):
        # Save data to the file
        with open(self.database, "w") as file:
            json.dump(data, file, indent=2)

    def add_employee(self, employee_name):
        employees = self.load()
        current_id = 0

        for employee in employees:
            if current_id == employee["id"]:
                current_id += 1

        new_employee = {
            "id": current_id,
            "name": employee_name
        }
        employees.append(new_employee)
        self.save(employees)

    def get_employee(self, employee_id):
        employees = self.load()
        for employee in employees:
            if employee_id == employee["id"]:
                print(employee["name"])

    def remove_employee(self, employee_id):
        employees = self.load()

        for employee in employees:
            if employee["id"] == employee_id:
                employees.remove(employee)

        self.save(employees)

    def update_employee(self, employee_id, new_name):
        employees = self.load()

        for employee in employees:
            if employee["id"] == employee_id:
                employee["name"] = new_name
                self.save(employees)

# Example usage of the EmployeeDatabase class
E = EmployeeDatabase("employees.json")
# E.add_employee("Patrick")
# E.get_employee(1)
# E.remove_employee(2)
# E.update_employee(1, "Pat")
# E.save()
