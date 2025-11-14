import pandas as pd
from sqlalchemy import text
from db import get_engine

engine = get_engine()

# Exoplanets
exo = pd.read_sql("select * from raw.exoplanets", engine)
neo = pd.read_sql(
    "select des, cd as close_time, dist_au, v_rel_kms from raw.neo_close_approaches",
    engine
)
neo["body"] = "Earth"
stars = pd.read_sql("select hip, proper, dist_pc from raw.hyg_stars", engine)

p = exo.copy()
p["radius_re"] = pd.to_numeric(p["pl_rade"], errors="coerce")
p["orbital_period_d"] = pd.to_numeric(p["pl_orbper"], errors="coerce")
p["eq_temp_k"] = pd.to_numeric(p["pl_eqt"], errors="coerce")
p["host_dist_pc"] = pd.to_numeric(p["sy_dist"], errors="coerce")
p["is_potentially_rocky"] = p["radius_re"].between(0.5, 1.8, inclusive="both")

dim_planet = p[[
  "planet_name","hostname","disc_year","radius_re","orbital_period_d","eq_temp_k","host_dist_pc","is_potentially_rocky"
]].rename(columns={"hostname":"host_name"})

# Curated tables
with engine.begin() as conn:
    conn.execute(text("truncate table curated.dim_planet"))
dim_planet.to_sql("dim_planet", engine, schema="curated", if_exists="append", index=False)

with engine.begin() as conn:
    conn.execute(text("truncate table curated.fact_close_approach"))
neo.to_sql("fact_close_approach", engine, schema="curated", if_exists="append", index=False)

with engine.begin() as conn:
    conn.execute(text("truncate table curated.dim_star"))
stars.to_sql("dim_star", engine, schema="curated", if_exists="append", index=False)

print("Transformations complete.")
