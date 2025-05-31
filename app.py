import pandas as pd
import numpy as np
import streamlit as st
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise  import cosine_similarity
from nltk.stem.porter import PorterStemmer

movies=pd.read_csv("C:\\MoviesRecommender\\tmdb_5000_movies.csv")
credits=pd.read_csv("C:\\MoviesRecommender\\tmdb_5000_credits.csv")

movies=movies.merge(credits,left_on='id',right_on='movie_id')

movies.drop(columns=['title_y','movie_id'],inplace=True)
movies.rename(columns={'title_x':'title'},inplace=True)

movies=movies[['genres','id','keywords','title','overview','cast','crew']]
movies.dropna(inplace=True)

def convert(list):
    L=[]
    for i in ast.literal_eval(list):
        L.append(i['name'])
    return L

def convert_(list):
    L=[]
    counter=0
    for i in ast.literal_eval(list):
        L.append(i['name'])
        counter=counter+1
        if counter==3:
            break
    return L

def convert1(list):
    L=[]
    for i in ast.literal_eval(list):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)
movies['cast']=movies['cast'].apply(convert_)
movies['crew']=movies['crew'].apply(convert1)

movies['overview']=movies['overview'].apply(lambda x:x.split())

movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']
final_df=movies[['id','title','tags']]

final_df['tags']=final_df['tags'].apply(lambda x:" ".join(x))
final_df['tags']=final_df['tags'].apply(lambda x:x.lower())

ps=PorterStemmer()
def stem(object):
    l=[]
    for i in object.split():
        l.append(ps.stem(i))

    return " ".join(l)

final_df['tags']=final_df['tags'].apply(stem)

vec=CountVectorizer(max_features=5000,stop_words='english')
vectors=vec.fit_transform(final_df['tags']).toarray()
scores = cosine_similarity(vectors)

def recommend(movie):
    idx = final_df[final_df['title']==movie].index.item()
    L=[]
    for i in scores:
        L.append(i[idx])

    K= sorted(L,reverse=True)[1:6]
    L=[]
    for i in range(len(scores)):
        if scores[i][idx] in K:
            L.append(i)
    K=[]
    for i in L:
        K.append(final_df.iloc[i]['title'])

    return K
        
st.title('Movies Recommender')

option = st.selectbox(
    'Choose your movie for recommendations:',
     final_df['title']
)

if st.button('Recommend'):
    a=recommend(option)
    for i in a:
        st.write(i)