# Doctor_test.py

import pytest
from models.Doctor import Doctor, DoctorManager

# Fixtures to set up initial data for testing
@pytest.fixture
def doctor_manager():
    return DoctorManager()

@pytest.fixture
def doctor():
    return Doctor(doctor_id=1, name="Dr. Chen", specialization="Cardiology", phone_number="123456789")

# Test cases for DoctorManager class
def test_add_doctor(doctor_manager, doctor):
    # Test adding a new doctor
    doctor_manager.add_doctor(doctor)
    assert len(doctor_manager.doctors) == 1
    assert doctor_manager.doctors[1].name == "Dr. Chen"

def test_add_existing_doctor(doctor_manager, doctor):
    # Test adding a doctor that already exists
    doctor_manager.add_doctor(doctor)
    doctor_manager.add_doctor(doctor)
    assert len(doctor_manager.doctors) == 1  # Should still only have one doctor

def test_delete_doctor(doctor_manager, doctor):
    # Test deleting a doctor
    doctor_manager.add_doctor(doctor)
    doctor_manager.delete_doctor(1)
    assert len(doctor_manager.doctors) == 0

def test_delete_nonexistent_doctor(doctor_manager):
    # Test deleting a doctor that doesn't exist
    doctor_manager.delete_doctor(99)  # Should not raise an error
    assert len(doctor_manager.doctors) == 0

def test_update_doctor_info(doctor_manager, doctor):
    # Test updating doctor information
    doctor_manager.add_doctor(doctor)
    doctor_manager.update_doctor(1, name="Dr. Chen Updated", phone_number="987654321")
    assert doctor_manager.doctors[1].name == "Dr. Chen Updated"
    assert doctor_manager.doctors[1].phone_number == "987654321"

def test_view_doctor(capsys, doctor_manager, doctor):
    # Test viewing a doctor's information
    doctor_manager.add_doctor(doctor)
    doctor_manager.view_doctor(1)
    captured = capsys.readouterr()
    assert "Doctor ID: 1, Name: Dr. Chen, Specialization: Cardiology, Phone: 123456789" in captured.out

def test_view_nonexistent_doctor(capsys, doctor_manager):
    # Test viewing a doctor that doesn't exist
    doctor_manager.view_doctor(99)
    captured = capsys.readouterr()
    assert "Doctor with ID 99 does not exist." in captured.out

def test_list_all_doctors(capsys, doctor_manager, doctor):
    # Test listing all doctors when there is one doctor
    doctor_manager.add_doctor(doctor)
    doctor_manager.list_all_doctors()
    captured = capsys.readouterr()
    assert "Doctor ID: 1, Name: Dr. Chen, Specialization: Cardiology, Phone: 123456789" in captured.out

def test_list_no_doctors(capsys, doctor_manager):
    # Test listing all doctors when there are no doctors
    doctor_manager.list_all_doctors()
    captured = capsys.readouterr()
    assert "No doctors available." in captured.out

# Main section to run tests if executing directly
if __name__ == "__main__":
    pytest.main()
