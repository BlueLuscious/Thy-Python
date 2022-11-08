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

class Employer:
    def __init__(self, salary):
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
                
class Client:
    def __init__(self, t_sales):
        self.__t_sales = t_sales
    
    def get_t_sales(self):
        return self.__t_sales
        
class AdminEmployer:
    def __init__(self, done_deal):
        self.__done_deal = done_deal
    
    def get_done_deal(self):
        return self.__done_deal
        
class SellerEmployer:
    def __init__(self, min_sells, max_sells):
        self.__min_sells = min_sells
        self.__max_sells = max_sells
        
    def get_min_sells(self):
        return self.__min_sells
    def get_max_sells(self):
        return self.__max_sells
    
en1 = Entity("Lucio", "17/02/2001", "lucio.200152@gmail.com", "1234")
print(f"Entity")
print(f"Name:", en1.get_name())
print(f"Birthday:", en1.get_birthday())
print(f"Email:", en1.get_email())
print(f"Password:", en1.get_password())
print(f"")

em1 = Employer("$100.000")
print(f"Employer")
print(f"Salary:", em1.get_salary())
print(f"")

c1 = Client("20")
print(f"Client")
print(f"Total Sales:", c1.get_t_sales())
print(f"")

ad1 = AdminEmployer("7")
print(f"Administrative Employer")
print(f"Deals Done:", ad1.get_done_deal())
print(f"")

se1 = SellerEmployer("3", "15")
print(f"Sells")
print(f"Minimum Sales:", se1.get_min_sells())
print(f"Maximum Sales:", se1.get_max_sells())
