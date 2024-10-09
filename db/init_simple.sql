CREATE TABLE Invoice (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(255),
    creation_date TIMESTAMP,
    issue_date DATE,
    payment_due VARCHAR(255),
    invoice_wording VARCHAR(255),
    days_count INT,
    hours_count INT,
    unit_price FLOAT,
    tva FLOAT,
    amount_ht FLOAT,
    amount_ttc FLOAT,
    intervention_dates JSONB,
    student_count INT,
    school VARCHAR(255),
    trainer VARCHAR(255),
    subject VARCHAR(255)
);


INSERT INTO Invoice (invoice_number, creation_date, issue_date, payment_due, invoice_wording, days_count, hours_count, unit_price, tva, amount_ht, amount_ttc, intervention_dates, student_count, school, trainer, subject)
VALUES
('INV001', '2024-01-01 10:00:00', '2024-01-02', '2024-01-15', 'Formation en développement web', 5, 40, 50.00, 20.00, 2000.00, 2400.00, '{"dates": ["2024-01-03", "2024-01-10"]}', 20, 'École A', 'Formateur A', 'Développement Web'),
('INV002', '2024-02-01 11:00:00', '2024-02-02', '2024-02-15', 'Atelier sur la gestion de projet', 3, 24, 70.00, 20.00, 1680.00, 2016.00, '{"dates": ["2024-02-05"]}', 15, 'École B', 'Formateur B', 'Gestion de Projet'),
('INV003', '2024-03-01 09:30:00', '2024-03-02', '2024-03-15', 'Séminaire sur l accessibilité', 2, 16, 60.00, 20.00, 960.00, 1152.00, '{"dates": ["2024-03-08"]}', 10, 'École C', 'Formateur C', 'Accessibilité'),
('INV004', '2024-04-01 14:00:00', '2024-04-02', '2024-04-15', 'Cours de data science', 7, 56, 80.00, 20.00, 4480.00, 5376.00, '{"dates": ["2024-04-10", "2024-04-12"]}', 25, 'École D', 'Formateur D', 'Data Science'),
('INV005', '2024-05-01 08:45:00', '2024-05-02', '2024-05-15', 'Formation en marketing digital', 4, 32, 55.00, 20.00, 1760.00, 2112.00, '{"dates": ["2024-05-05"]}', 12, 'École E', 'Formateur E', 'Marketing Digital'),
('INV006', '2024-06-01 13:00:00', '2024-06-02', '2024-06-15', 'Webinaire sur l UX design', 1, 8, 90.00, 20.00, 720.00, 864.00, '{"dates": ["2024-06-10"]}', 30, 'École F', 'Formateur F', 'UX Design'),
('INV007', '2024-07-01 15:30:00', '2024-07-02', '2024-07-15', 'Atelier de codage', 5, 40, 50.00, 20.00, 2000.00, 2400.00, '{"dates": ["2024-07-03", "2024-07-10"]}', 18, 'École G', 'Formateur G', 'Codage'),
('INV008', '2024-08-01 16:00:00', '2024-08-02', '2024-08-15', 'Formation en cybersécurité', 6, 48, 100.00, 20.00, 4800.00, 5760.00, '{"dates": ["2024-08-05", "2024-08-12"]}', 22, 'École H', 'Formateur H', 'Cybersécurité'),
('INV009', '2024-09-01 10:30:00', '2024-09-02', '2024-09-15', 'Séance de coaching en carrière', 4, 32, 75.00, 20.00, 2400.00, 2880.00, '{"dates": ["2024-09-05"]}', 8, 'École I', 'Formateur I', 'Coaching'),
('INV010', '2024-10-01 11:15:00', '2024-10-02', '2024-10-15', 'Formation en gestion des données', 3, 24, 85.00, 20.00, 2040.00, 2448.00, '{"dates": ["2024-10-08"]}', 14, 'École J', 'Formateur J', 'Gestion des Données');
