import requests

class Search:
   
   def __init__(self,lang,employer_name) -> None:
      self.lang = lang
      self.employer_name = employer_name

   def head_hunter(self):
      """получить вакансии данного языка програмирования , на платформе HeadHunter """

      params = {
         "text": self.employer_name}

      response = requests.get("https://api.hh.ru/employers", params=params)
      employers = response.json()
      employer_id = employers["items"][0]["id"]

      payload = {
         'text': f'Программист {self.lang}',
         'area': 1,
         'only_with_salary': True,
         'period': 30,
         'employer_id': employer_id}
      
      response_vacancies = requests.get(f"https://api.hh.ru/vacancies", params=payload)
      vacancies = response_vacancies.json()
      data_returned = []

      for item in vacancies["items"]:
         json_format = {"name":None, "price":None, "employment":None, "alternate_url":None, "requirement":None, "experience":None}

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
      
         data_returned.append(json_format)

      return data_returned
      
search = Search('Python',"ООО Дубайт")
x = search.head_hunter()
print(x)