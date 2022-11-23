CREATE TABLE school (school_id INTEGER PRIMARY KEY, name TEXT NOT NULL, address TEXT NOT NULL, phone_n NUMERIC NOT NULL, email TEXT NOT NULL)
CREATE TABLE teachers (teachers_id TEXT PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, birth_day TEXT NOT NULL, subject TEXT NOT NULL, phone_n NUMERIC, email TEXT)	
CREATE TABLE students (students_id TEXT PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, birth_day TEXT NOT NULL, grade TEXT NOT NULL, phone_n NUMERIC, email TEXT)
CREATE TABLE subjects (subjects_id INTEGER PRIMARY KEY AUTOINCREMENT, subject_name TEXT NOT NULL)
CREATE TABLE notes (notes_id INTEGER PRIMARY KEY AUTOINCREMENT, student TEXT NOT NULL, subject TEXT NOT NULL, exam_note NUMERIC, exam_date TEXT NOT NULL,
					FOREIGN KEY(student) REFERENCES students(students_id), FOREIGN KEY(subject) REFERENCES subjects(subjects_id))
					
INSERT INTO school (name, address, phone_n, email) VALUES ("Barba's Programming School", "Av. Garcha 123", 3400643092, "barbasproschool@gmail.com")
INSERT INTO teachers (teachers_id, first_name, last_name, birth_day, subject, phone_n, email) VALUES (43284118, "Lucio", "Santa Maria", "17/02/2001", "Maths", 3400664896, "latripa2001@gmail.com")
INSERT INTO students VALUES (67324983,"Jorge", "Diaz", "02/03/2026", "1°", 3400667893, "jorgito@gmail.com")
INSERT INTO students (students_id, first_name, last_name, birth_day, grade, phone_n, email) VALUES (72987824, "Marta", "Bodrero", "12/07/2029", "1°", 3400666374, "marturocha@gmail.com")
INSERT INTO subjects (subject_name) VALUES ("HTML"),("CSS"),("JS")
INSERT INTO notes VALUES (NULL, '72987824', '1', 7, "15/02/2040"),(NULL, '72987824', '2', 9, "09/02/2040"),(NULL, '72987824', '3', 7, "19/02/2040")
INSERT INTO notes VALUES (NULL, '69923834', '1', 8, "15/02/2040"),(NULL, '69923834', '2', 8, "09/02/2040"),(NULL, '69923834', '3', 7, "19/02/2040")

SELECT students.first_name,students.last_name,students.grade,subjects.subject_name,notes.exam_note,notes.exam_date FROM students,subjects,notes WHERE notes.student=students.students_id AND notes.subject=subjects.subjects_id
SELECT students.first_name,students.last_name,students.grade,subjects.subject_name,notes.exam_note,notes.exam_date FROM students,subjects,notes WHERE notes.student=students.students_id AND notes.subject=subjects.subjects_id AND first_name='Marta'
SELECT * FROM students WHERE grade='1°'

UPDATE teachers SET email='gustavoghioldifrontend@gmail.com' WHERE teacher_id=1
UPDATE students SET birth_day='02/03/2026' WHERE students_id=69923834

DELETE FROM subjects WHERE
DELETE FROM notes WHERE