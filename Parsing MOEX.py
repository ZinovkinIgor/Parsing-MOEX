import csv
import requests
from bs4 import BeautifulSoup
import lxml
import json


url = 'https://smart-lab.ru/q/shares/'
headers = {
          'accept':  '*/*',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'
         }

res = requests.get(url= url, headers=headers)            # Берем данные с сайта
src = res.text                                           # помещаем их в переменную

with open("MOEX.html", "w", encoding="utf-8") as file:   # Сохранили страницу MOEX.html и работаем с ней
    file.write(src)                                      #

with open("MOEX.html", "r", encoding="utf-8") as file:     # открываем MOEX.html
    src = file.read()                                      # начинаем его читать

soup = BeautifulSoup(src, "lxml")                          # переносим сайт в BeautifulSoup и начинаем работать

result_len = soup.find("table", class_="simple-little-table trades-table").find_all("tr")  # Заходим по адресу и забираем все данные с
score = len(result_len) - 2                                                                # тегом tr,  сохраняем количество полученных данных
print(f"На обработку {score} компаний")                                                    #

name_market = soup.find("table", class_="simple-little-table trades-table").find("tr").find_all("th")   # достаем данные с
for num, item in enumerate(name_market):                                                                #
    print(num, item.text)


#

# Сохраняем шапку для таблицы
number = name_market[0].text                   # номер по порядку
time = 'Время последней сделки'                # Время
name = name_market[2].text                     # Название компании
tiker = name_market[3].text                    # Тикер
price_end = name_market[7].text                # Цена последняя
price_change = name_market[8].text             # Изменение цены в %
value = name_market[9].text                    # Объем мил.рублей
change_price_w = name_market[10].text          # изменение за 1 неделю в %
change_price_m = name_market[11].text          # изменение за 1 месяц в %
change_price_y = name_market[12].text          # изменение с начала года в %
change_price_mon12 = name_market[13].text      # изменение за 12 месяцев в %
capitalization_ru = name_market[14].text       # Капитализация в милрд руб
capitalization_ue = name_market[15].text       # Капитализация в милрд дол
change_value = name_market[16].text            # Изменение Объема



with open("data/moex.csv", "w", encoding="utf-8") as file:
    winter = csv.writer(file)
    winter.writerow(
        (
            number,
            time,
            name,
            tiker,
            price_end,
            price_change,
            value,
            change_price_w,
            change_price_m,
            change_price_y,
            change_price_y,
            capitalization_ru,
            capitalization_ue,
            change_value
            )
        )


list_stock = []


teg = soup.find("table", class_="simple-little-table trades-table")

for n1 in teg.find_all("tr")[2:]:
    new_list = []
    for m2 in n1.find_all("td"):
        new_list.append(m2.text.replace('\t', '').replace('\n', ''))
    list_stock.append(new_list)

with open("data/moex.json", "w", encoding="utf-8") as file:
    json.dump(list_stock, file, indent=4, ensure_ascii=False)

for result_stock in list_stock:

    number_result = result_stock[0]                   # номер по порядку
    time_result = result_stock[1]                     # Время
    name_result = result_stock[2]                    # Название компании
    tiker_result = result_stock[3]                    # Тикер
    price_end_result = result_stock[7]                # Цена последняя
    price_change_result = result_stock[8].replace('\t', '').replace('\n', '')            # Изменение цены в %
    value_result = result_stock[9]                   # Объем мил.рублей
    change_price_w_result = result_stock[10]         # изменение за 1 неделю в %
    change_price_m_result = result_stock[11]         # изменение за 1 месяц в %
    change_price_y_result = result_stock[12]          # изменение с начала года в %
    change_price_mon12_result = result_stock[13]      # изменение за 12 месяцев в %
    capitalization_ru_result = result_stock[14]       # Капитализация в милрд руб
    capitalization_ue_result = result_stock[15]       # Капитализация в милрд дол
    change_value_result = result_stock[16]            # Изменение Объема


    with open("data/moex.csv", "a", encoding="utf-8") as file:
        winter = csv.writer(file)
        winter.writerow(
            (
                number_result,
                time_result,
                name_result,
                tiker_result,
                price_end_result,
                price_change_result,
                value_result,
                change_price_w_result,
                change_price_m_result,
                change_price_y_result,
                change_price_y_result,
                capitalization_ru_result,
                capitalization_ue_result,
                change_value_result
                )
            )

