from flask import Flask, request
import csv
import json
# import pandas as pd
app = Flask(__name__)


# movies_df = pd.read_csv('imdb-movie-data.csv', index_col='Rank')
# print(movies_df.head())
# genre = movies_df['Genre']
# print(genre)


def filter_genre(genre):

    lmdb_data = []

    with open('imdb-movie-data.csv', 'r') as csv_file:
        content = csv.DictReader(csv_file)
        if genre == None:
            for movie in content:
                lmdb_data.append(movie)

        for movie in content:
            genres = movie['Genre'].split(',')
            if genre.lower() in [item.lower() for item in genres]:
                lmdb_data.append(movie)

    return lmdb_data

print(len(filter_genre('western')))

@app.route("/")
def root():
    gn = request.args.get('genre')
    return json.dumps(filter_genre(gn))

@app.route("/action")
def action():
    return json.dumps(filter_genre('action'))

@app.route("/adventure")
def adventure():
    return json.dumps(filter_genre('adventure'))

# @app.route("/western")
# def western():
#     # print(filter_genre('Western'))
#     return json.dumps(filter_genre('Western'))

# @app.route("/biography")
# def biography():
#     return json.dumps(filter_genre('Biography'))

@app.route("/comedy")
def comedy():
    return json.dumps(filter_genre('comedy'))

@app.route("/drama")
def drama():
    return json.dumps(filter_genre('drama'))

@app.route("/romance")
def romance():
    return json.dumps(filter_genre('romance'))


app.run('0.0.0.0', port=8080)