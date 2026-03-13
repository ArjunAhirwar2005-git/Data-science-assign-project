# Step 5: Main Menu System

def main_menu(emp_dict):
    """
    Function to display the main menu and handle user selections.
    emp_dict: dictionary containing all employee records
    """
    while True:
        print("=== Employee Management System (EMS) ===")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search for an Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_employee(emp_dict)
        elif choice == "2":
            view_employees(emp_dict)
        elif choice == "3":
            search_employee(emp_dict)
        elif choice == "4":
            print("\n✅ Exiting the system. Thank you for using EMS!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 4.\n")
# Example usage
employees = {   
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 30, "department": "Finance", "salary": 60000},
    103: {"name": "Ravi", "age": 24, "department": "IT", "salary": 45000},
}                       
main_menu(employees)    
# Note: Ensure that the functions add_employee, view_employees, and search_employee
# are defined in the same file or imported appropriately for this main_menu function to work.       

from ems2 import add_employee
from ems3 import view_employees     
from ems4 import search_employee

   


