from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional


class Person(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_info(self) -> str:
        pass


class Doctor(Person):
    def __init__(self, name: str, age: int, gender: str, faculty: str, room_number: str):
        super().__init__(name, age, gender)
        self.faculty = faculty
        self.room_number = room_number
        self.appointments: List[Appointment] = []

    def get_info(self) -> str:
        return f"Dr. {self.name}, {self.faculty}, Room {self.room_number}"

    def add_appointment(self, appointment: 'Appointment') -> None:
        self.appointments.append(appointment)


class Patient(Person):
    def __init__(self, name: str, age: int, gender: str, med: str, phone_number: str, problems: List[str]):
        super().__init__(name, age, gender)
        self.med = med
        self.phone_number = phone_number
        self.problems = problems
        self.appointments: List[Appointment] = []

    def get_info(self) -> str:
        return f"{self.name}, Medical ID: {self.med}, Phone: {self.phone_number}"

    def add_appointment(self, appointment: 'Appointment') -> None:
        self.appointments.append(appointment)


class Appointment:
    def __init__(self, doctor: Doctor, patient: Patient, time: datetime, duration: int = 30):
        self.doctor = doctor
        self.patient = patient
        self.time = time
        self.duration = duration
        self.status = "Scheduled"

    def __str__(self) -> str:
        return (f"Appointment with Dr. {self.doctor.name} "
                f"for {self.patient.name} "
                f"at {self.time.strftime('%Y-%m-%d %H:%M')}")

    def reschedule(self, new_time: datetime) -> None:
        self.time = new_time

    def cancel(self) -> None:
        self.status = "Cancelled"


class ReceptionSystem:
    def __init__(self):
        self.doctors: List[Doctor] = []
        self.patients: List[Patient] = []
        self.appointments: List[Appointment] = []

    def register_doctor(self, doctor: Doctor) -> None:
        self.doctors.append(doctor)

    def register_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def create_appointment(self, doctor: Doctor, patient: Patient, time: datetime) -> Appointment:
        for existing_appt in doctor.appointments:
            if existing_appt.time == time:
                raise ValueError("Doctor already has an appointment at this time")

        appointment = Appointment(doctor, patient, time)

        doctor.add_appointment(appointment)
        patient.add_appointment(appointment)
        self.appointments.append(appointment)

        return appointment

    def view_doctor_appointments(self, doctor: Doctor) -> List[Appointment]:
        return doctor.appointments

    def view_patient_appointments(self, patient: Patient) -> List[Appointment]:
        return patient.appointments

    def find_available_doctors(self, time: datetime) -> List[Doctor]:
        return [
            doctor for doctor in self.doctors
            if not any(appt.time == time for appt in doctor.appointments)
        ]


def main():
    reception = ReceptionSystem()

    dr_smith = Doctor("Smith", 45, "Male", "Cardiology", "101")
    dr_jones = Doctor("Jones", 38, "Female", "Pediatrics", "202")
    reception.register_doctor(dr_smith)
    reception.register_doctor(dr_jones)

    patient1 = Patient("John Doe", 35, "Male", "MED001", "555-1234", ["Heart checkup"])
    patient2 = Patient("Jane Smith", 28, "Female", "MED002", "555-5678", ["Child vaccination"])
    reception.register_patient(patient1)
    reception.register_patient(patient2)

    appointment_time = datetime(2024, 1, 15, 10, 0)
    appointment = reception.create_appointment(dr_smith, patient1, appointment_time)

    print(appointment)
    print("Dr. Smith's Appointments:", [str(appt) for appt in reception.view_doctor_appointments(dr_smith)])


if __name__ == "__main__":
    main()