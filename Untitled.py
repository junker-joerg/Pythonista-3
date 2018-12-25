# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_csv(
"data.csv", # Dateiname - bei gleichem Verzeichnis
sep = ";" # Separator - hier aus Excel festgelegt
)
#TODO: wie funktioniert "drucken" bei pandas?
#? oder geht es auch in Spalten
# * WICHTIG
print(data.head())

