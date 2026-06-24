import pandas as pd
from sheet_load import SHEET_SHOPEE
 
df_shopee = pd.read_excel(SHEET_SHOPEE)
df_shopee = df_shopee[["UF", "Valor Total", "Quantidade", "Nº de referência do SKU principal"]]
df_shopee = df_shopee.rename(columns={"Valor Total": "Valor_Total"})
df_shopee["Valor Total"] = df_shopee["Valor_Total"].astype(float)
df_shopee["UF"] = df_shopee["UF"].astype(str)
