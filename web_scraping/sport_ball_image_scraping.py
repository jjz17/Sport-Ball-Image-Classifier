# %%

# IMPORTS

import urllib.request as urllib

import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup

sns.set_style('darkgrid')
sns.set_palette(sns.diverging_palette(220, 20, n=7))
import time
import random

# %%

import os


def Test():
    main_dir = ["FolderA", "FolderB"]
    common_dir = ["SubFolder1", "SubFolder2", "SubFolder3"]

    for dir1 in main_dir:
        for dir2 in common_dir:
            try:
                os.makedirs(os.path.join(dir1, dir2))
            except OSError:
                pass


# %%

# os.makedirs('New Folder')
# os.makedirs(os.path.join('New Folder', 'Newer Folder'))

# %%

def get_soup(url):
    # Open the target category page
    html = urllib.urlopen(url)

    # Create a BeautifulSoup object after the HTML page is read
    soup = BeautifulSoup(html.read())

    # Close the urllib connection to avoid issues with the website
    html.close()

    return soup


# %%

# Create the DataFrame and populate it with Data


'''
https://www.spalding.com/basketball/basketballs/?srule=product-name-ascending&start=0&sz=36
https://www.wilson.com/en-us/basketball/basketballs/shopby/size_7_off   + ?p=1 (2 or 3)
https://www.victeamsports.com/product-categories/basketballs/?product-page=1 (2 or 3)


https://www.victeamsports.com/product-categories/soccer-balls/?product-page=1 (goes thru 6)

'''

target_url = 'https://www.spalding.com/basketball/basketballs/?srule=product-name-ascending&start=0&sz=36'
df = pd.DataFrame(columns=['Brand', 'Type', 'Image_URL'])

soup = get_soup(target_url)

# SPALDING SCRAPING

products = soup.find_all('a', class_='image-anchor d-none d-sm-block')

url_count = 0

for count, product in enumerate(products):
    #     if product.has_attr('href'):
    #         print(product['href'])
    img_urls = product.find_all('img')

    for img_url in img_urls:
        if img_url.has_attr('src'):
            url = img_url['src']
            temp_dict = {'Brand': 'Spalding', 'Type': 'Basketball', 'Image_URL': url}
            df = df.append(temp_dict, ignore_index=True)
            #             print(url)
            url_count += 1

# print(url_count)
# df

target_url = 'https://www.victeamsports.com/product-categories/basketballs/?product-page='
for i in range(1, 4):
    t_url = f'{target_url}{i}'
    soup = get_soup(t_url)
    products = soup.find_all('div', class_='fusion-image-wrapper fusion-image-size-fixed')

    for count, product in enumerate(products):
        #     if product.has_attr('href'):
        #         print(product['href'])
        img_url = product.find('img')

        if img_url.has_attr('src'):
            url = img_url['src']
            temp_dict = {'Brand': 'Victeam', 'Type': 'Basketball', 'Image_URL': url}
            df = df.append(temp_dict, ignore_index=True)
            #             print(url)
            url_count += 1
    time.sleep(random.randint(2, 5))
print(url_count)
df

# %%

target_url = 'https://www.victeamsports.com/product-categories/soccer-balls/?product-page='
for i in range(1, 7):
    t_url = f'{target_url}{i}'
    soup = get_soup(t_url)
    products = soup.find_all('div', class_='fusion-image-wrapper fusion-image-size-fixed')

    for count, product in enumerate(products):
        #     if product.has_attr('href'):
        #         print(product['href'])
        img_url = product.find('img')

        if img_url.has_attr('src'):
            url = img_url['src']
            temp_dict = {'Brand': 'Victeam', 'Type': 'Soccer', 'Image_URL': url}
            df = df.append(temp_dict, ignore_index=True)
    time.sleep(random.randint(2, 5))

# %%

df['Image_URL'][100]

# %%

df

# %%

info = df.groupby('Brand').describe()

# %%
df.to_csv('image_urls.csv', index=False)
