# 🎬 Movie Recommendation System

A machine learning-based movie recommender system built using Python. This project predicts and suggests movies to users based on their preferences using collaborative and/or content-based filtering methods.

## 🚀 Project Overview

This project is designed to recommend movies to users using:

- ✅ **Content-Based Filtering**: Recommends similar movies using movie metadata like genres, keywords, and overview text.
- ✅ **Similarity Metrics**: Cosine similarity on movie vectors generated from text-based features.

---

## 🧰 Tech Stack

- `Python`
- `Pandas`, `NumPy`
- `Scikit-learn`
- `CountVectorizer`
- `Cosine Similarity`

---

## 📁 Dataset

- **TMDB 5000 Movie Dataset**  
  Contains detailed metadata including:
  - Movie titles
  - Overviews
  - Genres
  - Cast, Crew, Keywords

Source: [Kaggle TMDB Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 📊 Features Used

- Movie **genres**
- Cast and crew information
- Movie **overviews** (description)
- Keywords and tags

All features are cleaned, preprocessed, and vectorized using NLP techniques.

---

## 📌 How It Works

1. **Preprocessing**:
   - Remove stopwords, punctuation
   - stemming
2. **Vectorization**:
   - CountVectorizer
3. **Similarity Calculation**:
   - Cosine similarity to find most similar movies
4. **Recommendation Engine**:
   - Given a movie, returns top 5 similar movies

---

## 🔍 Example Usage

```python
recommend("Interstellar")
# Output: ['Inception', 'Gravity', 'The Martian', ...]
