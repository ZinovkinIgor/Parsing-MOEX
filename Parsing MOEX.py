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

# res = requests.get(url= url, headers=headers)            # Берем данные с сайта
# src = res.text                                           # помещаем их в переменную
#
# with open("MOEX.html", "w", encoding="utf-8") as file:   # Сохранили страницу MOEX.html и работаем с ней
#     file.write(src)                                      #

with open("MOEX.html", "r", encoding="utf-8") as file:     # открываем MOEX.html
    src = file.read()                                      # начинаем его читать

soup = BeautifulSoup(src, "lxml")                          # переносим сайт в BeautifulSoup и начинаем работать

result_len = soup.find("table", class_="simple-little-table trades-table").find_all("tr")  # Заходим по адресу и забираем все данные с
score = len(result_len) - 1                                                                # тегом tr,  сохраняем количество полученных данных
print(f"На обработку {score} компаний")                                                      #

name_market = soup.find("table", class_="simple-little-table trades-table").find("tr").find_all("th")
for num, item in enumerate(name_market):
    print(num, item.text)

#
number = name_market[0].text               # номер по порядку
time = 'Время последней сделки'            # Время
name = name_market[2].text                 # Название компании
tiker = name_market[3].text                # Тикер
price_end = name_market[7].text            # Цена последняя
price_change = name_market[8].text         # Изменение цены в %
value = name_market[9].text                # Объем мил.рублей
change_price_w =name_market[10].text       # изменение за 1 неделю в %
change_price_m = name_market[11].text      # изменение за 1 месяц в %
change_price_y = name_market[12].text      # изменение с начала года в %
change_price_y = name_market[13].text      # изменение за 12 месяцев в %
capitalization_ru = name_market[14].text   # Капитализация в милрд руб
capitalization_ue = name_market[15].text   # Капитализация в милрд дол
change_value = name_market[16].text        # Изменение Объема
change_value_pos = name_market[17].text    # Изменение позиции по объему


with open("moex.csv", "w", encoding="utf-8") as file:
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
            change_value,
            change_value_pos
            )
        )

result_stock = soup.find("table", class_="simple-little-table trades-table").find("tr", class_="down").find_all("td")
for numb, item2 in enumerate(result_stock):
    print(numb, item2.text)
number_result = result_stock[0].text              # номер по порядку
time_result = result_stock[1].text          # Время
name_result = result_stock[2].text                # Название компании
tiker_result = result_stock[3].text               # Тикер
price_end_result = result_stock[7].text           # Цена последняя
price_change_result = result_stock[8].text       # Изменение цены в %
value_result = result_stock[9].text               # Объем мил.рублей
change_price_w_result =result_stock[10].text      # изменение за 1 неделю в %
change_price_m_result = result_stock[11].text     # изменение за 1 месяц в %
change_price_y_result = result_stock[12].text     # изменение с начала года в %
change_price_y_result = result_stock[13].text      # изменение за 12 месяцев в %
capitalization_ru_result = result_stock[14].text   # Капитализация в милрд руб
capitalization_ue_result = result_stock[15].text  # Капитализация в милрд дол
change_value_result = result_stock[16].text       # Изменение Объема
change_value_pos_result = result_stock[17].text   # Изменение позиции по объему

with open("moex.csv", "a", encoding="utf-8") as file:
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
            change_value_result,
            change_value_pos_result
            )
        )

# new_res = soup.find_all(class_="simple-little-table trades-table")
# for i in new_res:
#     print(i.text)



# name_market = soup.find(class_="simple-little-table trades-table").find("tr").find_all("a")
#stock_market = soup.find(class_= "simple-little-table trades-table").find_all("tr").f


#
# with open("moex.scv", "w", encoding="utf-8") as file:
#     writen = csv.writer(file)
#     writen.writerow(
#         (
#             time,
#             name,
#             tiker,
#             price_end,
#             price_change,
#             value,
#             change_price_w,
#             change_price_m,
#             change_price_y,
#             capitalization_ru,
#             capitalization_ue,
#             change_value,
#             change_value_pos,
#         )
#     )
#
# # market = soup.find(class_="down")
# # print(market)
# # stocks #акции
#
# stocks = []
#
# name_market_stocks = soup.find(class_="simple-little-table trades-table").find_all("tr")
# #stock_market = soup.find(class_= "simple-little-table trades-table").find_all("tr").f
#
# #
# for item in name_market_stocks:
#     stocks_data = item.find_all("td")
#
#     for numb, i in enumerate(stocks_data):
#         print("=" * 30)
#         print(numb)
#         print("=" * 30)
#         print(i.text.strip())
    # time = stocks_data[0].text
    # name = stocks_data[1].text
    # tiker = stocks_data[2].text
    # price_end = stocks_data[3].text
    # price_change = stocks_data[4].text
    # value = stocks_data[5].text
    # change_price_w =stocks_data[6].text
    # change_price_m = stocks_data[7].text
    # change_price_y = stocks_data[8].text
    # capitalization_ru = stocks_data[9].text
    # capitalization_ue = stocks_data[10].text
    # change_value = stocks_data[11].text
    # change_value_pos = stocks_data[12].text

    #
    # stocks.append(
    #     {
    #         "time": time,
    #         "name": name,
    #         "tiker": tiker,
    #         "price_end": price_end,
    #         "price_change": price_change,
    #         "value": value,
    #         "change_price_w": change_price_w,
    #         "change_price_m": change_price_m,
    #         "change_price_y": change_price_y,
    #         "capitalization_ru": capitalization_ru,
    #         "capitalization_ue": capitalization_ue,
    #         "change_value": change_value,
    #         "change_value_pos": change_value_pos,
    #     }
    # )
    # with open("moex.scv", "a", encoding="utf-8") as file:
    #     writen = csv.writer(file)
    #     writen.writerow(
    #         (
    #             time,
    #             name,
    #             tiker,
    #             price_end,
    #             price_change,
    #             value,
    #             change_price_w,
    #             change_price_m,
    #             change_price_y,
    #             capitalization_ru,
    #             capitalization_ue,
    #             change_value,
    #             change_value_pos,
    #         )
    #     )
    #
    #
    #
