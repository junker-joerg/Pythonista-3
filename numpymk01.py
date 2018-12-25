import numpy as np

a = np.array(
								([1,2,3],
								[4,5,6],
								[7,8,9]), dtype=float
								)
print(a)
							

class Consumer:
	def __init__(self, w):
		"Initialize consumer with w dollars of wealth"
		self.wealth = w
	def earn(self, y):
		"The consumer earns y dollars"
		self.wealth += y
	def spend(self, x):
		"The consumer spends x dollars if feasible"
		new_wealth = self.wealth - x
		if new_wealth < 0:
			print("Insufficent funds")
		else:
			self.wealth = new_wealth

class botText:
	""" 
	hiermit wird ein eigener namespace
	erstellt der mit "self" adressiert
	wird. 
	"""	
	def __init(self, textin, textout, a,b):
		self.textin, self.textout, self.a, self.b 	= textin, textout, a, b 
			 			 	 			 
bot = botText("Z","2",3,4)
b = range(3)
j=1
for i in b:
	for j in b:
		a[i][j]	= 2						
print("\n")
print(a)		
