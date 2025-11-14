create schema if not exists raw;
create table if not exists raw.exoplanets (
  loaded_at timestamptz default now(),
  hostname text, planet_name text, disc_year int,
  pl_rade double precision, pl_orbper double precision,
  st_teff double precision, st_rad double precision,
  sy_dist double precision, -- pc
  pl_eqt double precision,  -- provided when available
  source jsonb
);

create table if not exists raw.neo_close_approaches (
    des text,
    orbit_id text,
    jd text,
    cd text,
    dist_au double precision,
    dist_min text,
    dist_max text,
    v_rel_kms double precision,
    v_inf text,
    t_sigma_f text,
    h text,
    fullname text
);

create table if not exists raw.hyg_stars (
  loaded_at timestamptz default now(),
  id int, 
  hip int, 
  proper text, 
  ra double precision, 
  dec double precision,
  dist_pc double precision, 
  spect text, 
  x double precision, 
  y double precision, 
  z double precision
);