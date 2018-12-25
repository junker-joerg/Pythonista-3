#python
# 26.10 Was gelernt:
# "global" nutzen, um Variablen ausserhalb von Funktionen zu nutzen
# mehr numpy - hier "recarray"
#  

import logging
import logging.handlers as handlers
import sqlite3
import numpy as np
import json

def haupttabelleAnlegen():
	global haupttabelle
	haupttabelle = np.recarray(3, dtype={'names': ('Jahr', 'Wert', 'Kommentar'), 'formats':('i4','f4','U90')})
	haupttabelle["Jahr"] = ("2010", "2011", "2012")
	haupttabelle["Wert"] = ("100", "200", "300")	
	logger.info("Haupttabelle angelegt")

	
if __name__ == "__main__":
	# starte logging
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')	
	logHandler = logging.FileHandler('mk_26_10_18a.log', mode="a")	
	logHandler.setFormatter(formatter)
	logger.addHandler(logHandler)	
	logger.info("Starte Logging")
	haupttabelleAnlegen()
	#print(haupttabelle["Jahr"])
	#Verarbeitung
	#JSON-Speichern 
	#sql-lite speichern
