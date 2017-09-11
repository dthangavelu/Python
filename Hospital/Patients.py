
class Patient(object):
	Id = 0
	def __init__(self, name, allergies):
		Patient.Id += 1
		self.Id = Patient.Id
		self.name = name
		self.allergies = allergies
		self.bedNum = "none"
	def __str__(self):
		return "\nId: {}\nName: {}\nAllergies: {}\nBedNumber: {}\n".format(self.Id, self.name, self.allergies, self.bedNum)
#pat1 = Patient("test", "none")
#print pat1
#pat2 = Patient("test", "none")
#print pat2
#pat3 = Patient("test", "none")
#print pat3