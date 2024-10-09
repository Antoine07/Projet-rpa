CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    action VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE role_permission (
    id SERIAL PRIMARY KEY,
    role_id INT REFERENCES Role(id) ON DELETE CASCADE,
    permission_id INT REFERENCES Permission(id) ON DELETE CASCADE
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    role_id INT REFERENCES Role(id) ON DELETE SET NULL
);

CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(10) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date de création
    payment_due VARCHAR(50),
    invoice_wording VARCHAR(255),
    days_count INT NOT NULL,
    hours_count INT NOT NULL,
    unit_price FLOAT,
    tva FLOAT,
    amount_ht FLOAT,
    amount_ttc FLOAT,
    intervention_dates JSONB,
    student_count INT, -- Champ pour le nombre d'étudiants
    school_id INT REFERENCES School(id), -- Relation avec la table School
    trainer_id INT REFERENCES Trainer(id), -- Relation avec la table Trainer
    subject_id INT REFERENCES Subject(id) -- Relation avec la table Subject
);


ALTER TABLE invoices
ADD COLUMN creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date de création
ADD COLUMN student_count INT; -- Champ pour le nombre d'étudiants

-- Data

-- Insertion des rôles
INSERT INTO roles (name) VALUES
('Admin'),
('User'),
('Trainer');

-- Insertion des permissions
INSERT INTO permissions (action, description) VALUES
('create_invoice', 'Permission to create invoices'),
('view_invoice', 'Permission to view invoices'),
('edit_invoice', 'Permission to edit invoices'),
('delete_invoice', 'Permission to delete invoices');

-- Insertion des relations rôle-permission
INSERT INTO role_permission (role_id, permission_id) VALUES
(1, 1), -- Admin can create invoices
(1, 2), -- Admin can view invoices
(1, 3), -- Admin can edit invoices
(1, 4), -- Admin can delete invoices
(2, 2), -- User can view invoices
(2, 3); -- User can edit invoices

-- Insertion des utilisateurs
INSERT INTO users (email, password, firstname, lastname, role_id) VALUES
('admin@example.com', 'adminpassword', 'Admin', 'User', 1),
('user@example.com', 'userpassword', 'John', 'Doe', 2),
('trainer@example.com', 'trainerpassword', 'Jane', 'Smith', 3);

-- Insertion des écoles
INSERT INTO schools (name) VALUES
('School of Engineering'),
('School of Arts'),
('School of Science');

-- Insertion des formateurs
INSERT INTO trainers (name) VALUES
('Alice Johnson'),
('Bob Brown'),
('Charlie Davis');

-- Insertion des matières
INSERT INTO subjects (name) VALUES
('Mathematics'),
('History'),
('Biology');

-- Insertion de 10 factures
INSERT INTO invoices (
    invoice_number, 
    creation_date, 
    payment_due, 
    invoice_wording, 
    days_count, 
    hours_count, 
    unit_price, 
    tva, 
    amount_ht, 
    amount_ttc, 
    intervention_dates, 
    student_count, 
    school_id, 
    trainer_id, 
    subject_id
) VALUES
('INV001', NOW(), '2024-10-30', 'Invoice for Math Course', 5, 40, 100.00, 20.00, 5000.00, 6000.00, '{"dates":["2024-10-01","2024-10-02"]}', 30, 1, 1, 1),
('INV002', NOW(), '2024-11-15', 'Invoice for History Course', 3, 24, 150.00, 30.00, 3600.00, 4320.00, '{"dates":["2024-10-03","2024-10-04"]}', 25, 2, 2, 2),
('INV003', NOW(), '2024-12-01', 'Invoice for Biology Course', 7, 56, 200.00, 40.00, 11200.00, 13440.00, '{"dates":["2024-10-05","2024-10-06"]}', 20, 3, 3, 3),
('INV004', NOW(), '2024-10-31', 'Invoice for Physics Course', 4, 32, 120.00, 24.00, 3840.00, 4608.00, '{"dates":["2024-10-07","2024-10-08"]}', 28, 1, 1, 1),
('INV005', NOW(), '2024-11-10', 'Invoice for Chemistry Course', 5, 40, 180.00, 36.00, 7200.00, 8640.00, '{"dates":["2024-10-09","2024-10-10"]}', 22, 2, 2, 2),
('INV006', NOW(), '2024-11-20', 'Invoice for English Course', 6, 48, 110.00, 22.00, 5280.00, 6336.00, '{"dates":["2024-10-11","2024-10-12"]}', 30, 3, 3, 3),
('INV007', NOW(), '2024-12-15', 'Invoice for Art Course', 2, 16, 200.00, 40.00, 3200.00, 3840.00, '{"dates":["2024-10-13","2024-10-14"]}', 15, 1, 1, 3),
('INV008', NOW(), '2024-12-20', 'Invoice for Music Course', 3, 24, 250.00, 50.00, 6000.00, 7200.00, '{"dates":["2024-10-15","2024-10-16"]}', 18, 2, 2, 2),
('INV009', NOW(), '2024-12-30', 'Invoice for Philosophy Course', 5, 40, 300.00, 60.00, 12000.00, 14400.00, '{"dates":["2024-10-17","2024-10-18"]}', 10, 3, 3, 1),
('INV010', NOW(), '2024-12-31', 'Invoice for Computer Science Course', 6, 48, 150.00, 30.00, 7200.00, 8640.00, '{"dates":["2024-10-19","2024-10-20"]}', 20, 1, 1, 3);

