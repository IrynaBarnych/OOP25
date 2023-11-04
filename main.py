#Завдання 1
#Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
#дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.


class People:
    def __init__(self, full_name, date_of_birth, contact_phone_number, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.contact_phone_number = contact_phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def full_namee(self):
        return self.full__name

    def date_of_birth(self):
        return self.date__of__birth

    def contact_phone_number(self):
        return self.contact__phone__number

    def city(self):
        return self.__city

    def country(self):
        return self.__country

    def home_address(self):
        return self.home__address


# Створення екземпляра класу
event = People("Шевченко Т.Г.", "2010-03-09", "0661234567", "Київ",
               "Україна", "вул. Листопадна буд. 4")
