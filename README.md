# 🎧 Spotify Data Analysis

> Exploratory data analysis project using real Spotify data to uncover trends in music and popularity.
> # 🎧 Spotify Data Analysis

## ⚙️ Tech Stack

* Python
* pandas
* matplotlib

## 📊 Key Analysis

### 🎵 Music Features

* Calculated average tempo (BPM) across all tracks
* Analyzed distribution of musical keys (converted numeric values into musical notation such as C, D, E, etc.)

---

### ⭐ Popularity Insights

* Computed average track popularity
* Identified Top 10 and Top 20 most popular songs
* Observed that popularity scores are concentrated between 90–100

---

### 🔗 Correlation Analysis

* Evaluated relationship between **song duration and popularity**
* Result: correlation ≈ 0 → no meaningful relationship

---

### 💿 Album Analysis

* Identified album with the highest number of tracks
* Created a feature to classify **singles** (albums with only one track)
* Calculated total number of singles in the dataset

---

### 📝 Text Analysis

* Extracted most frequent words in song titles
* Cleaned text by removing symbols and irrelevant tokens
* Identified common naming patterns

---

### 🎼 Genre Analysis

* Identified Top 5 most common genres
* Visualized genre distribution

---

## 📈 Visualizations

### Top 5 Genres

![Top Genres](images/top_5_genres.png)

### Most Common Words in Song Titles

![Common Words](images/common_words.png)

### Top 20 Songs by Popularity

![Top Songs](images/top_20_songs.png)

---

## 🔍 Key Insights

* Song duration has **no significant impact on popularity**
* Popular tracks are concentrated in a narrow score range
* Certain genres dominate the dataset
* Song titles frequently reuse common words
* A large portion of tracks are classified as singles

---

## 🚀 Future Improvements

* Add interactive visualizations using Plotly
* Perform deeper text analysis (NLP techniques)
* Explore additional correlations between features
* Build a predictive model for song popularity

---

## 👤 Author

**Breno Larocerie Zamponi**
## License
MIT

