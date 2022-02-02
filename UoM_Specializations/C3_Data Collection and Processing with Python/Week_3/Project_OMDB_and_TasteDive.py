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
# Define a function called get_movie_data.
# It takes in one parameter which is a string
# that should represent the title of a movie you want to search.
# The function should return a dictionary with information about that movie.


def get_movie_data(movie):
    moviename = str(movie)
    apikey = "c451a42"
    base_url = "http://www.omdbapi.com/"
    paramdict = {}

    paramdict['t'] = moviename
    paramdict['r'] = 'json'
    paramdict['apikey'] = apikey

    omdbresp = requests.get(base_url, paramdict)
    y = omdbresp.json()

    return y


# -----------------------------------------------------------------------
# Now write a function called get_movie_rating.
# It takes an OMDB dictionary result for one movie
# and extracts the Rotten Tomatoes rating as an integer.
# For example, if given the OMDB dictionary for “Black Panther”,
# it would return 97. If there is no Rotten Tomatoes rating, return 0.


def get_movie_rating(indict):

    if indict['Ratings'][1]['Source'] == 'Rotten Tomatoes':
        rating = int(indict['Ratings'][1]['Value'].replace('%', ''))
    else:
        rating = 0

    return rating


# -----------------------------------------------------------------------
# Define a function get_sorted_recommendations.
# It takes a list of movie titles as an input.
# It returns a sorted list of related movie titles as output,
# up to five related movies for each input movie title.
# The movies should be sorted in descending order by their
# Rotten Tomatoes rating, as returned by the get_movie_rating function.
# Break ties in reverse alphabetic order,
# so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

# %%
def get_sorted_recommendations(movielist):
