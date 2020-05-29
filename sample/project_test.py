class Woman:
	def __init__(self,num1,num2,num3):
		self.weight = num1
		self.iq = num2
		self.height = num3

	def eat(self):
		print("몸무게는 : " + self.weight)

	def study(self):
		print("iq는 : " + self.iq)

	def sleep(self):
		print("키는 : " + self.height)

	def show(self):
		print("몸무게는 : " + self.weight + " id는 : " + self.iq + " 키는 : " + self.height)



#psi = Woman("90","60")
#psi.eat()