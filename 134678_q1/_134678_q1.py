def add_patient(patients):
  """
  Prompts user for patient details and adds them as a dictionary to the patients list.
  """
  name = input("Enter patient name: ")
  age = int(input("Enter patient age: "))
  illness = input("Enter patient illness: ")
  patient = {"name": name, "age": age, "illness": illness}
  patients.append(patient)
  print("Patient added successfully!")

def display_patients(patients):
  """
  Iterates over the patients list and prints details of each patient.
  """
  if not patients:
    print("No patients in the list yet.")
    return
  print("Patients:")
  for i, patient in enumerate(patients):
    print(f"{i+1}. Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(patients, name):
  """
  Searches for a patient with the given name and returns their details if found.
  Returns None if not found.
  """
  for patient in patients:
    if patient["name"].lower() == name.lower():
      return patient
  return None

def remove_patient(patients, name):
  """
  Finds and removes a patient with the given name from the patients list.
  """
  for i, patient in enumerate(patients):
    if patient["name"].lower() == name.lower():
      del patients[i]
      print("Patient removed successfully!")
      return
  print(f"Patient named {name} not found.")

def main():
  """
  Main function to manage the patient management system loop.
  """
  patients = []
  while True:
    print("\nPatient Management System")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Remove Patient")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
      add_patient(patients)
    elif choice == "2":
      display_patients(patients)
    elif choice == "3":
      search_name = input("Enter patient name to search: ")
      search_result = search_patient(patients, search_name)
      if search_result:
        print(f"\nPatient Details:")
        print(f"Name: {search_result['name']}")
        print(f"Age: {search_result['age']}")
        print(f"Illness: {search_result['illness']}")
      else:
        print(f"Patient named {search_name} not found.")
    elif choice == "4":
      remove_name = input("Enter patient name to remove: ")
      remove_patient(patients, remove_name)
    elif choice == "5":
      print("Exiting program...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()

