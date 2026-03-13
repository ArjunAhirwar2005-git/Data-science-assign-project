# Step 4: Search Employee

def search_employee(emp_dict):
    """
    Function to search for an employee by their ID.
    emp_dict: dictionary containing employee records
    """
    print("\n--- Search Employee ---")

    # If no employees exist
    if not emp_dict:
        print(" No employee records found.\n")
        return

    # Get Employee ID to search
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print(" Invalid input! Please enter a valid integer ID.\n")
        return

    # Check if employee exists
    if emp_id in emp_dict:
        emp = emp_dict[emp_id]
        print("\n✅ Employee Found:")
        print(f"ID         : {emp_id}")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}\n")
    else:
        print(" Employee not found. Please check the ID and try again.\n")
# Example usage
employees = { 
                  
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 30, "department": "Finance", "salary": 60000},
    103: {"name": "Ravi", "age": 24, "department": "IT", "salary": 45000},
}
search_employee(employees)
        