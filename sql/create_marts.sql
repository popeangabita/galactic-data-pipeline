create schema if not exists mart;

-- Habitable Candidates View
create or replace view mart.habitable_candidates as
select planet_name,
       host_name,
       radius_re,
       orbital_period_d,
       coalesce(eq_temp_k, pl_eqt_est) as eq_temp_k,
       host_dist_pc
from (
    select p.*,
           case
               when eq_temp_k is null and host_dist_pc is not null
               then null -- keep simple
               else eq_temp_k
           end as pl_eqt_est
    from curated.dim_planet p
) t
where radius_re between 0.5 and 1.8
  and (eq_temp_k between 180 and 310 or eq_temp_k is null);

-- when/where asterorids are coming near Earth
create or replace view mart.upcoming_neo_events as
select des,
       min(close_time) as next_approach,
       min(dist_au) as min_dist_au
from curated.fact_close_approach
where close_time >= now()
  and body = 'Earth'
group by des
order by min_dist_au asc
limit 50;
