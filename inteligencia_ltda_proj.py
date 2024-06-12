import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('window-size=400,800') 
browser = webdriver.Chrome(options=options)

playlist_urls = [
    ('https://www.youtube.com/playlist?list=PLJznpI7w9Tor2LuPPHczHLOYuxBvMIufA', 'MÚSICA'),
    ('https://youtube.com/playlist?list=PLJznpI7w9TormzjSNPcrLI91P4LyDig65', 'FÉ E ESPIRITUALIDADE'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9TopkFkFw-9MXmFl7LGeFGbmb', 'ECONOMIA E INVESTIMENTO'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9TopwTYPsDU_kavs5yQXmU31C', 'JORNALISMO'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9Toq_DDt3aEVWKkZNbfgKk6V1', 'TV E ENTRETENIMENTO'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9TopUNKbaX2fhQj3M40OuU-8g', 'DEBATES'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9TorbcXanv4-fK5ZHVd3gcU1X', 'TRUE CRIME: CRIMES REAIS'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9Too3lLbxllv0KReqx_9-YniN', 'POLÍTICA E GEOPOLÍTICA'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9Toqyv_DWEFZnS7rU1ETaERbD', 'HUMOR'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9Top4w9gZk5KNJeL6P2itXAyJ', 'CIÊNCIA E TECNOLOGIA'),
    ('https://www.youtube.com/playlist?list=PLJznpI7w9Toq-Gl4Pdz7kIsneuxZCw90X', 'A MENTE HUMANA'),
]

all_data = {column_name: [] for _, column_name in playlist_urls}

for playlist_url, column_name in playlist_urls:
    browser.get(playlist_url)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'video-title'))
        )

        all_site = BeautifulSoup(browser.page_source, 'html.parser')
        views_elements = all_site.find_all('yt-formatted-string', id='video-info')

        playlist_data = []
        for view in views_elements:
            views_text = view.text.split(' ')[0]
            views_number = re.sub('[^0-9]', '', views_text)
            playlist_data.append(views_number)

        all_data[column_name] = playlist_data

    except Exception as e:
        print(f"Erro ao acessar a playlist {playlist_url}: {e}")

browser.quit()

max_length = max(len(data) for data in all_data.values())
for column_name in all_data:
    all_data[column_name].extend([''] * (max_length - len(all_data[column_name])))

df = pd.DataFrame(all_data)

df.to_csv('youtube_views.csv', index=False)
