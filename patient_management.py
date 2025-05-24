import json
import os

DATA_FILE = 'patients.json'

# Load existing data or initialize empty list
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new patient
def add_patient():
    patients = load_data()
    patient = {
        "id": input("Enter Patient ID: "),
        "name": input("Enter Patient Name: "),
        "age": input("Enter Patient Age: "),
        "gender": input("Enter Gender (M/F): "),
        "condition": input("Enter Medical Condition: "),
        "phone": input("Enter Phone Number: ")
    }
    patients.append(patient)
    save_data(patients)
    print("Patient added successfully!\n")

# View all patients
def view_patients():
    patients = load_data()
    if not patients:
        print("No patient records found.\n")
        return
    for p in patients:
        print(f"ID: {p['id']}, Name: {p['name']}, Age: {p['age']}, Gender: {p['gender']}, Condition: {p['condition']}, Phone: {p['phone']}")
    print()

# Update patient info
def update_patient():
    patients = load_data()
    pid = input("Enter Patient ID to update: ")
    for patient in patients:
        if patient["id"] == pid:
            patient["name"] = input("Enter new name: ") or patient["name"]
            patient["age"] = input("Enter new age: ") or patient["age"]
            patient["gender"] = input("Enter new gender: ") or patient["gender"]
            patient["condition"] = input("Enter new condition: ") or patient["condition"]
            patient["phone"] = input("Enter new phone: ") or patient["phone"]
            save_data(patients)
            print("Patient updated successfully.\n")
            return
    print("Patient not found.\n")

# Delete patient
def delete_patient():
    patients = load_data()
    pid = input("Enter Patient ID to delete: ")
    new_patients = [p for p in patients if p["id"] != pid]
    if len(new_patients) == len(patients):
        print("Patient not found.\n")
    else:
        save_data(new_patients)
        print("Patient deleted successfully.\n")

# Main menu
def menu():
    while True:
        print("==== Healthcare Patient Management System ====")
        print("1. Add New Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print()

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
