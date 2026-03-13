# Step 2: Add Employee Function

def add_employee(emp_dict):
    """
    Function to add a new employee record to the employee dictionary.
    emp_dict: dictionary storing all employee records
    """
    print("\n--- Add New Employee ---")

    # 1️⃣ Get unique Employee ID
    while True:
        try:
            emp_id = int(input("Enter Employee ID (integer): "))
            if emp_id in emp_dict:
                print(" Employee ID already exists! Please enter a unique ID.")
            else:
                break
        except ValueError:
            print(" Please enter a valid integer ID.")

    # 2️⃣ Get other employee details
    name = input("Enter Name: ").strip()
    while not name:
        print(" Name cannot be empty.")
        name = input("Enter Name: ").strip()

    # Age validation
    while True:
        try:
            age = int(input("Enter Age: "))
            if 18 <= age <= 100:
                break
            else:
                print(" Age must be between 18 and 100.")
        except ValueError:
            print(" Please enter a valid integer for age.")

    department = input("Enter Department: ").strip()
    while not department:
        print(" Department cannot be empty.")
        department = input("Enter Department: ").strip()

    # Salary validation
    while True:
        try:
            salary = int(input("Enter Salary: "))
            if salary >= 0:
                break
            else:
                print(" Salary cannot be negative.")
        except ValueError:
            print(" Please enter a valid number for salary.")

    # 3️⃣ Add new employee record
    emp_dict[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary,
    }

    print(f"\n✅ Employee '{name}' added successfully with ID {emp_id}!\n")
# Example usage
employees = {}  
add_employee(employees) 
print(employees)        

