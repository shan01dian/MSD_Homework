# Patient.py

from datetime import datetime


class Patient:
    def __init__(self, patient_id, name, age, gender, phone_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.admission_date = None
        self.discharge_date = None

    def update_info(self, name=None, age=None, gender=None, phone_number=None):
        """ Update patient's information """
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender
        if phone_number:
            self.phone_number = phone_number

    def admit(self, admission_date=None):
        """ Admit the patient with a specific admission date """
        if not admission_date:
            admission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.admission_date = admission_date
        self.discharge_date = None
        print(f"Patient {self.name} admitted on {self.admission_date}")

    def discharge(self, discharge_date=None):
        """ Discharge the patient with a specific discharge date """
        if not discharge_date:
            discharge_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.discharge_date = discharge_date
        print(f"Patient {self.name} discharged on {self.discharge_date}")

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone: {self.phone_number}, Admission Date: {self.admission_date}, Discharge Date: {self.discharge_date}"


# To manage a collection of patients
class PatientManager:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        """ Add a patient to the collection """
        if patient.patient_id in self.patients:
            print(f"Patient with ID {patient.patient_id} already exists.")
        else:
            self.patients[patient.patient_id] = patient
            print(f"Patient {patient.name} added successfully.")

    def delete_patient(self, patient_id):
        """ Delete a patient by ID """
        if patient_id in self.patients:
            removed_patient = self.patients.pop(patient_id)
            print(f"Patient {removed_patient.name} removed successfully.")
        else:
            print(f"Patient with ID {patient_id} does not exist.")

    def update_patient(self, patient_id, name=None, age=None, gender=None, phone_number=None):
        """ Update patient's information """
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.update_info(name, age, gender, phone_number)
            print(f"Patient {patient_id} updated successfully.")
        else:
            print(f"Patient with ID {patient_id} does not exist.")

    def view_patient(self, patient_id):
        """ View a patient's information """
        if patient_id in self.patients:
            print(self.patients[patient_id])
        else:
            print(f"Patient with ID {patient_id} does not exist.")

    def list_all_patients(self):
        """ List all patients in the collection """
        if self.patients:
            for patient in self.patients.values():
                print(patient)
        else:
            print("No patients available.")

    def admit_patient(self, patient_id, admission_date=None):
        """ Admit a patient by ID """
        if patient_id in self.patients:
            self.patients[patient_id].admit(admission_date)
        else:
            print(f"Patient with ID {patient_id} does not exist.")

    def discharge_patient(self, patient_id, discharge_date=None):
        """ Discharge a patient by ID """
        if patient_id in self.patients:
            self.patients[patient_id].discharge(discharge_date)
        else:
            print(f"Patient with ID {patient_id} does not exist.")


# Example usage
if __name__ == "__main__":
    manager = PatientManager()

    # Adding patients
    patient1 = Patient(patient_id=1, name="John Doe", age=45, gender="Male", phone_number="123456789")
    patient2 = Patient(patient_id=2, name="Jane Smith", age=32, gender="Female", phone_number="987654321")
    manager.add_patient(patient1)
    manager.add_patient(patient2)

    manager.view_patient(1)

    manager.update_patient(1, phone_number="1122334455")

    manager.view_patient(1)

    manager.admit_patient(1)

    manager.discharge_patient(1)

    manager.list_all_patients()

    manager.delete_patient(2)
