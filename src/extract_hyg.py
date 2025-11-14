import pandas as pd
from db import get_engine

df = pd.read_csv("data/hyg.csv")
df.rename(columns={"dist":"dist_pc"}, inplace=True)

engine = get_engine()
df.to_sql("hyg_stars", engine, schema="raw", if_exists="replace", index=False)
