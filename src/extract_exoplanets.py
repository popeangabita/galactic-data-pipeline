import requests, io, pandas as pd
from db import get_engine

API = ("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?"
       "query=select+*+from+pscomppars&format=csv")

df = pd.read_csv(io.BytesIO(requests.get(API, timeout=60).content))

keep = {
  "hostname":"hostname", "pl_name":"planet_name", "disc_year":"disc_year",
  "pl_rade":"pl_rade", "pl_orbper":"pl_orbper",
  "st_teff":"st_teff", "st_rad":"st_rad", "sy_dist":"sy_dist", "pl_eqt":"pl_eqt"
}
df = df.rename(columns=keep)[list(keep.values())]

engine = get_engine()
df.to_sql("exoplanets", engine, schema="raw", if_exists="append", index=False)
