-- Insertion de données dans la table schools
INSERT INTO schools (name) VALUES 
('École Multimédia'),
('ESTIAM'),
('HETIC');

-- Insertion de données dans la table subjects
INSERT INTO subjects (name) VALUES 
('Web Development'),
('Data Science'),
('Digital Marketing'),
('Graphic Design');

-- Insertion de données dans la table students
INSERT INTO students (name, email, school_id) VALUES 
('Alice Dupont', 'alice.dupont@example.com', 1),
('Bob Martin', 'bob.martin@example.com', 1),
('Claire Petit', 'claire.petit@example.com', 2),
('David Bernard', 'david.bernard@example.com', 3),
('Eve Moreau', 'eve.moreau@example.com', 2),
('Frank Dubois', 'frank.dubois@example.com', 1);

-- Insertion de données dans la table trainers
INSERT INTO trainers (name, email) VALUES 
('Michel', 'michel@example.com'),
('Antoine', 'antoine@example.com'),
('Aurélien', 'aurelien@example.com'),
('Mathieu', 'mathieu@example.com');

-- Insertion de données dans la table invoices
INSERT INTO invoices (invoice_number, payment_due, invoice_wording, days_count, hours_count, unit_price, tva, amount_ht, amount_ttc, intervention_dates, student_count, school_id, trainer_id, subject_id) VALUES 
('INV001', '2024-11-01', 'Cours de Web Development', 1, 10, 50.0, 10.0, 500.0, 550.0, '["2024-10-10"]', 2, 1, 1, 1),
('INV002', '2024-11-02', 'Cours de Data Science', 1, 8, 60.0, 12.0, 480.0, 537.6, '["2024-10-11"]', 1, 2, 2, 2),
('INV003', '2024-11-03', 'Cours de Digital Marketing', 1, 5, 70.0, 14.0, 350.0, 399.0, '["2024-10-12"]', 3, 3, 3, 3),
('INV004', '2024-11-04', 'Cours de Graphic Design', 1, 12, 45.0, 9.0, 540.0, 594.0, '["2024-10-13"]', 4, 1, 1, 4),
('INV005', '2024-11-05', 'Cours de Web Development', 1, 10, 50.0, 10.0, 500.0, 550.0, '["2024-10-14"]', 2, 1, 1, 1),
('INV006', '2024-11-06', 'Cours de Data Science', 1, 8, 60.0, 12.0, 480.0, 537.6, '["2024-10-15"]', 1, 2, 2, 2),
('INV007', '2024-11-07', 'Cours de Digital Marketing', 1, 5, 70.0, 14.0, 350.0, 399.0, '["2024-10-16"]', 3, 3, 3, 3),
('INV008', '2024-11-08', 'Cours de Graphic Design', 1, 12, 45.0, 9.0, 540.0, 594.0, '["2024-10-17"]', 4, 1, 1, 4),
('INV009', '2024-11-09', 'Cours de Web Development', 1, 10, 50.0, 10.0, 500.0, 550.0, '["2024-10-18"]', 2, 1, 1, 1),
('INV010', '2024-11-10', 'Cours de Data Science', 1, 8, 60.0, 12.0, 480.0, 537.6, '["2024-10-19"]', 1, 2, 2, 2);
