# Appointment_test.py

import pytest
from models.Appointment import Appointment, AppointmentManager

# Fixtures to set up initial data for testing
@pytest.fixture
def appointment_manager():
    return AppointmentManager()

@pytest.fixture
def appointment():
    return Appointment(appointment_id=1, patient_id=1, doctor_id=101, appointment_date="2024-10-20 09:30", reason="General Checkup")

# Test cases for AppointmentManager class
def test_book_appointment(appointment_manager, appointment):
    # Test booking a new appointment
    appointment_manager.book_appointment(appointment)
    assert len(appointment_manager.appointments) == 1
    assert appointment_manager.appointments[1].reason == "General Checkup"

def test_book_existing_appointment(appointment_manager, appointment):
    # Test booking an appointment that already exists
    appointment_manager.book_appointment(appointment)
    appointment_manager.book_appointment(appointment)
    assert len(appointment_manager.appointments) == 1  # Should still only have one appointment

def test_cancel_appointment(appointment_manager, appointment):
    # Test canceling an appointment
    appointment_manager.book_appointment(appointment)
    appointment_manager.cancel_appointment(1)
    assert len(appointment_manager.appointments) == 0

def test_cancel_nonexistent_appointment(appointment_manager):
    # Test canceling an appointment that doesn't exist
    appointment_manager.cancel_appointment(99)  # Should not raise an error
    assert len(appointment_manager.appointments) == 0

def test_update_appointment_info(appointment_manager, appointment):
    # Test updating appointment information
    appointment_manager.book_appointment(appointment)
    appointment_manager.update_appointment(1, appointment_date="2024-10-20 10:30", reason="Follow-up")
    assert appointment_manager.appointments[1].appointment_date.strftime("%Y-%m-%d %H:%M") == "2024-10-20 10:30"
    assert appointment_manager.appointments[1].reason == "Follow-up"

def test_view_appointment(capsys, appointment_manager, appointment):
    # Test viewing an appointment's details
    appointment_manager.book_appointment(appointment)
    appointment_manager.view_appointment(1)
    captured = capsys.readouterr()
    assert "Appointment ID: 1, Patient ID: 1, Doctor ID: 101, Appointment Date: 2024-10-20 09:30:00, Reason: General Checkup" in captured.out

def test_view_nonexistent_appointment(capsys, appointment_manager):
    # Test viewing an appointment that doesn't exist
    appointment_manager.view_appointment(99)
    captured = capsys.readouterr()
    assert "Appointment with ID 99 does not exist." in captured.out

def test_list_all_appointments(capsys, appointment_manager, appointment):
    # Test listing all appointments when there is one appointment
    appointment_manager.book_appointment(appointment)
    appointment_manager.list_all_appointments()
    captured = capsys.readouterr()
    assert "Appointment ID: 1, Patient ID: 1, Doctor ID: 101, Appointment Date: 2024-10-20 09:30:00, Reason: General Checkup" in captured.out

def test_list_no_appointments(capsys, appointment_manager):
    # Test listing all appointments when there are no appointments
    appointment_manager.list_all_appointments()
    captured = capsys.readouterr()
    assert "No appointments available." in captured.out

def test_find_appointments_for_patient(capsys, appointment_manager, appointment):
    # Test finding appointments for a specific patient
    appointment_manager.book_appointment(appointment)
    appointment_manager.find_appointments_for_patient(1)
    captured = capsys.readouterr()
    assert "Appointment ID: 1, Patient ID: 1, Doctor ID: 101, Appointment Date: 2024-10-20 09:30:00, Reason: General Checkup" in captured.out

def test_find_appointments_for_nonexistent_patient(capsys, appointment_manager):
    # Test finding appointments for a patient with no appointments
    appointment_manager.find_appointments_for_patient(99)
    captured = capsys.readouterr()
    assert "No appointments found for Patient ID 99." in captured.out

# Main section to run tests if executing directly
if __name__ == "__main__":
    pytest.main()
