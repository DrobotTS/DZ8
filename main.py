# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список оветов сервиса http://forismatic.com/ru/api/.
# Если автор не указан, цитату не брать. Цитаты не должны повторяться.

import requests, random, csv

def get_raw_quote(numb_quotes):
    quotes = []
    for _ in range(int(numb_quotes)):
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": random.randint(1, 1000),
                  "lang": "ru"}
        resp = requests.get(url, params=params)
        quote = resp.json()
        if quote["quoteAuthor"] != '':
            default_quote = dict(Author=quote["quoteAuthor"], Quote=quote["quoteText"], URL=quote["quoteLink"])
            quotes.append(default_quote)
    return quotes



# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

def csv_writer(my_quotes):
    with open("quotes.csv", 'w', encoding='utf-8') as file:
        header = ["Author", "Quote", "URL"]
        writer = csv.DictWriter(file, delimiter=",", fieldnames=header)
        writer.writeheader()
        writer.writerows(sorted(my_quotes, key=lambda x: x.get("Author")))


res_quotes = get_raw_quote(input("Enter your number: "))
print(res_quotes)
csv_writer(res_quotes)

