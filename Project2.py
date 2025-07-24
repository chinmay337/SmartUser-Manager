# Assignmet 2
import os

E_FOLDER = "Employee"

if not os.path.exists(E_FOLDER):
    os.makedirs(E_FOLDER)

def get_file_name(data):
    name = data.get("name")
    company = data.get("company_name")
    if company:
        return f"{name}_{company}.txt"
    else:
        return f"{name}.txt"

def add_employee():
    print("\n--- ADD NEW EMPLOYEE DETAILS ---")

    while True:
        name = input("Enter the name of the employee (mandatory): ")
        if name:
            break
        print("Name is required.")

    while True:
        email = input("Enter the employee email (must contain '@'): ")
        if '@' in email:
            break
        print("Invalid email. It must contain '@'.")

    while True:
        location = input("Enter the location of the employee (mandatory): ")
        if location:
            break
        print("Location is required.")

    while True:
        age_input = input("Enter the age of the employee (18 to 60): ")
        if age_input.isdigit():
            age = int(age_input)
            if 18 <= age <= 60:
                break
            else:
                print("Age must be between 18 and 60.")
        else:
            print("Age must be a number.")

    company_name = input("Enter the company name (optional): ")
    company_loc = input("Enter the company location (optional): ")

    employee_data = {
        "name": name,
        "email": email,
        "location": location,
        "age": age,
    }

    if company_name:
        employee_data["company_name"] = company_name
    if company_loc:
        employee_data["company_loc"] = company_loc

    file_name = get_file_name(employee_data)
    file_path = os.path.join(E_FOLDER, file_name)

    with open(file_path, 'w') as file:
        for key, value in employee_data.items():
            file.write(f"{key}: {value}\n")

    print(f"Employee data saved to: {file_path}")


def show_details():
    files = os.listdir(E_FOLDER)
    if not files:
        print("\nNo employee records found. Please add an employee first.")
        return

    print("\nAvailable Employee Files:")
    for f in files:
        print(f" - {f}")

    while True:
        print("\n--- SHOW EMPLOYEE DETAILS ---")
        file_name = input("Enter employee file name (with .txt): ")
        file_path = os.path.join(E_FOLDER, file_name)

        if not os.path.exists(file_path):
            print("File not found. Try again.")
            continue

        with open(file_path, 'r') as file:
            print("\nEmployee Details:")
            for content in file:
                print(content.strip())
        break


def edit_details():
    while True:
        print("\n--- EDIT EMPLOYEE DETAILS ---")

        files = os.listdir(E_FOLDER)
        if not files:
            print("\nNo employee records found.")
            return

        print("\nAvailable Employee Files:")
        for f in files:
            print(f" - {f}")

        file_name = input("Enter employee file name (with .txt): ")
        file_path = os.path.join(E_FOLDER, file_name)

        if not os.path.exists(file_path):
            print("File not found. Try again.")
            continue

        with open(file_path, 'r') as file:
            data = {}
            for line in file:
                if ':' in line:
                    key, value = line.strip().split(":", 1)
                    data[key.strip()] = value.strip()

        print("\nCurrent Employee Data:")
        for k, v in data.items():
            print(f"{k}: {v}")

        print("\nChoose an option:")
        print("1. Edit a field")
        print("2. Delete a field")
        print("3. Add a new field")

        while True:
            choice = input("Enter your choice (1/2/3): ")
            if choice in ["1", "2", "3"]:
                break
            print("Invalid choice. Please enter 1, 2, or 3.")

        if choice == "1":
            while True:
                key_to_edit = input("Enter the key you want to edit: ")
                if key_to_edit in data:
                    new_value = input(f"Enter new value for {key_to_edit}: ")
                    data[key_to_edit] = new_value
                    print(f"{key_to_edit} updated.")
                    break
                else:
                    print("Key not found. Try again.")

        elif choice == "2":
            while True:
                key_to_delete = input("Enter the key to delete: ")
                if key_to_delete in data:
                    del data[key_to_delete]
                    print(f"{key_to_delete} deleted.")
                    break
                else:
                    print("Key not found. Try again.")

        elif choice == "3":
            while True:
                new_key = input("Enter new key name: ").strip()
                if not new_key:
                    print("Key name cannot be empty. Try again.")
                    continue
                new_value = input("Enter value for new key: ")
                data[new_key] = new_value
                print(f"{new_key} added.")
                break

        with open(file_path, 'w') as file:
            for k, v in data.items():
                file.write(f"{k}: {v}\n")
        print("Employee data updated.")
        break

def resign_employee():
    while True:
        print("\n--- RESIGN EMPLOYEE ---")
        
        files = os.listdir(E_FOLDER)
        if not files:
            print("\nNo employee records found.")
            return

        print("\nAvailable Employee Files:")
        for f in files:
            print(f" - {f}")

        file_name = input("Enter employee file name (with .txt): ")
        file_path = os.path.join(E_FOLDER, file_name)

        if not os.path.exists(file_path):
            print("File not found. Try again.")
            continue

        with open(file_path, 'r') as file:
            data = {}
            for line in file:
                if ':' in line:
                    key, value = line.strip().split(":", 1)
                    data[key.strip()] = value.strip()

        if "company_name" in data:
            reason = input("Enter reason for resignation: ")
            data["reason"] = reason
            del data["company_name"]
            if "company_loc" in data:
                del data["company_loc"]

            with open(file_path, 'w') as file:
                for k, v in data.items():
                    file.write(f"{k}: {v}\n")

            print("Resignation updated and saved.")


            os.remove(file_path)
            print(f"Employee file '{file_name}' has been deleted after resignation.")

        else:
            print("No company_name found. Cannot resign.")
        break


def main():
    while True:
        print("\n=== EMPLOYEE MANAGEMENT SYSTEM ===")
        print("1. Add New Employee")
        print("2. Show Details")
        print("3. Edit Existing Details")
        print("4. Resign")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            show_details()
        elif choice == "3":
            edit_details()
        elif choice == "4":
            resign_employee()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()

