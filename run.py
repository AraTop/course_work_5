import configparser
from utils import DBManager

config = configparser.ConfigParser()
config.read('config.ini')

host = config.get('postgresql', 'host')
database = config.get('postgresql', 'database')
user = config.get('postgresql', 'user')
password = config.get('postgresql', 'password')
port = config.get('postgresql', 'port')

dbmanager = DBManager(database, user, password, host, port)
while True:
   print("Здравтсвуйте, на какие данные вы бы хотели посмотреть?\nВиберите: нужную вам цыфру \n1 - Получает список всех компаний и количество вакансий у каждой компании.\n2 - Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n3 - Получает среднюю зарплату по вакансиям.\n4 - Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n5 - Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.\n6 - Eсли хочешь надоело :)")
   user_input = input()
   print("\n")
   if user_input == "1":
      print(dbmanager.get_companies_and_vacancies_count())
   elif user_input == "2":
      print(dbmanager.get_all_vacancies())
   elif user_input == "3":
      print(dbmanager.get_avg_salary())
   elif user_input == "4":
      print(dbmanager.get_vacancies_with_higher_salary())
   elif user_input == "5":
      print(dbmanager.get_vacancies_with_keyword())
   elif user_input == "6":
      dbmanager.closed_sql()
      break