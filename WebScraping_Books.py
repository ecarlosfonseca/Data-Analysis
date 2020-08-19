import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def get_titles(sp):
    titles = sp.find_all('article', class_='product_pod')
    titles_list = [title.div.img.get('alt') for title in titles]
    return titles_list


def get_ratings(sp):
    ratings = sp.find_all('article', class_='product_pod')
    ratings_list = [rating.p.get('class')[1] for rating in ratings]
    word_to_num = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    ratings_list = [word_to_num[val] for val in ratings_list]
    return ratings_list


def get_prices(sp):
    prices = sp.find_all('p', class_='price_color')
    price_list = [price.get_text().strip() for price in prices]
    return price_list


def get_links(sp):
    links = sp.find_all('article', class_='product_pod')
    link_list = [base_url + link.div.a.get('href') for link in links]
    return link_list


base_url = 'http://books.toscrape.com/catalogue/'
i = 1
response = requests.get(base_url + 'page-' + str(i) + '.html')
soup = BeautifulSoup(response.content, 'html.parser')
titles_final_list = get_titles(soup)
ratings_final_list = get_ratings(soup)
prices_final_list = get_prices(soup)
links_final_list = get_links(soup)
while i <= 50:
    i += 1
    response = requests.get(base_url + 'page-' + str(i) + '.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    titles_final_list += get_titles(soup)
    ratings_final_list += get_ratings(soup)
    prices_final_list += get_prices(soup)
    links_final_list += get_links(soup)

books_dict = {'Tile': titles_final_list, 'Rating': ratings_final_list, 'Prices': prices_final_list, 'Links': links_final_list}

books_df = pd.DataFrame(books_dict)
print(books_df.head())
print(books_df.shape)

# EDA

analysis_dict = {'variables': list(books_df.columns.values),
                 'count': list(books_df.count().values),
                 'v_types': list(books_df.dtypes.values),
                 'n_null': list(books_df.isnull().sum().values),
                 'n_uniques': list(books_df.nunique().values)}

analysis = pd.DataFrame(analysis_dict)
print(analysis)
