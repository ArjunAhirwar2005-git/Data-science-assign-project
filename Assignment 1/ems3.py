 # Step 3: View All Employees

def view_employees(emp_dict):
    """
    Function to display all employees in a table-like structure.
    emp_dict: dictionary containing employee records
    """
    print("\n--- Employee List ---")

    # If no employees exist
    if not emp_dict:
        print(" No employee records available.\n")
        return

    # Print table header
    print(f"{'ID':<6} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 55)

    # Print each employee record
    for emp_id, details in emp_dict.items():
        print(f"{emp_id:<6} {details['name']:<15} {details['age']:<5} {details['department']:<15} {details['salary']:<10}")

    print("-" * 55)
    print(f"✅ Total Employees: {len(emp_dict)}\n")
# Example usage
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 30, "department": "Finance", "salary": 60000},
    103: {"name": "Ravi", "age": 24, "department": "IT", "salary": 45000},
}
view_employees(employees)   
    
