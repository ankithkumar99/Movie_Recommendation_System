import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Recommendation:
    def __init__(self, name):
        self.output_list = []
        self.f = 0
        movie_user_likes = name
        while self.f <= 16:
            self.df = pd.read_csv("Dataset1/IMDb movies.csv" + str(self.f) + ".csv")
            self.f += 1

            try:
                self.movie_id = self.get_id_from_title(movie_user_likes)
                self.movie_record = self.df[self.df.id == self.movie_id].squeeze()
                break
            except IndexError:
                continue

        self.f = 0
        while self.f <= 16:
            self.df = pd.read_csv("Dataset1/IMDb movies.csv" + str(self.f) + ".csv")
            self.f += 1
            #    print(movie_record)
            if self.f == 17:
                self.movie_record['id'] = 1279
            else:
                self.movie_record['id'] = 5000
            self.df = self.df.append(self.movie_record)

            self.movie_id = self.get_id_from_title(movie_user_likes)
            self.features = ['title', 'director', 'lead_actors', 'genre', 'language', 'country']
            for feature in self.features:
                self.df[feature] = self.df[feature].fillna('')

            self.df["combined_features"] = self.df.apply(self.combine_features, axis=1)

            self.cv = CountVectorizer()
            self.count_matrix = self.cv.fit_transform(self.df["combined_features"])
            self.cosine_sim = cosine_similarity(self.count_matrix)

            #    print(movie_id)
            self.similar_movies = list(enumerate(self.cosine_sim[self.movie_id]))
            #    print(similar_movies)
            self.sorted_similar_movies = sorted(self.similar_movies, key=lambda x: x[1], reverse=True)

            list1 = []
            self.list2 = self.output_list
            for i in range(len(self.sorted_similar_movies)):
                if i >= 12:
                    break
                list1.append(list(self.sorted_similar_movies[i]))
                list1[i][0] = self.get_title_from_id(list1[i][0])
            self.list2 = self.list2 + list1
            self.output_list = sorted(self.list2, key=lambda x: x[1], reverse=True)

        self.count = 0
        self.req_list = []
        for elements in self.output_list:
            if elements[0] == movie_user_likes:
                continue
            self.req_list.append(elements[0].capitalize())
            self.count += 1
            if self.count == 10:
                break

    def get_title_from_id(self, id1):
        return self.df[self.df.id == id1]["title"].values[0]

    def get_id_from_title(self, title):
        return self.df[self.df.title == title]["id"].values[0]

    @staticmethod
    def combine_features(row):
        try:
            return row['title'] + " " + row['director'] + " " + row['lead_actors'] + " " + row['genre'] + " " + row[
                'language'] + " " + row['country'] + " " + row['lead_actors'] + " " + row['lead_actors']
        except:
            print("Error:", row)


# a = Recommendation('darbar')
