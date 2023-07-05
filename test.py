import requests
from utils import Search
employer_name = "python"

# Параметры запроса
params = {
   "text": employer_name
}

response = requests.get("https://api.hh.ru/employers", params=params)
employers = response.json()
employer_id = employers["items"][0]["id"]
#print(employers)
payload = {
   'text': f'python',
   'area': 1,
   'only_with_salary': True,
   'period': 30,
   'employer_id': employer_id

}
response_vacancies = requests.get(f"https://api.hh.ru/vacancies", params=payload)

vacancies = response_vacancies.json()
#for vacancy in vacancies["items"]:
   #print(vacancy)

search1 = Search('python',"АО Рут Код")
search2 = Search('Python',"ООО ЭС-АЙ Безопасность")
search3 = Search('Python',"КИБЕР-РОМ")
search4 = Search('Python',"Университет искусственного интеллекта")
search5 = Search('Python',"Модульбанк")
search6 = Search('Python',"EFT GROUP")
search7 = Search('Python',"Digital Reputation")
search8 = Search('Python',"БО-ЭНЕРГО")
search9 = Search('Python',"Decart IT-production")
search10 = Search('Python',"ООО Дубайт")

#data = [search1.head_hunter(), search2.head_hunter(), search3.head_hunter(), search4.head_hunter(), search5.head_hunter(), search6.head_hunter(), search7.head_hunter(), search8.head_hunter(), search9.head_hunter(), search10.head_hunter()]

#for items in data:
   #for item in items:
x = search1.head_hunter()
print(x)