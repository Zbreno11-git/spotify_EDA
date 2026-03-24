import pandas as pd
import matplotlib.pyplot as plt

df_spotify = pd.read_csv('spotify_songs.csv')

    #Summary:
print(df_spotify.head())
print(df_spotify.describe())
print(df_spotify.columns)
print()

    #Average BPM:
#print(df_spotify['tempo'].notnull().value_counts())
    #No null values
print(f'\nAverage BPM: {df_spotify['tempo'].mean():.2f}')

    #Key Distribution:
    #Put actual Keys instead of numbers
tons = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'}
df_spotify['key'] = df_spotify['key'].replace(tons)
    #Create a new DataFrame to show the distribution
percent_key = lambda df, coluna: pd.DataFrame({
    'Total': df[coluna].value_counts(),
    'Percentage': (df[coluna].value_counts(normalize=True) * 100)
})
new_dis_df = percent_key(df_spotify, 'key')
print(new_dis_df)

    #Average popularity and top 10 songs:
    #Discovering any Nulls/Nan
#print(df_spotify.track_popularity.isnull().values.any())
    #Avg Popul.
print(f'\nAverage popularity: {df_spotify.track_popularity.mean():.2f}')
    #Top 10 songs:
    #Sort the values, remove the duplicates but keep one/original, show the top 10,...
    #...show only name and popularity, and reset the index 0-9
top_10 = df_spotify.sort_values('track_popularity', ascending=False).drop_duplicates(subset='track_name', keep='first').head(10)[['track_name', 'track_popularity']].reset_index()
print(f'\nTop 10: {top_10}')

    #Correlation between duration and popularity:
corr = df_spotify.duration_ms.corr(df_spotify.track_popularity)
print(f'\nThe correlation between duration and popularity is {corr:.2f}')
    #Correlation is not close to 1 or -1,...
# ...correlation between duration and popularity was -0.03, indicating no meaningful relationship

    #What album have the most songs:
album_counts = df_spotify.groupby('track_album_name')['track_name'].count()
    #Idxmax to find the name fo the album and max for the num of songs
print(f'\nThe album with more songs is {album_counts.idxmax()} with {album_counts.max()} songs!')

    #Create a column = Singles for albums with only one song: (Bool)
df_spotify['single'] = df_spotify['track_album_name'].map(album_counts) == 1
    #Info about it (count = 32833)
#print(df_spotify['single'].describe())
    #How many singles: (True = 14210)
print(f'\nNumber of singles in the dataset: {df_spotify['single'].sum()}')
    #Could use value_counts() to get the counts for True and False,...
#...but .sum() counts just the singles(True) already.

    #Most common words in the song titles: *With visualization
titles = df_spotify['track_name'].str.lower().str.split(expand=True).stack()
titles = titles.drop(titles[titles.isin(['#', '-', '$', '&', '(feat.'])].index)
plt.bar(titles.value_counts().head(10).index, titles.value_counts().head(10).values, color='green')
plt.xlabel('Words')
plt.ylabel('Count')
plt.title('Most common words in the song titles')
plt.tight_layout()
plt.savefig('/Users/luanabreno/Desktop/Images/common_words.png', dpi=150, bbox_inches='tight')
plt.show()

    #Top 5 genres: *With Visualization
top_genres = df_spotify.playlist_genre.value_counts().head(5)
plt.bar(top_genres.index, top_genres.values, color='red')
plt.ylim(5000,6100)
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Top 5 Genres')
plt.savefig('/Users/luanabreno/Desktop/Images/top_5_genres.png', dpi=150, bbox_inches='tight')
plt.show()

    #Top 20 songs: *With Visualization
plt.figure(figsize=(8, 6))
top_20 = df_spotify.sort_values('track_popularity', ascending=False).drop_duplicates(subset='track_name', keep='first').head(20)[['track_name', 'track_popularity']].reset_index()
plt.barh(top_20['track_name'], top_20['track_popularity'])
    #Adjusting the axis so the difference between them is clearer
plt.xlim(90,100)
plt.xlabel('Popularity')
plt.ylabel('Song')
plt.title('Top 20 Songs')
plt.tight_layout()
plt.savefig('/Users/luanabreno/Desktop/Images/top_20_songs.png', dpi=150, bbox_inches='tight')
plt.show()
