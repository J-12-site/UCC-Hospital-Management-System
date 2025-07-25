# 🏥 ADISALI Hospital Management System - Powered by Innovation, Compassion, and Care

# importing libraries
import sys
import random
from datetime import datetime

def generate_id(prefix):
    return f"{prefix}-{random.randint(10000,99999)}"

def is_time_available(schedule, date, time):
    return (date ,time) not in schedule

# CLASS: Person( Parent Class)
# Represents a generic person with name, age, and gender.

class Person:
    def __init__(self, name, age, gender):
        self.name   = name
        self.age    = age
        self.gender = gender

# CLASS: Patient
# Add fields for patient_id and appointment_list

class Patient(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.patient_id = generate_id("P")
        self.appointments = []

        # Add an appointment to the patient's list


#CLASS: Doctor
# Inputs doctor_id, speciality, and schedule

class Doctor(Person):
    def __init__(self, name, age, gender, speciality):
        super().__init__(name, age, gender)
        self.doctor_id  = generate_id("D")
        self.speciality = speciality
        self.schedule   = []

    def is_available(self, date, time):
        return is_time_available(self.schedule, date, time)


# CLASS: Appointment Scheduling

# Appointment between patient and doctor

class Appointment:
    def __init__(self,patient, doctor, date, time):
        self.appointment_id = generate_id("A")
        self.patient = patient
        self.doctor  = doctor
        self.date    = date
        self.time    = time

    def confirm(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n📅 Appointment Booked Successfully!")
        print(f"🔖 Appointment ID: {self.appointment_id}")
        print(f"📍 Date & Time: {self.date} at {self.time}")
        print(f"👨‍⚕️ Doctor: {self.doctor.name} ({self.doctor.speciality})")
        print(f"🧍‍♀️ Patient: {self.patient.name}")
        print(f"🕓 Timestamp: {now}")
        print("✅ Please arrive 15 minutes early.\n")

# This class defines the Hospital_system which manages data for patients, doctors, and appointments.
# CLASS: Hospital_Management_System

class Hospital_Management_System:
    def __init__(self):
        self.patients     = {}
        self.doctors      = {}
        self.appointments = {}

# Register a new patient and adds it to the system
    def register_patient(self):
        print("\n 📝 New Patient Registration")
        try:
            name = input("👤 Enter Patient Name: ")
            age = int(input("🎂 Age: "))
            gender = input("🚻 Gender (M/F/O): ")
            patient = Patient(name, age, gender)
            self.patients[patient.patient_id] = patient
            print(f"\n ****Registration successfully completed****")
            print(f"✅Patient registered successfully. 🆔 ID is: {patient.patient_id}\n")
        except ValueError:
            print("❌Invalid input. Please enter a valid age in numbers!")


# Register a new doctor and adds it to the system

    def register_doctor(self):
        print("\n 🩺 New Doctor Registration")
        try:
            name = input("👨‍⚕️ Full Name:")
            age = int(input("🎂 Age: "))
            gender = input("🚻 Gender (M/F/O): ")
            speciality = input("💼 Speciality: ")
            doctor = Doctor(name, age, gender, speciality)
            self.doctors[doctor.doctor_id] = doctor
            print(f"✅Doctor registered successfully. 🆔 ID: {doctor.doctor_id}\n")
        except ValueError:
            print("❌ Invalid input. Please enter a valid age in numbers!")


# Book an appointment for a patient with a doctor

    def book_appointment(self):
        print("\n📆 Booking Appointment")
        patient_id = input("🔍 Enter Patient ID:  ")
        doctor_id = input("🔍 Enter Doctor ID: ")

        if patient_id not in self.patients or doctor_id not in self.doctors:
            print("❌ Invalid data received (Patient & Doctor ID. \n")
            return

        date = input("📅 Date (YYYY-MM-DD): ")
        time = input("🕒 Time :  ")

    # Check if doctor is available

        doctor = self.doctors[doctor_id]
        if doctor.is_available(date, time):
            appointment = Appointment(self.patients[patient_id], doctor, date, time)
            self.appointments[appointment.appointment_id] = appointment
            self.patients[patient_id].appointments.append(appointment)
            doctor.schedule.append((date, time))
            appointment.confirm()
        else:
            print("⚠️ Sorry, doctor not available at that time.\n")

    # Cancel an appointment and update records

    def cancel_appointment(self):
        print("\n❌ Cancel Appointment")
        appointment_id = input("🔍 Enter Appointment ID: ")
        appointment= self.appointments.get(appointment_id)

        if appointment:
            appointment.doctor.schedule.remove((appointment.date, appointment.time))
            appointment.patient.appointments.remove(appointment)
            del self.appointments[appointment_id]
            print(f"🗑️ Appointment {appointment_id} cancelled successfully.\n")
        else:
            print("❌ Appointment not found.\n")


    # Display doctor's appointment schedule

    def view_doctor_schedule(self):
        print("\n 📖 View Doctor Schedule")
        doctor_id = input("🔍 Enter Doctor ID: ")
        doctor = self.doctors.get(doctor_id)
        if doctor:
            print(f"\n🩺 Dr. {doctor.name} ({doctor.speciality})'s Schedule:")
            if doctor.schedule:
                for date, time in doctor.schedule:
                    print(f"📅 {date} at {time}")
            else:
                print("📭 No appointments scheduled.")
        else:
            print("❌ Doctor not found.\n")

    def view_patient_profile(self):
        print("\n 🧾 View Patient Details")
        patient_id = input("🔍 Enter Patient ID: ")
        patient = self.patients.get(patient_id)
        if patient:
            print(f"\n👤 {patient.name} | 🎂 Age: {patient.age} | 🚻 Gender: {patient.gender}")
            print(f"🆔 ID: {patient.patient_id}")
            print("📅 Appointments:")
            if patient.appointments:
                for appt in patient.appointments:
                    print(f"- {appt.date} at {appt.time} with Dr. {appt.doctor.name} ({appt.doctor.speciality})")
            else:
                print("🗃️ No appointments found.")
        else:
            print("❌ Patient not found.\n")

    # Generate and print the bills for an appointment

    def generate_bill(self):
        print("\n💳 Generate Medical Bill")
        appointment_id = input("🔍 Enter Appointment ID: ")
        appointment = self.appointments.get(appointment_id)

        if not appointment:
            print("❌ Appointment not found.\n")
            return

    # Print hospital and appointment details

        print("\֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍")
        print("n  ADISALI HOSPITAL RECORD - Westtree District, Ocho Rios   ")
        print("             Tel: 876-345-0986 ׀ adisali.com                  ")
        print("\֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍֍")
        print(f"👤Patient:  {appointment.patient.name}")
        print(f"👨‍⚕️Doctor: {appointment.doctor.name}  ({appointment.doctor.speciality})")
        print(f"📅 Date & Time: {appointment.date} at {appointment.time}")
        print("------------------------------------------------------------------------------")

# Calculate bill

        consultation_fee = 3000
        print(f"💰Consultation fee: JMD ${consultation_fee}")
        try:
            extra_fees = float(input("➕ Enter any additional charges below (test/meds): JMD $"))
            if extra_fees < 0:
                raise ValueError
        except ValueError:
            print("⚠️Invalid input. Setting Extra fee to 0.")
            extra_fees = 0

        total = consultation_fee + extra_fees
        print("*************************************************************")
        print(f"🧾TOTAL BILL: JMD $ {total}")
        print("✅ Payment can be made via cash, card or bank transfer.\n")



# Main Program Loop

def main():
    hospital = Hospital_Management_System()
    print("\n🏥 Welcome to ADISALI Hospital Management System")
    print("🔷 Innovating Care. Empowering Health. Since 2002.")
    print(" Select a menu option to continue \n")

    while True:
        print("\n🧭 MAIN MENU")
        print(" 1️⃣Let’s Register a Patient")
        print(" 2️⃣ Register new Doctor")
        print(" 3️⃣Book Appointment")
        print(" 4️⃣Cancel Appointment")
        print(" 5️⃣ Doctors Schedule")
        print(" 6️⃣View Patient Profile")
        print(" 7️⃣Generate Patient Bill")
        print(" 8️⃣Exit \n")
        print("===================================")

        option = input("👉 Select an option (1-8): ")

        # Register New Patient
        if option == "1":
            hospital.register_patient()

        # Add New Doctor
        elif option == "2":
            hospital.register_doctor()

        # Book Appointment
        elif option == "3":
            hospital.book_appointment()

        # Cancel Appointment
        elif option == "4":
            hospital.cancel_appointment()

        # View Doctor Schedule
        elif option == "5":
            hospital.view_doctor_schedule()

        # View Patient Profile
        elif option == "6":
            hospital.view_patient_profile()

        # Generate Patient Bill
        elif option == "7":
            hospital.generate_bill()

        elif option == "8":
            print("\n👋 Thank you for using ADISALI HMS. ")
            print("💙 Stay healthy. Goodbye and take care!")
            sys.exit()
        else:
            print("❌ Invalid choice. Please try again.\n")

# Only runs main when you execute this file directly
if __name__ == "__main__":
    main()



