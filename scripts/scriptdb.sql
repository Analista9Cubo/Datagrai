CREATE TABLE IF NOT EXISTS public.users
(
    id SERIAL PRIMARY KEY,
    email VARCHAR(150),
    password_hash VARCHAR(128),
    created_at timestamp,
    is_active boolean
);
