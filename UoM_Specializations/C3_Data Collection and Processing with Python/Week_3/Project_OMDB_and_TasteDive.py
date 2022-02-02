# %%
import json
import requests

# -----------------------------------------------------------------------
# Define a function, called get_movies_from_tastedive.
# It should take one input parameter,
# a string that is the name of a movie or music artist.
# The function should return the 5 TasteDive results
# that are associated with that string
# be sure to only get movies, not other kinds of media.
# It will be a python dictionary with just one key, ‘Similar’.


def get_movies_from_tastedive(searchquery):

    moviename = str(searchquery)
    apikey = ""
    base_url = "https://tastedive.com/api/similar"
    paramdict = {}

    paramdict['q'] = 'movie:' + moviename
    paramdict['type'] = "movies"
    paramdict['limit'] = '5'

    tastediveresponse = requests.get(base_url, paramdict)
    x = tastediveresponse.json()

    return x
# -----------------------------------------------------------------------
# Next, you will need to write a function that extracts
# just the list of movie titles from a dictionary
# returned by get_movies_from_tastedive.
# Call it extract_movie_titles.


def extract_movie_titles(indict):
    x = indict

    movielist = []
    for res1 in x['Similar']['Results']:
        movie = res1['Name']
        movielist.append(movie)
    return movielist
# -----------------------------------------------------------------------
# you’ll write a function, called get_related_titles.
# It takes a list of movie titles as input.
# It gets five related movies for each from TasteDive,
# extracts the titles for all of them,
# and combines them all into a single list.
# Don’t include the same movie twice.


def get_related_titles(inlist):
    retlist = []
    for movie in inlist:
        movielist = extract_movie_titles(get_movies_from_tastedive(movie))
        for m in movielist:
            if m in retlist:
                continue
            else:
                retlist.append(m)
    return retlist
# -----------------------------------------------------------------------
