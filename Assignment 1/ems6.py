import json
import os

# Step 6: File Handling — Save and Load Data

DATA_FILE = "employees.json"

def save_data(emp_dict):
    """
    Save employee data to a JSON file.
    """
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(emp_dict, f, indent=4)
        print("💾 Employee data saved successfully!\n")
    except Exception as e:
        print(f" Error saving data: {e}")


def load_data():
    """
    Load employee data from a JSON file.
    If the file doesn't exist, return an empty dictionary.
    """
    if not os.path.exists(DATA_FILE):
        print(" No existing data found. Starting fresh.\n")
        return {}

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        print("✅ Employee data loaded successfully!\n")
        # Convert keys to integers (JSON stores dict keys as strings)
        return {int(k): v for k, v in data.items()}
    except Exception as e:
        print(f" Error loading data: {e}")
        return {}
# Example usage
employees = load_data() 
print(employees)
# Modify employees dictionary as needed...  
save_data(employees)    


                            