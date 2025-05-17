CREATE TABLE IF NOT EXISTS public.users
(
    id SERIAL PRIMARY KEY,
    email VARCHAR(150),
    password_hash VARCHAR(128),
    created_at timestamp,
    is_active boolean,
	rol_id NUMERIC 
);

CREATE TABLE IF NOT EXISTS public.readings_raw
(
    id SERIAL PRIMARY KEY,
    level numeric,
    time timestamp,
    sensor VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS public.readings_q
(
    id SERIAL PRIMARY KEY,
    level numeric,
    caudal numeric,
    id_read numeric
);

CREATE TABLE IF NOT EXISTS public.roles
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

insert into public.roles (name) values
('visitante'),
('superadministrador'), 
('administrador distrito'), 
('gerente'), 
('jefe operaciones'), 
('inspector')

CREATE TABLE IF NOT EXISTS public.alert_rules
(
    id SERIAL PRIMARY KEY,
    alert_level VARCHAR(50),
	id_sensor VARCHAR(50),
	umb_min numeric,
	umb_max numeric
);

CREATE TABLE IF NOT EXISTS public.alert_rol
(
    id SERIAL PRIMARY KEY,
    id_alert NUMERIC,
	id_rol NUMERIC
);


CREATE TABLE IF NOT EXISTS public.sensors
(
    id SERIAL PRIMARY KEY,
    coord VARCHAR(150),
	state VARCHAR(50),
	id_sensor VARCHAR(50)
);







