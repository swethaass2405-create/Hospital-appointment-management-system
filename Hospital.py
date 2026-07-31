appointments = []

name = input("Enter Patient Name: ")
doctor = input("Enter Doctor Name: ")

appointments.append([name, doctor])

print("\nAppointment Details")
for app in appointments:
    print("Patient:", app[0])
    print("Doctor :", app[1])