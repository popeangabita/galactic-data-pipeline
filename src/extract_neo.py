import requests, pandas as pd
from datetime import date, timedelta
from db import get_engine

base = "https://ssd-api.jpl.nasa.gov/cad.api"
today = date.today()
params = {
  "date-min": (today - timedelta(days=1)).isoformat(),
  "date-max": (today + timedelta(days=30)).isoformat(),
  "dist-max": "0.5",
  "body": "Earth",
  "sort": "date",
  "fullname": "true"
}
r = requests.get(base, params=params, timeout=60).json()
cols = r["fields"]; rows = r["data"]
df = pd.DataFrame(rows, columns=cols)
df = df.rename(columns={"des":"des","cd":"cd","dist":"dist_au","v_rel":"v_rel_kms"})
df["dist_au"] = pd.to_numeric(df["dist_au"], errors="coerce")
df["v_rel_kms"] = pd.to_numeric(df["v_rel_kms"], errors="coerce")

engine = get_engine()
df.to_sql("neo_close_approaches", engine, schema="raw", if_exists="append", index=False)
