CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    school_id INT,
    CONSTRAINT fk_school FOREIGN KEY (school_id) 
        REFERENCES schools(id) 
        ON DELETE SET NULL
);

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    hours_count INT
);

-- Table d'association entre les cours et les étudiants
CREATE TABLE course_students (
    course_id INT,
    student_id INT,
    PRIMARY KEY (course_id, student_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) 
        REFERENCES courses(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_student FOREIGN KEY (student_id) 
        REFERENCES students(id) 
        ON DELETE CASCADE
);

-- Table d'association entre les cours et les formateurs
CREATE TABLE course_trainers (
    course_id INT,
    trainer_id INT,
    PRIMARY KEY (course_id, trainer_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) 
        REFERENCES courses(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_trainer FOREIGN KEY (trainer_id) 
        REFERENCES trainers(id) 
        ON DELETE CASCADE
);

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(10) NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_due DATE,
    invoice_wording VARCHAR(255),
    amount_ht FLOAT,
    amount_ttc FLOAT,
    school_id INT,
    course_id INT,
    CONSTRAINT fk_school FOREIGN KEY (school_id) 
        REFERENCES schools(id) ON DELETE SET NULL,
    CONSTRAINT fk_course FOREIGN KEY (course_id) 
        REFERENCES courses(id) ON DELETE CASCADE
);

-- Insertion de données dans la table schools
INSERT INTO schools (name) VALUES 
('École Multimédia'),
('ESTIAM'),
('HETIC');

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

-- Insertion de données dans la table courses
INSERT INTO courses (name, date, hours_count) VALUES 
('Web Development', '2024-10-10', 10), 
('Data Science', '2024-10-11', 8),
('Digital Marketing', '2024-10-12', 5), 
('Graphic Design', '2024-10-13', 12);

-- Insertion de données dans la table course_students
INSERT INTO course_students (course_id, student_id) VALUES 
(1, 1), 
(1, 2), 
(2, 3), 
(3, 4), 
(4, 5), 
(1, 6);

-- Insertion de données dans la table course_trainers
INSERT INTO course_trainers (course_id, trainer_id) VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 1),
(3, 4),
(4, 2);

-- Insertion de données dans la table invoices
INSERT INTO invoices (invoice_number, payment_due, invoice_wording, amount_ht, amount_ttc, school_id, course_id) VALUES 
('INV001', '2024-11-01', 'Cours de Web Development', 500.0, 550.0, 1, 1),
('INV002', '2024-11-02', 'Cours de Data Science', 480.0, 537.6, 2, 2),
('INV003', '2024-11-03', 'Cours de Digital Marketing', 350.0, 399.0, 3, 3),
('INV004', '2024-11-04', 'Cours de Graphic Design', 540.0, 594.0, 1, 4);
