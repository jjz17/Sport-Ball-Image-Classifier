import os
import time
import urllib.request as urllib
import random

import pandas as pd


def url_to_jpg(index, url, file_path):
    file_name = f'image{index}.jpg'
    full_path = f'{file_path}{file_name}'
    urllib.urlretrieve(url, full_path)

    # print(f'{file_name} saved successfully')


# main_dir = ["FolderA", "FolderB"]
# common_dir = ["SubFolder1", "SubFolder2", "SubFolder3"]

# Creating Directories

# main_dir = 'sport_ball_images'
# sub_dirs = ['basketball', 'soccer']
#
# for sub_dir in sub_dirs:
#     try:
#         os.makedirs(os.path.join(main_dir, sub_dir))
#     except OSError:
#         pass

df = pd.read_csv('image_urls.csv')

# print(df.head())

for i in df.index:
    row = df.loc[i]
    label = row['Type']
    url = row['Image_URL']
    print(url)
    file_path = ''
    if label == 'Basketball':
        file_path = f'sport_ball_images{os.path.sep}basketball{os.path.sep}'
    else:
        file_path = f'sport_ball_images{os.path.sep}soccer{os.path.sep}'
    try:
        url_to_jpg(i+1, url, file_path)
        print(f'Saving image {i+1}')
        time.sleep(random.randint(2, 5))
    except:
        pass
    # print(f'{label} {url}')

# url_to_jpg(1, 'https://www.victeamsports.com/wp-content/uploads/2019/01/Customize-Your-Own-Soccer-Footballs-500x500.jpg', 'sport_ball_images/soccer/')
