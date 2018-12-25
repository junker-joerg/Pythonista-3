import numpy as np
from io import BytesIO
import json
# Use a compound data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})

data = (
				["Martin", 52, 91],
				["Sandra", 51, 89],
				["Antje", 54, 60],
				["Nette", 60,90]
				)

#Einfacher Loop
for i in range(10)
	#code
	pass



test = np.arange(15).reshape(3,5)
"""
	testmatrix ... Format
	... und noch ne Zeile
"""
									
#print(json.dumps(data))
				
i = 1
'Das ist eine Matrix'
"Man läuft über die Diagonale"
for i in range(3):
		test[i,i] = 7
		print(test[i,i])

				
