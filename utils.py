import requests
import psycopg2
class Search:
   
   def __init__(self,employer_name) -> None:
      #self.lang = lang
      self.employer_name = employer_name

   def head_hunter(self):
      """получить вакансии данного языка програмирования , на платформе HeadHunter """

      params = {
         "text": self.employer_name}

      response = requests.get("https://api.hh.ru/employers", params=params)
      employers = response.json()
      employer_id = employers["items"][0]["id"]
      
      payload = {
         #'text': f'Программист {self.lang}',
         'area': 1,
         'only_with_salary': True,
         'period': 30,
         'employer_id': employer_id}
      
      response_vacancies = requests.get(f"https://api.hh.ru/vacancies", params=payload)
      vacancies = response_vacancies.json()
      data_returned = []

      for item in vacancies["items"]:
         json_format = {"name":None, "price":None, "employment":None, "alternate_url":None, "requirement":None, "experience":None, "name_company":None}

         json_format["name"] = item["name"]

         if item["salary"]["from"] == None:
            json_format["price"] = item["salary"]["to"]

         elif item["salary"]["to"] == None:
            json_format["price"] = item["salary"]["from"]

         else:
            json_format["price"] = item["salary"]["from"] + item["salary"]["to"]

         json_format['employment'] = item["employment"]["name"]
         json_format["alternate_url"] = item["alternate_url"]
         json_format["requirement"] = item["snippet"]["requirement"]
         json_format["experience"] = item["experience"]["name"]
         json_format["name_company"] = self.employer_name
      
         data_returned.append(json_format)

      return data_returned
      
class DBManager:
   def __init__(self, name_file, user, password, host, port) -> None:
      self.conn = psycopg2.connect(
      host=host,
      port=port,
      database=name_file,
      user=user,
      password=password
      )
      self.cursor = self.conn.cursor()

   def get_companies_and_vacancies_count(self):
      select_Query = """SELECT  COUNT(name), name_company FROM vacancies
      GROUP BY name_company"""

      self.cursor.execute(select_Query)
      results = self.cursor.fetchall()
      for row in results:
         print(row)
      return ""
   
   def get_all_vacancies(self):
      select_Query = """SELECT name, name_company, price, alternate_url FROM vacancies"""

      self.cursor.execute(select_Query)
      results = self.cursor.fetchall()
      for row in results:
         print(row)
      return ""

   def get_avg_salary(self):
      select_Query = """SELECT avg(price) as avg_price FROM vacancies"""

      self.cursor.execute(select_Query)
      results = self.cursor.fetchall()
      for row in results:
         print(row)
      return ""

   def get_vacancies_with_higher_salary(self):
      select_Query = """SELECT * FROM vacancies 
      WHERE price > (SELECT AVG(price) FROM vacancies)"""

      self.cursor.execute(select_Query)
      results = self.cursor.fetchall()
      for row in results:
         print(row)
      return ""

   def get_vacancies_with_keyword(self):
      select_Query = """SELECT name FROM vacancies 
      WHERE name LIKE '%Python%'"""

      self.cursor.execute(select_Query)
      results = self.cursor.fetchall()
      for row in results:
         print(row)
      return ""
   