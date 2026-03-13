"""
Step 1: Basic Setup for Employee Management System (EMS)
"""

# Initialize employee dictionary with sample data
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 30, "department": "Finance", "salary": 60000},
    103: {"name": "Ravi", "age": 24, "department": "IT", "salary": 45000},
}

# Display a simple welcome message
print("=== Employee Management System (EMS) ===")
print("Employee records loaded successfully!")
print(f"Total employees: {len(employees)}")

# Print all employees
for emp_id, emp_info in employees.items():
    print(f"ID: {emp_id}, Name: {emp_info['name']}, Department: {emp_info['department']}")    
        
