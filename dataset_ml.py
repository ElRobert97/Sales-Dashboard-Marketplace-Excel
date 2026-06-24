import pandas as pd
from sheet_load import SHEET_ML


df_ml = pd.read_excel(SHEET_ML)

print(df_ml)