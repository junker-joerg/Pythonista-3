# -*- coding: utf-8 -*-
"""
@author: martin


# WiWi Sim 1
# 15.07.13
# Eine Simulation von Maerkten unterschiedlicher Branchen
# 1. Geldmarkt
# 2. Arbeitsmarkt
# 3. Kreditmarkt
# 4-n: Definierbar oder werden während der Laufzeit entstehen
"""
import pickle
import pprint
import numpy as np

class Datensammler (object):
	def __init__(self):
		self.NumDatenSam = np.array(
																[1,2,3],
																[4,5,6],
																[7,8,9]
																)
																

#richtet eine neue Branche ein
#extern indiziert oder intern - z.b. durch Innovation
class branche(object):
    def __init__(self, branchenschluessel):
        self.Branchenschluessel = branchenschluessel
        pass # construktor
    def __del__(self):
        pass # deconstructor
    
class markt(object):
# richtet einen Markt ein
# periode: ab wann es den Markt gibt
    def __init(self, marktnummer):
        pass
    def __del__(self):
        pass    
    pass
class simulation(object):
    #richtet eine Simulation ein
    def __init__(self):
        pass
    def __del__(self):
        pass
    pass
    

