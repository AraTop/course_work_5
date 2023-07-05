import psycopg2
from utils import Search

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
   experience VARCHAR(255)
);
'''
cursor.execute(create_table_query)

insert_data_query = '''
INSERT INTO vacancies (name, price, employment, alternate_url, requirement, experience)
VALUES (%s, %s, %s, %s, %s, %s);
'''

# Данные для вставки
search1 = Search('Python',"АО Рут Код")
search2 = Search('Python',"ООО ЭС-АЙ Безопасность")
search3 = Search('Python',"КИБЕР-РОМ")
search4 = Search('Python',"Университет искусственного интеллекта")
search5 = Search('Python',"Модульбанк")
search6 = Search('Python',"EFT GROUP")
search7 = Search('Python',"Digital Reputation")
search8 = Search('Python',"БО-ЭНЕРГО")
search9 = Search('Python',"Decart IT-production")
search10 = Search('Python',"ООО Дубайт")

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
        item['experience']
      )
      cursor.execute(insert_data_query, record)

conn.commit()
cursor.close()
conn.close()
