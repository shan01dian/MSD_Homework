# Doctor.py

class Doctor:
    def __init__(self, doctor_id, name, specialization, phone_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.phone_number = phone_number

    def update_info(self, name=None, specialization=None, phone_number=None):
        """ Update doctor's information """
        if name:
            self.name = name
        if specialization:
            self.specialization = specialization
        if phone_number:
            self.phone_number = phone_number

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, Phone: {self.phone_number}"

# To manage a collection of doctors
class DoctorManager:
    def __init__(self):
        self.doctors = {}

    def add_doctor(self, doctor):
        """ Add a doctor to the collection """
        if doctor.doctor_id in self.doctors:
            print(f"Doctor with ID {doctor.doctor_id} already exists.")
        else:
            self.doctors[doctor.doctor_id] = doctor
            print(f"Doctor {doctor.name} added successfully.")

    def delete_doctor(self, doctor_id):
        """ Delete a doctor by ID """
        if doctor_id in self.doctors:
            removed_doctor = self.doctors.pop(doctor_id)
            print(f"Doctor {removed_doctor.name} removed successfully.")
        else:
            print(f"Doctor with ID {doctor_id} does not exist.")

    def update_doctor(self, doctor_id, name=None, specialization=None, phone_number=None):
        """ Update doctor's information """
        if doctor_id in self.doctors:
            doctor = self.doctors[doctor_id]
            doctor.update_info(name, specialization, phone_number)
            print(f"Doctor {doctor_id} updated successfully.")
        else:
            print(f"Doctor with ID {doctor_id} does not exist.")

    def view_doctor(self, doctor_id):
        """ View a doctor's information """
        if doctor_id in self.doctors:
            print(self.doctors[doctor_id])
        else:
            print(f"Doctor with ID {doctor_id} does not exist.")

    def list_all_doctors(self):
        """ List all doctors in the collection """
        if self.doctors:
            for doctor in self.doctors.values():
                print(doctor)
        else:
            print("No doctors available.")

# Example usage
if __name__ == "__main__":
    manager = DoctorManager()

    # Adding doctors
    doctor1 = Doctor(doctor_id=1, name="Dr. Chen", specialization="Cardiology", phone_number="123456789")
    doctor2 = Doctor(doctor_id=2, name="Dr. Liu", specialization="Neurology", phone_number="987654321")
    manager.add_doctor(doctor1)
    manager.add_doctor(doctor2)

    # Viewing a doctor
    manager.view_doctor(1)

    # Updating doctor information
    manager.update_doctor(1, phone_number="1122334455")

    # Viewing updated information
    manager.view_doctor(1)

    # Deleting a doctor
    manager.delete_doctor(2)

    # Listing all doctors
    manager.list_all_doctors()
