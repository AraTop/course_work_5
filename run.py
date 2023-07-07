from utils import DBManager

dbmanager = DBManager('db_vacancies', 'postgres', 'Komaz5357abv', 'localhost', 5432)
print(dbmanager.get_companies_and_vacancies_count())
print(dbmanager.get_all_vacancies())
print(dbmanager.get_avg_salary())
print(dbmanager.get_vacancies_with_higher_salary())
print(dbmanager.get_vacancies_with_keyword())