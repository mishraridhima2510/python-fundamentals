# Hospital System

class Person:

    def info(self):
        print("Person Information")

class Doctor(Person):

    def department(self):
        print("Cardiology")

doctor = Doctor()

doctor.info()
doctor.department()
