Projeto de Extração e Visualização de Visualizações do YouTube
Descrição
Este projeto extrai o número de visualizações de vídeos de várias playlists do YouTube e gera um gráfico de barras mostrando o total de visualizações por playlist.

Dependências
Certifique-se de ter as seguintes dependências instaladas:

BeautifulSoup
Selenium
Pandas
Matplotlib
Você pode instalá-las usando os comandos abaixo:

bash
Copiar código
pip install beautifulsoup4
pip install selenium
pip install pandas
pip install matplotlib
Como rodar o projeto
Passo 1: Configurar o Selenium
Você precisará do ChromeDriver para rodar o Selenium com o Google Chrome. Baixe o ChromeDriver compatível com a versão do seu Chrome (ou com o navegador que você usa) e coloque-o no seu PATH.

Passo 2: Executar o Script de Extração de Dados
Copie e cole o código abaixo em um arquivo Python, por exemplo, extracao_dados.py, e execute-o.

python
Copiar código
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
Passo 3: Executar o Script de Visualização de Dados
Copie e cole o código abaixo em um arquivo Python, por exemplo, visualizacao_dados.py, e execute-o.

python
Copiar código
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('youtube_views.csv')
df = df.fillna(0)
views_by_playlist = df.sum(axis=0)
views_by_playlist_df = views_by_playlist.to_frame(name='views')
views_by_playlist_df = views_by_playlist_df.sort_values(by='views')

plt.bar(views_by_playlist.index, views_by_playlist_df['views'])
plt.xlabel('Playlist')
plt.ylabel('Número de visualizações')
plt.title('Número de visualizações por playlist')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
Considerações Finais
Validação dos Dados: Você pode adicionar verificações para garantir que os dados foram extraídos corretamente, como verificar se há duplicatas ou entradas vazias.
Otimização: Se a extração dos dados for lenta, considere otimizar a espera dos elementos ou aumentar o tempo de espera no WebDriverWait.

