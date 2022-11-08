class Entity:
    def __init__(self, name, birthday, email, password):
        self.__name = name
        self.__birthday = birthday
        self.__email = email
        self.__password = password
         
    def get_name(self):
        return self.__name
    def get_birthday(self):
        return self.__birthday
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password

class Employer(Entity):
    pass

class Client(Entity):
    pass

en1 = Entity("Lucio", "17/02/2001", "lucio.200152@gmail.com", "1234")
print(f"Entity")
print(f"Name:", en1.get_name())
print(f"Birthday:", en1.get_birthday())
print(f"Email:", en1.get_email())
print(f"Password:", en1.get_password())
print(f"")

em1 = Employer("Jeronimo", "26/02/2001", "jeronimo.200152@gmail.com", "0000")
print(f"Employer")
print(f"Name:", em1.get_name())
print(f"Birthday:", em1.get_birthday())
print(f"Email:", em1.get_email())
print(f"Password:", em1.get_password())
print(f"")

c1 = Client("Joaquin", "11/01/2001", "joaquin.200152@gmail.com", "1230")
print(f"Client")
print(f"Name:", c1.get_name())
print(f"Birthday:", c1.get_birthday())
print(f"Email:", c1.get_email())
print(f"Password:", c1.get_password())
