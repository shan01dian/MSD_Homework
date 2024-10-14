# Appointment.py

from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date, reason):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
        self.reason = reason

    def update_appointment(self, appointment_date=None, reason=None):
        """ Update appointment information """
        if appointment_date:
            self.appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
        if reason:
            self.reason = reason

    def __str__(self):
        return (f"Appointment ID: {self.appointment_id}, Patient ID: {self.patient_id}, "
                f"Doctor ID: {self.doctor_id}, Appointment Date: {self.appointment_date}, Reason: {self.reason}")

# To manage a collection of appointments
class AppointmentManager:
    def __init__(self):
        self.appointments = {}

    def book_appointment(self, appointment):
        """ Book a new appointment """
        if appointment.appointment_id in self.appointments:
            print(f"Appointment with ID {appointment.appointment_id} already exists.")
        else:
            self.appointments[appointment.appointment_id] = appointment
            print(f"Appointment for Patient {appointment.patient_id} with Doctor {appointment.doctor_id} booked successfully.")

    def cancel_appointment(self, appointment_id):
        """ Cancel an appointment by ID """
        if appointment_id in self.appointments:
            canceled_appointment = self.appointments.pop(appointment_id)
            print(f"Appointment ID {canceled_appointment.appointment_id} canceled successfully.")
        else:
            print(f"Appointment with ID {appointment_id} does not exist.")

    def update_appointment(self, appointment_id, appointment_date=None, reason=None):
        """ Update appointment information """
        if appointment_id in self.appointments:
            appointment = self.appointments[appointment_id]
            appointment.update_appointment(appointment_date, reason)
            print(f"Appointment ID {appointment_id} updated successfully.")
        else:
            print(f"Appointment with ID {appointment_id} does not exist.")

    def view_appointment(self, appointment_id):
        """ View appointment details by ID """
        if appointment_id in self.appointments:
            print(self.appointments[appointment_id])
        else:
            print(f"Appointment with ID {appointment_id} does not exist.")

    def list_all_appointments(self):
        """ List all appointments in the collection """
        if self.appointments:
            for appointment in self.appointments.values():
                print(appointment)
        else:
            print("No appointments available.")

    def find_appointments_for_patient(self, patient_id):
        """ Find all appointments for a specific patient """
        found_appointments = [appt for appt in self.appointments.values() if appt.patient_id == patient_id]
        if found_appointments:
            for appointment in found_appointments:
                print(appointment)
        else:
            print(f"No appointments found for Patient ID {patient_id}.")

# Example usage
if __name__ == "__main__":
    manager = AppointmentManager()

    # Booking appointments
    appointment1 = Appointment(appointment_id=1, patient_id=1, doctor_id=101, appointment_date="2024-10-20 09:30", reason="General Checkup")
    appointment2 = Appointment(appointment_id=2, patient_id=2, doctor_id=102, appointment_date="2024-10-21 11:00", reason="Consultation")
    manager.book_appointment(appointment1)
    manager.book_appointment(appointment2)

    # Viewing an appointment
    manager.view_appointment(1)

    # Updating an appointment
    manager.update_appointment(1, appointment_date="2024-10-20 10:30")

    # Viewing updated appointment details
    manager.view_appointment(1)

    # Listing all appointments
    manager.list_all_appointments()

    # Canceling an appointment
    manager.cancel_appointment(2)

    # Finding appointments for a specific patient
    manager.find_appointments_for_patient(1)
