# # 1. Проверка доступности веб-страницы
#
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
#
# def check_website(url):
#     try:
#         response = urlopen(url)
#         print(f"Страница {url} найдена. Код ответа: {response.status}")
#     except HTTPError as e:
#         print(f"Ошибка HTTP: {e.code} - {e.reason}")
#     except URLError as e:
#         print(f"Ошибка URL: {e.reason}")
#
# # Пример использования
# check_website("https://www.python.org")
#
#
#
#
#
# # 2. Проверка SSL сертификата
#
# import requests
#
# def check_ssl(url):
#     try:
#         response = requests.get(url)
#         if response.ok:
#             print(f"У сайта {url} есть SSL сертификат.")
#         else:
#             print(f"SSL сертификат не найден или сайт недоступен.")
#     except requests.exceptions.SSLError:
#         print(f"Ошибка SSL для сайта {url}.")
#
# # Пример использования
# check_ssl("https://www.python.org")
#
#
#
#
#
#
#
# # 3. Вывод информации о сайте
#
# import requests
#
# def get_site_info(url):
#     response = requests.get(url)
#     print("Status Code:", response.status_code)
#     print("Headers:", response.headers)
#     print("URL:", response.url)
#     print("History:", response.history)
#     print("Encoding:", response.encoding)
#     print("Reason:", response.reason)
#     print("Cookies:", response.cookies)
#     print("Elapsed:", response.elapsed)
#     print("Request:", response.request)
#     print("Content:", response.text[:500])  # Вывод первых 500 символов контента
#
# # Пример использования
# get_site_info("https://www.python.org")
#
#
#
#
# # 4. Выгрузка файла robots.txt
#
# import requests
#
# def get_robots_txt(url):
#     response = requests.get(url + "/robots.txt")
#     print(response.text)
#
# # Пример использования
# get_robots_txt("https://en.wikipedia.org")
#
#
#
#
# # 5. Извлечение заголовка <h1>
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# def get_h1(url):
#     html = urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     h1 = soup.find('h1')
#     print(h1.text if h1 else "Заголовок <h1> не найден.")
#
# # Пример использования
# get_h1("http://www.example.com")
#
#
#
#
#
# # 6.Извлечение всех заголовков <header>
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# def get_headers(url):
#     html = urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
#     for header in headers:
#         print(header.text)
#
# # Пример использования
# get_headers("https://en.wikipedia.org/wiki/Main_Page")
#
#
#
# # 7. Извлечение всех ссылок
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# def get_links(url):
#     html = urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup.find_all('a', href=True)
#     for link in links:
#         print(link['href'])
#
# # Пример использования
# get_links("https://en.wikipedia.org/wiki/Python")
#
#
#
#
# # 8. Выгрузка CSV и подсчет строк
#
# import requests
# import pandas as pd
#
# def count_csv_rows(url):
#     response = requests.get(url)
#     with open("earthquakes.csv", "wb") as file:
#         file.write(response.content)
#     df = pd.read_csv("earthquakes.csv")
#     print(f"Количество строк в CSV: {len(df)}")
#
# # Пример использования
# count_csv_rows("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv")
#
#
#
#
# # 9. Скрейпинг IMDb
#
# import requests
# from bs4 import BeautifulSoup
# import random
#
# def scrape_imdb():
#     url = "https://www.imdb.com/chart/top"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Новые селекторы для фильмов и их описаний
#     movies = soup.select('h3.ipc-title__text')  # Названия фильмов
#     descriptions = soup.select('span.cli-title-metadata-item')  # Год выпуска
#
#     # Собираем список фильмов и их описаний
#     movie_list = []
#     for i in range(0, len(movies)):
#         title = movies[i].text.strip()  # Название фильма
#         year = descriptions[i].text.strip() if i < len(descriptions) else "N/A"  # Год выпуска
#         movie_list.append((title, year))
#
#     # Проверяем, достаточно ли фильмов для выборки
#     if len(movie_list) < 10:
#         print(f"Найдено фильмов: {len(movie_list)}. Вывод всех доступных фильмов:")
#         random_movies = movie_list
#     else:
#         random_movies = random.sample(movie_list, 10)
#
#     # Выводим фильмы
#     for movie, year in random_movies:
#         print("-" * 45)
#         print(f"{movie} ({year})")
#
# # Пример использования
# scrape_imdb()
#
#
# # 10. SOAP запрос с использованием zeep
#
# import zeep
#
# def get_country_phone_code(country_code):
#     wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
#     client = zeep.Client(wsdl=wsdl_url)
#     result = client.service.CountryIntPhoneCode(sCountryISOCode=country_code)
#     print(f"Телефонный код для страны {country_code}: {result}")
#
# # Пример использования
# get_country_phone_code("RU")