# -*- coding: utf-8 -*-

"""Скраппер для сайта ComputerUnivers для заполнения базы исходными данными

Скраппер парсит страницы сайта https://www.computeruniverse.ru/ на предмет данных и записывает их в базу
проекта Django.
"""

import sys, os, django
sys.path.append("\\".join(sys.path[0].split("\\")[:-1:]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comparison.settings")
django.setup()
# import logging
# logging.basicConfig(level=logging.DEBUG)
import time

from requests_html import HTMLSession
session = HTMLSession()
from vergleich.models import ScrapperBenchRam, ScrapperBenchCPU, ScrapperBenchHDD, ScrapperBenchVideo


def get_urls(url):
    r = session.get(url)
    # Вытягиваем ссылки
    lst = r.html.find(".listProductTitle")
    n = 0
    for i in lst:
        n += 1
        # Запись данный в базу
        new_obj = ScrapperCURamUrls(url = list(i.find("a")[0].absolute_links)[0], name = i.find("a")[0].attrs["title"])
        new_obj.save()
        print("Обработано ссылок {0} из {1}".format(n, len(lst)))


def get_all_rams_url():
    print("Start!")
    first_url = 'https://www.computeruniverse.ru/en/groups/30001005/memory.asp'
    print("Первая страница пошла на обработку")
    get_urls(first_url)
    r = session.get(first_url)   # Ещё раз забираем первую страницу для выяснения количества страниц
    pag = r.html.find("#pageLast")[0]  # Забираем номер последней страницы пагинации
    for page in range(2, int(pag.attrs["value"]), 1):  # Для всех старниц
        url =  "{0}{1}{2}".format("https://www.computeruniverse.ru/en/groups/p", page, '/30001005/memory.asp')  # Создаём ссылку страницы
        print("Страница номер {0} на обработке".format(page))
        get_urls(url)  # Отправляем страницу на обработку
        time.sleep(3)  # Выжидаем время
    print("Done!")


def get_ram_info(url, name):  # Забираем информацию со страницы
    req = session.get(url)
    req.html.render()
    # Достаём со старницы SKU
    res = req.html.find(".p_ilh")[0]
    sku = res.text.split(",")[1][6::]
    # Достаём со страницы тип DDR
    ddr_type = req.html.find(".propsInfo > li > span")[2].text[:4:]
    # Достаём цены в евро
    coast_e = req.html.find(".cartAreaPrice")[0].text.replace(" ", "")
    # Достаём цены в рублях
    # coast_r = req.html.find(".oldpricebolditalic")[0].text.replace(" ", "")[:-5:]
    # Смотрим наличие
    res = req.html.find(".statushelp_layer > strong")[0].text
    in_stock = True if "in stock" in res else False
    new_obj = ScrapperCURamInfo(
        name = name,
        url = url,
        ddr_type = ddr_type,
        sku = sku,
        coast_e = coast_e,
        # coast_r = coast_r,
        in_stock = in_stock
    )
    new_obj.save()


# Парсим базу бенчмарк-таблицы
def get_ram_bench_save_to_base(obj):
    res_td = obj.find("td")  # Находим внутренние элементы td
    name = res_td[0].text
    url = list(res_td[0].absolute_links)[0]
    latency = int(res_td[1].text)
    speed_read = int(res_td[2].text)
    speed_write = int(res_td[3].text)
    in_stock = True if "NA" not in res_td[4].text else False
    if "NA" not in res_td[4].text:
        price = float(res_td[4].text[1::].replace(",", "").replace("*", ""))
    else:
        price = -1
    # print("{0:<70}{1:<5}{2:<7}{3:<7}{4:<7}{5:<7}".format(name, latency, speed_read, speed_write, in_stock, price))  # Для отладки
    new_obj = ScrapperBenchRam(
            name = name,
            url = url,
            speed_read = speed_read,
            speed_write = speed_write,
            latency = latency,
            in_stock = in_stock,
            price = price,
    )
    new_obj.save()


def get_ram_bench():  # Собираем данные с таблицы результатов тестов
    req = session.get("http://127.0.0.1:8001/ram_table.html")
    req.html.render()
    res_even = req.html.find(".even")  # Находим все строки с CSS классом .even
    res_odd = req.html.find(".odd")  # Находим все строки с CSS классом .odd
    res_all = res_even + res_odd  # Складываем оба списка для одновременной обработки
    len_in_all = len(res_even) + len(res_odd)
    count = 0
    for td in res_all:  # Для всех элементов
        count += 1
        get_ram_bench_save_to_base(td)  # Отправляем найденный элемент на обработку
        print("Обработано {0} записей из {1}".format(count, len_in_all))


# Ищем совпадения
from difflib import get_close_matches as gcm
from difflib import SequenceMatcher as SM
def get_matches(word):
    search_list = []  # Создаю будущий списко сравнения
    word = word.upper()  # Перевожу переданное словов в верхний регистр
    for i in ScrapperBenchRam.objects.all():
        search_list.append(i.name.upper().split(" "))  # Собираю список, с которым буду сверять и список в верхний регистр, и разделяю на подсписки
    for i in search_list:
        res = gcm(word, i, n=1, cutoff=0.9)  # Проиводится сверка со всей стройкой
        if len(res)>0:
            print(res)


# Get data from bench table
def get_bench_table(url, save_to_base = 0, base_name = object):
    req = session.get(url)
    req.html.render()
    res = req.html.find("#mark")[0].find("tr")[1:-1]
    res_len = len(res)
    count = 0
    for i in res:
        count += 1
        td = i.find("td")
        name = td[0].text
        url = list(td[0].absolute_links)[0]
        score = float(td[1].text.replace(",", "."))
        rank = int(td[1].find("span")[0].attrs["onmouseover"].split(",")[1])
        in_stock = True if "NA" not in td[2].text else False
        if "NA" not in td[2].text:
            price = float(td[2].text[1::].replace(",", "").replace("*", ""))
        else:
            price = -1
        if save_to_base == 1:
            new_obj = base_name(
                name = name,
                url = url,
                score = score,
                rank = rank,
                in_stock = in_stock,
                price = price,
            )
            new_obj.save()
            print("Обрботано {0} записей из {1}".format(count, res_len))
        else:
            print("{0:<70}{1:<7}{2:<5}{3:<7}{4:<10}".format(name, score, rank, in_stock, price))

if __name__ == '__main__':
    get_ram_bench()    
