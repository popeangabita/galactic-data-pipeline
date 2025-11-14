create schema if not exists curated;
create table if not exists curated.dim_star (
  star_id serial primary key,
  hip int, 
  proper text, 
  ra double precision, 
  dec double precision, 
  dist_pc double precision, 
  spect text
);

create table if not exists curated.dim_planet (
  planet_id serial primary key,
  planet_name text, 
  host_name text, 
  disc_year int,
  radius_re double precision, 
  orbital_period_d double precision,
  eq_temp_k double precision, 
  host_dist_pc double precision,
  is_potentially_rocky boolean
);

create table if not exists curated.fact_close_approach (
  event_id serial primary key,
  des text, 
  close_time timestamptz, 
  dist_au double precision, 
  v_rel_kms double precision, 
  body text
);
