#python3!

 
import requests
import json
import urllib
import numpy as np

class test:
	def __init__(self, x1,x2,x3):
	self.a, self.b, self.c = x1,x2,x3	

"""
EINE Funkion
Eine Schleife hängt Zufallsdaten an eine Zeitreihen-Struktur
und schreibt sie dann in JSON				
"""				
x = np.zeros((5),dtype={'names': ('Jahr', 'Wert', 'Kommentar'), 
									'formats':('i4','f4','U90')
									} 
					)
					
x[:] = [	(1967,200.5,"Start"),
		(1968,210.0,'Weiter mit eine'),
		(1969,220.3,'ein neuer Höhepunkt'),
		(1970,230.9,'---'),
	  (1971,240.3,'ENDE')
	]

x.dtype.names = ['Jahr', 'Wert', 'Kommentar']				
"""
def meineFunktion():
print("Hier geht es los jetzt")

def holeInput():
mkinpt = input(":")
return mkinpt
"""
if __name__ == "__main__":
	#json.loads(x)
	#print(z.Kommentar)	
	v = test(1,2, "test") 
	print(v.c)
# hier ein neuer Kommentar	


