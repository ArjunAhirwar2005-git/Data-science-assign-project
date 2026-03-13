# Step 7: Update and Delete Employee Records

def update_employee(emp_dict):
    """
    Function to update details of an existing employee.
    """
    print("\n--- Update Employee ---")

    if not emp_dict:
        print("⚠️ No employees to update.\n")
        return

    try:
        emp_id = int(input("Enter Employee ID to update: "))
    except ValueError:
        print("⚠️ Invalid ID format.\n")
        return

    if emp_id not in emp_dict:

        
        print("❌ Employee not found.\n")
        return

    emp = emp_dict[emp_id]
    print(f"\nCurrent details for Employee {emp_id}:")
    print(f"Name       : {emp['name']}")
    print(f"Age        : {emp['age']}")
    print(f"Department : {emp['department']}")
    print(f"Salary     : {emp['salary']}\n")

    # Get new details (press Enter to skip)
    new_name = input("Enter new name (or press Enter to keep current): ").strip()
    new_age = input("Enter new age (or press Enter to keep current): ").strip()
    new_dept = input("Enter new department (or press Enter to keep current): ").strip()
    new_salary = input("Enter new salary (or press Enter to keep current): ").strip()

    # Update fields only if user entered something
    if new_name:
        emp["name"] = new_name
    if new_age:
        try:
            emp["age"] = int(new_age)
        except ValueError:
            print("⚠️ Invalid age. Keeping old value.")
    if new_dept:
        emp["department"] = new_dept
    if new_salary:
        try:
            emp["salary"] = int(new_salary)
        except ValueError:
            print("⚠️ Invalid salary. Keeping old value.")

    emp_dict[emp_id] = emp
    print(f"\n✅ Employee ID {emp_id} updated successfully!\n")


def delete_employee(emp_dict):
    """
    Function to delete an employee record.
    """
    print("\n--- Delete Employee ---")

    if not emp_dict:
        print("⚠️ No employees to delete.\n")
        return

    try:
        emp_id = int(input("Enter Employee ID to delete: "))
    except ValueError:
        print("⚠️ Invalid ID format.\n")
        return

    if emp_id not in emp_dict:
        print("❌ Employee not found.\n")
        return

    # Confirm before deleting
    confirm = input(f"Are you sure you want to delete Employee ID {emp_id}? (y/n): ").lower()
    if confirm == "y":
        del emp_dict[emp_id]
        print(f"🗑️ Employee ID {emp_id} deleted successfully.\n")
    else:
        print("❎ Deletion canceled.\n")
# Example usage
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 30, "department": "Finance", "salary": 60000},
    103: {"name": "Ravi", "age": 24, "department": "IT", "salary": 45000},
}               
update_employee(employees)
delete_employee(employees)
print(employees)


