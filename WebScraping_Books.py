import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#  Creating df with all books
#  Getting Books Titles
def get_titles(sp):
    titles = sp.find_all('article', class_='product_pod')
    titles_list = [title.div.img.get('alt') for title in titles]
    return titles_list


#  Getting Books Ratings
def get_ratings(sp):
    ratings = sp.find_all('article', class_='product_pod')
    ratings_list = [rating.p.get('class')[1] for rating in ratings]
    word_to_num = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    ratings_list = [word_to_num[val] for val in ratings_list]
    return ratings_list


#  Getting Books Prices
def get_prices(sp):
    prices = sp.find_all('p', class_='price_color')
    price_list = [price.get_text().strip() for price in prices]
    return price_list


#  Getting Books Links
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
#  Iterating over all pages
while i <= 50:
    i += 1
    response = requests.get(base_url + 'page-' + str(i) + '.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    titles_final_list += get_titles(soup)
    ratings_final_list += get_ratings(soup)
    prices_final_list += get_prices(soup)
    links_final_list += get_links(soup)

books_dict = {'Title': titles_final_list, 'Rating': ratings_final_list, 'Prices': prices_final_list, 'Links': links_final_list}

books_df = pd.DataFrame(books_dict)

#  Getting the Category for each book
#  Getting all Categories
response = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')
nav_list = soup.find_all('li', class_=False)
categories_list = [category.get_text().strip().lower() for category in nav_list[2:]]

cat_dict = {}
for i in range(len(categories_list)):
    cat_url_st = 'http://books.toscrape.com/catalogue/category/books/' + str(categories_list[i].replace(' ', '-')) + '_' + str(i+2)
    cat_url = cat_url_st + '/index.html'
    response = requests.get(cat_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    book_nb = int(soup.find('form', class_='form-horizontal').get_text().strip().split(' ')[0])
    titles = soup.find_all('article', class_='product_pod')
    titles_list = [title.div.img.get('alt') for title in titles]
    book_nb -= 20
    j = 1
    while book_nb > 0:
        book_nb -= 20
        j += 1
        page_cat_url = cat_url_st + '/page-' + str(j) + '.html'
        response = requests.get(page_cat_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('article', class_='product_pod')
        titles_list += [title.div.img.get('alt') for title in titles]
    aux_dict = {str(categories_list[i]): titles_list}
    cat_dict = {**cat_dict, **aux_dict}

books_df['Category'] = ''
books_df = books_df.set_index('Title')

for key, value in cat_dict.items():
    for book in value:
        books_df.at[book, 'Category'] = key

# EDA

analysis_dict = {'variables': list(books_df.columns.values),
                 'count': list(books_df.count().values),
                 'v_types': list(books_df.dtypes.values),
                 'n_null': list(books_df.isnull().sum().values),
                 'n_uniques': list(books_df.nunique().values)}

analysis = pd.DataFrame(analysis_dict)
print(books_df.head())
print(books_df.shape)
print(analysis)
