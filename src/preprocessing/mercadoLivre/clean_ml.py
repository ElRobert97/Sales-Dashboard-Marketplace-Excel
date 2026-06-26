from pathlib import Path
import pandas as pd

cwd = Path.cwd()

sheet = cwd / "data/raw/dataset_ml_062025_06_2026.xlsx"

df = pd.read_excel(sheet, skiprows=5)
"""
Total (BRL) = Receita por produtos (BRL) + Receita por acréscimo no preço (pago pelo comprador)	 + Receita por envio (BRL)
- Taxa de parcelamento equivalente ao acréscimo - Tarifa de venda e impostos (BRL) - Tarifas de envio (BRL)
"""
select_columns =[
    'Data da venda',
    'Unidades',
    'Receita por produtos (BRL)',
    'Receita por acréscimo no preço (pago pelo comprador)',
    'Taxa de parcelamento equivalente ao acréscimo',
    'Tarifa de venda e impostos (BRL)',
    'Receita por envio (BRL)',
    'Tarifas de envio (BRL)',
    'Custo de envio por troca de produto',
    'Custo de envio com base nas medidas e peso declarados',
    'Custo por diferenças nas medidas e no peso do pacote',
    'Descontos e bônus',
    'Cancelamentos e reembolsos (BRL)',
    'Total (BRL)',
    'Venda por publicidade',
    'SKU',
    '# de anúncio',
    'Canal de venda',
    'Título do anúncio',
    'Variação',
    'Preço unitário de venda do anúncio (BRL)',
    'Cidade',
    'Estado.1',
    'CEP',
    'Reclamação aberta',
    'Reclamação encerrada',
 ]
df = df[select_columns]
