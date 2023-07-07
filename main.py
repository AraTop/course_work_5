import psycopg2
from utils import Search

#перед запуском main.py, измените данные на свои. database = название файла где будут все вакансии

host = 'localhost'
port = '5432'  
database = 'db_vacancies'  
user = 'postgres'  
password = 'Komaz5357abv'  

conn = psycopg2.connect(
   host=host,
   port=port,
   database="postgres",
   user=user,
   password=password)

conn.set_session(autocommit=True)
cursor = conn.cursor()
create_database_query = f"CREATE DATABASE {database};"
cursor.execute(create_database_query)

conn.close()
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE vacancies (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255),
   price INTEGER ,
   employment VARCHAR(255),
   alternate_url VARCHAR(255),
   requirement VARCHAR(255),
   experience VARCHAR(255),
   name_company VARCHAR(255)
);
'''
cursor.execute(create_table_query)

insert_data_query = '''
INSERT INTO vacancies (name, price, employment, alternate_url, requirement, experience, name_company)
VALUES (%s, %s, %s, %s, %s, %s, %s);
'''

# Данные для вставки
search1 = Search("АО Рут Код")
search2 = Search("ООО ЭС-АЙ Безопасность")
search3 = Search("КИБЕР-РОМ")
search4 = Search("Университет искусственного интеллекта")
search5 = Search("Модульбанк")
search6 = Search("EFT GROUP")
search7 = Search("Digital Reputation")
search8 = Search("БО-ЭНЕРГО")
search9 = Search("Decart IT-production")
search10 = Search("ООО Дубайт")

data = [search1.head_hunter(), search2.head_hunter(), search3.head_hunter(), search4.head_hunter(), search5.head_hunter(), search6.head_hunter(), search7.head_hunter(), search8.head_hunter(), search9.head_hunter(), search10.head_hunter()]

# Выполнение SQL-запроса для вставки данных в цикле
for items in data:
   for item in items:
      record = (
        item['name'],
        item['price'],
        item['employment'],
        item['alternate_url'],
        item['requirement'],
        item['experience'],
        item["name_company"]
      )
      cursor.execute(insert_data_query, record)

conn.commit()
cursor.close()
conn.close()
