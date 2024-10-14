# Patient_test.py

import pytest
from models.Patient import Patient, PatientManager

# Fixtures to set up initial data for testing
@pytest.fixture
def patient_manager():
    return PatientManager()

@pytest.fixture
def patient():
    return Patient(patient_id=1, name="John Doe", age=45, gender="Male", phone_number="123456789")

# Test cases for PatientManager class
def test_add_patient(patient_manager, patient):
    # Test adding a new patient
    patient_manager.add_patient(patient)
    assert len(patient_manager.patients) == 1
    assert patient_manager.patients[1].name == "John Doe"

def test_add_existing_patient(patient_manager, patient):
    # Test adding a patient that already exists
    patient_manager.add_patient(patient)
    patient_manager.add_patient(patient)
    assert len(patient_manager.patients) == 1  # Should still only have one patient

def test_delete_patient(patient_manager, patient):
    # Test deleting a patient
    patient_manager.add_patient(patient)
    patient_manager.delete_patient(1)
    assert len(patient_manager.patients) == 0

def test_delete_nonexistent_patient(patient_manager):
    # Test deleting a patient that doesn't exist
    patient_manager.delete_patient(99)  # Should not raise an error
    assert len(patient_manager.patients) == 0

def test_update_patient_info(patient_manager, patient):
    # Test updating patient information
    patient_manager.add_patient(patient)
    patient_manager.update_patient(1, name="John Doe Updated", phone_number="987654321")
    assert patient_manager.patients[1].name == "John Doe Updated"
    assert patient_manager.patients[1].phone_number == "987654321"

def test_view_patient(capsys, patient_manager, patient):
    # Test viewing a patient's information
    patient_manager.add_patient(patient)
    patient_manager.view_patient(1)
    captured = capsys.readouterr()
    assert "Patient ID: 1, Name: John Doe, Age: 45, Gender: Male, Phone: 123456789" in captured.out

def test_view_nonexistent_patient(capsys, patient_manager):
    # Test viewing a patient that doesn't exist
    patient_manager.view_patient(99)
    captured = capsys.readouterr()
    assert "Patient with ID 99 does not exist." in captured.out

def test_list_all_patients(capsys, patient_manager, patient):
    # Test listing all patients when there is one patient
    patient_manager.add_patient(patient)
    patient_manager.list_all_patients()
    captured = capsys.readouterr()
    assert "Patient ID: 1, Name: John Doe, Age: 45, Gender: Male, Phone: 123456789" in captured.out

def test_list_no_patients(capsys, patient_manager):
    # Test listing all patients when there are no patients
    patient_manager.list_all_patients()
    captured = capsys.readouterr()
    assert "No patients available." in captured.out

def test_admit_patient(patient_manager, patient):
    # Test admitting a patient
    patient_manager.add_patient(patient)
    patient_manager.admit_patient(1, admission_date="2024-10-15 09:00:00")
    assert patient_manager.patients[1].admission_date == "2024-10-15 09:00:00"
    assert patient_manager.patients[1].discharge_date is None

def test_discharge_patient(patient_manager, patient):
    # Test discharging a patient
    patient_manager.add_patient(patient)
    patient_manager.admit_patient(1, admission_date="2024-10-15 09:00:00")
    patient_manager.discharge_patient(1, discharge_date="2024-10-20 10:00:00")
    assert patient_manager.patients[1].discharge_date == "2024-10-20 10:00:00"

# Main section to run tests if executing directly
if __name__ == "__main__":
    pytest.main()
