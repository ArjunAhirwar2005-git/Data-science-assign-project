# Step 1: Initialize data storage with sample data [cite: 5, 11]
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

def add_employee():
    """Adds a new employee to the dictionary [cite: 50]"""
    print("\n--- Add New Employee ---")
    
    # Check for unique Employee ID [cite: 29, 30]
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Error: This ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric ID.")

    # Prompt for details [cite: 21, 23, 25, 27, 28]
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ")
    salary = float(input("Enter Monthly Salary: "))

    # Store in dictionary [cite: 31]
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': dept,
        'salary': salary
    }
    print(f"Success: Employee {name} added successfully! [cite: 32]")

def view_employees():
    """Displays all employees in a table-like structure [cite: 51]"""
    print("\n--- View All Employees ---")
    if not employees:
        print("No employees available. [cite: 37]")
        return

    # Table Header 
    print(f"{'ID':<10} {'Name':<15} {'Age':<10} {'Dept':<15} {'Salary':<10}")
    print("-" * 60)
    
    # Display each employee [cite: 34]
    for emp_id, info in employees.items():
        print(f"{emp_id:<10} {info['name']:<15} {info['age']:<10} {info['department']:<15} {info['salary']:<10}")

def search_employee():
    """Searches for an employee by ID [cite: 52]"""
    print("\n--- Search Employee ---")
    try:
        search_id = int(input("Enter Employee ID to search: [cite: 39]"))
        
        # Search dictionary [cite: 40]
        if search_id in employees:
            emp = employees[search_id]
            print(f"Found: Name: {emp['name']}, Age: {emp['age']}, Dept: {emp['department']}, Salary: {emp['salary']} [cite: 41]")
        else:
            print("Employee not found. [cite: 43]")
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")

def main_menu():
    """Main function to control the menu loop [cite: 49]"""
    while True:
        # Display Menu [cite: 14, 15, 16, 17, 18]
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using EMS. Goodbye! [cite: 46]")
            break # Exit the loop [cite: 19, 45]
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()