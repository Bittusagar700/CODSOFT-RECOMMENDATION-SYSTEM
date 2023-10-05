'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import numpy as np
import pandas as pd
data = {
    'User1': [5, 4, 0, 0, 0, 0],
    'User2': [0, 0, 5, 4, 0, 0],
    'User3': [0, 0, 0, 0, 5, 4],
    'User4': [4, 5, 0, 0, 0, 0],
}

movies = ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5', 'Movie6']

df = pd.DataFrame(data, index=movies)
def cosine_similarity(user1, user2):
    numerator = np.dot(user1, user2)
    denominator = np.linalg.norm(user1) * np.linalg.norm(user2)
    return numerator / denominator
def get_movie_recommendations(user, df, num_recommendations=3):
    similar_users = {}
    
    for col in df.columns:
        if col != user:
            similarity = cosine_similarity(df[user], df[col])
            similar_users[col] = similarity
    
    # Sort the users by similarity in descending order
    similar_users = dict(sorted(similar_users.items(), key=lambda x: x[1], reverse=True))
    
    recommendations = []
    for movie in df.index:
        if df[user][movie] == 0:
            score = 0
            total_similarity = 0
            for other_user, similarity in similar_users.items():
                if df[other_user][movie] != 0:
                    score += df[other_user][movie] * similarity
                    total_similarity += similarity
            if total_similarity > 0:
                recommendations.append((movie, score / total_similarity))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations[:num_recommendations]
user_to_recommend = 'User1'
recommendations = get_movie_recommendations(user_to_recommend, df)

print(f"Top movie recommendations for {user_to_recommend}:")
for movie, score in recommendations:
    print(f"{movie}: Score {score}")

