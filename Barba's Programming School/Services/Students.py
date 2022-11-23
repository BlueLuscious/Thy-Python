import sqlite3

class Students:
    def __init__(self):
        self.conn = sqlite3.connect("C:/Users/Lucio/Documents/HTML/Barba's Programming School/BPS.db")

    def __str__(self):
        data = self.get_students()
        aux = ""
        for row in data:
            aux=aux + str(row) + "\n"
        return aux

    def get_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data
    
    ##def get_student(self, students_id):
        cursor = self.conn.cursor()
        sql = f"SELECT * FROM students WHERE students_id = {students_id}"
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        self.conn.close()
        return data

    def insert_students(self, students_id, first_name, last_name, birth_day, grade, phone_n, email):
        cursor = self.conn.cursor()
        sql = f'''INSERT INTO students VALUES ('{students_id}', '{first_name}', '{last_name}', '{birth_day}', '{grade}', '{phone_n}', '{email}')'''
        cursor.execute(sql)
        r=cursor.rowcount
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return r

    def delete_students(self, students_id):
        cursor = self.conn.cursor()
        sql = f'''DELETE FROM students WHERE students_id = {students_id}'''
        cursor.execute(sql)
        r=cursor.rowcount
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return r

    def update_students(self, first_name, last_name, birth_day, grade, phone_n, email, students_id):
        cursor = self.conn.cursor()
        sql = f'''UPDATE students SET first_name='{first_name}', last_name='{last_name}', birth_day='{birth_day}', grade='{grade}', phone_n='{phone_n}', email='{email}' WHERE students_id = {students_id}'''
        cursor.execute(sql)
        r=cursor.rowcount
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return r
