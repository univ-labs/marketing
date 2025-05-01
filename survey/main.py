import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame

from rename import rename_columns, rename_ciphers

df: DataFrame = pd.read_excel("data.xlsx", skiprows=3)
df = df.iloc[:, 3:]
df = rename_columns(df)

df['Шифр'] = rename_ciphers(df['Шифр'])

# for idx, col in enumerate(df.columns):
#     if col in ["Шифр", "комментарии"]:
#         continue
#
#     title = f"Оценка {col}"
#
#     plt.figure(figsize=(9, 6))
#     df[col].value_counts().sort_index().plot(kind="bar")
#
#     plt.title(title)
#     plt.xlabel("Оценка")
#     plt.ylabel("Количество ответов")
#     plt.grid(axis="y")
#     plt.tight_layout()
#     plt.savefig(f"images/{idx + 1}_{col}.png")
#     plt.close()
#
#     print(f"График {title} сделан...")

grouped = df.groupby(["Шифр", "комментарии"]).size().reset_index(name='count')
pivoted = grouped.pivot(index="Шифр", columns="комментарии", values="count").fillna(0)
print(pivoted)
