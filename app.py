from prefab_ui.app import PrefabApp
from prefab_ui.components.charts import BarChart, ChartSeries
from dataset_shopee import df_shopee



grouped = df_shopee.groupby(by="UF")["Valor_Total"].sum().sort_values(ascending=False).reset_index()

json_grouped = grouped.to_dict(orient="records")

# with PrefabApp() as app:

#     BarChart(
#         data=json_grouped,
#         series=[
#             ChartSeries(data_key="Valor_Total", label="Valor Total"),
#         ],
#         x_axis="UF",
#     )
                