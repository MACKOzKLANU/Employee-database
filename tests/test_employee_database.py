import unittest
import sys
import os

# Add the parent directory to the Python path
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, ".."))

# Import the EmployeeDatabase class from src.employee_database module
from src.employee_database import EmployeeDatabase

class Testing(unittest.TestCase):
    def setUp(self):
        # Create temporary test database files for testing
        self.test_db_filename = "database/testjson.json"
        self.test_db_empty_filename = "database/emptyjson.json"

        # Create a test database file with an empty list
        with open(self.test_db_filename, "w") as file:
            file.write("[]")

        # Create an empty test database file
        with open(self.test_db_empty_filename, "w") as file:
            file.write("")

    def tearDown(self):
        # Remove the temporary test database files after each test
        if os.path.exists(self.test_db_filename):
            os.remove(self.test_db_filename)
        if os.path.exists(self.test_db_empty_filename):
            os.remove(self.test_db_empty_filename)
            
    # Test cases start here
    
    def test_load(self):
        # Test loading employee data
        E = EmployeeDatabase("employees.json")
        employees = E.load()

        # Ensure that the loaded data is a list of dictionaries
        self.assertTrue(isinstance(employees, list))
        for employee in employees:
            self.assertTrue(isinstance(employee, dict))
    
    def test_load_no_file(self):
        # Test loading from a non-existent file
        E = EmployeeDatabase("nofile.json")
        employees = E.load()

        # Ensure that an empty list is returned when the file doesn't exist
        self.assertEqual(employees, [])
    
    def test_load_empty_file(self):
        # Test loading from an empty file
        E = EmployeeDatabase("emptyjson.json")
        employees = E.load()

        # Ensure that an empty list is returned when the file is empty
        self.assertEqual(employees, [])
    
    def test_add_employee(self):
        # Test adding an employee
        E = EmployeeDatabase("testjson.json")
        E.add_employee("John")
        employees = E.load()

        # Ensure that the added employee is in the list
        self.assertTrue(len(employees) > 0)
        self.assertEqual(employees[0]["name"], "John")
    
    def test_remove_employee(self):
        # Test removing an employee
        E = EmployeeDatabase("testjson.json")
        E.remove_employee(0)
        employees = E.load()

        # Ensure that the employee is removed from the list
        self.assertEqual(len(employees), 0)
    
    def test_get_nonexistent_employee(self):
        # Test getting a non-existent employee
        E = EmployeeDatabase("testjson.json")

        # Ensure that None is returned for a non-existent employee
        self.assertIsNone(E.get_employee(10))
    
    def test_remove_nonexisting_employee(self):
        # Test removing a non-existent employee
        E = EmployeeDatabase("testjson.json")

        E.remove_employee(0)
        employees = E.load()

        # Ensure that removing a non-existent employee doesn't affect the list
        self.assertEqual(len(employees), 0)
    
    def test_update_employee(self):
        # Test updating an employee
        E = EmployeeDatabase("testjson.json")
        E.add_employee("John")
        E.update_employee(0, "Mack")
        employees = E.load()

        # Ensure that the employee's name is updated
        self.assertEqual(employees[0]["name"], "Mack")
        E.remove_employee(0)
    
    def test_update_nonexistent_employee(self):
        # Test updating a non-existent employee
        E = EmployeeDatabase("testjson.json")
        E.update_employee(0, "name")
        employees = E.load()
    
if __name__ == '__main__':
    unittest.main()
