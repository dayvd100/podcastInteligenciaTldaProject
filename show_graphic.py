import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('youtube_views.csv')

df = df.fillna(0)

views_by_playlist = df.sum()

views_by_playlist_df = views_by_playlist.to_frame(name='views')

views_by_playlist_df = views_by_playlist_df.sort_values(by='views')

plt.bar(views_by_playlist.index, views_by_playlist_df['views'])
plt.xlabel('Playlist')
plt.ylabel('Número de visualizações')
plt.title('Número de visualizações por playlist')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()
plt.show()
