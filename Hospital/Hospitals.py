
import Patients

class Hospital():	
	BedNum = 0	
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients_list = []		
	def displayPatientInfo(self):		
		for patient in self.patients_list:
			print patient			
	def discharge(self, patientName):			
		if(len(self.patients_list) > 0):
			for patient in range(0, len(self.patients_list)):
				if self.patients_list[patient].name == patientName:
					self.patients_list[patient].bedNum = "none"
					self.patients_list.pop(patient)
					break			
	def admit(self, *newPatient):
		if len(self.patients_list) == int(self.capacity):
			print "Hospital is full"
		else:				
			Hospital.BedNum += 1
			for patient in newPatient:
				self.patients_list.append(patient)
				patient.bedNum = Hospital.BedNum 			
	def __repr__(self):
		return "\nName: {}\nCapacity: {}\n".format(self.name, self.capacity)
hospital = Hospital("inova", "2")
#print hospital
pat1 = Patients.Patient("test", "none")
pat2 = Patients.Patient("test2", "dust")
pat3 = Patients.Patient("test3", "none")
hospital.admit(pat1)
hospital.admit(pat2)
hospital.admit(pat3)
#hospital.displayPatientInfo()
#hospital.discharge("test")
hospital.displayPatientInfo()