import sqlite3

class Subjects:
    def __init__(self):
        self.conn = sqlite3.connect("C:/Users/Lucio/Documents/HTML/Barba's Programming School/BPS.db")

    def __str__(self):
        data = self.get_subjects()
        aux = ""
        for row in data:
            aux=aux + str(row) + "\n"
        return aux

    def get_subjects(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM subjects")
        data = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return data

    def insert_subjects(self, subject_name):
        cursor = self.conn.cursor()
        sql = f'''INSERT INTO subjects (subject_name) VALUES ('{subject_name}')'''
        cursor.execute(sql)
        r=cursor.rowcount
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return r

    def delete_subjects(self, subjects_id):
        cursor = self.conn.cursor()
        sql = f'''DELETE FROM subjects WHERE subjects_id = {subjects_id}'''
        cursor.execute(sql)
        r=cursor.rowcount
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return r

    def update_subjects(self, subject_name, subjects_id):
        cursor = self.conn.cursor()
        sql = f'''UPDATE subjects SET subject_name='{subject_name}' WHERE subjects_id = {subjects_id}'''
        cursor.execute(sql)
        r=cursor.rowcount
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return r