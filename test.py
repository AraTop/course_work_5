import requests
employer_name = "АО Рут Код"

# Параметры запроса
params = {
   "text": employer_name
}

response = requests.get("https://api.hh.ru/employers", params=params)
employers = response.json()
employer_id = employers["items"][0]["id"]

payload = {
   'text': f'Программист {self.lang}',
   'area': 1,
   'only_with_salary': True,
   'period': 30,
   'employer_id': employer_id

}
response_vacancies = requests.get(f"https://api.hh.ru/vacancies", params=payload)

vacancies = response_vacancies.json()
for vacancy in vacancies["items"]:
   print(vacancy)