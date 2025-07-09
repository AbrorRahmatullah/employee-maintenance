CREATE TABLE employees_employee (
    id SERIAL PRIMARY KEY,                    -- Kolom id otomatis
    first_name VARCHAR(50) NOT NULL,         -- Kolom untuk nama depan
    last_name VARCHAR(50) NOT NULL,          -- Kolom untuk nama belakang
    email VARCHAR(254) UNIQUE NOT NULL,      -- Kolom untuk email, unik
    phone VARCHAR(15),                        -- Kolom untuk nomor telepon
    department VARCHAR(100),                  -- Kolom untuk departemen
    position VARCHAR(100),                    -- Kolom untuk posisi
    hire_date DATE NOT NULL                   -- Kolom untuk tanggal perekrutan
);
