# -----------------------------------------------------------------------
# Define a function get_sorted_recommendations.
# It takes a list of movie titles as an input.
# It returns a sorted list of related movie titles as output,
# up to five related movies for each input movie title.
# The movies should be sorted in descending order by their
# Rotten Tomatoes rating, as returned by the get_movie_rating function.
# Break ties in reverse alphabetic order,
# so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
# -----------------------------------------------------------------------
# %%

import requests

from Project_OMDB_and_TasteDive import *

# -----------------------------------------------------------------------
#get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


def get_sorted_recommendations(movielist):

    relatedmovies = get_related_titles(movielist)
    retlist: []
    moviedict = {}
    for movie in relatedmovies:
        rating = get_movie_rating(get_movie_data(movie))

        moviedict[movie] = rating
    sortedmoviedict = dict(
        sorted(moviedict.items(), key=lambda k: (k[1], k[0]), reverse=True))
    retlist = list(sortedmoviedict.keys())

    return retlist


# %%
get_sorted_recommendations(['Avengers', 'Iron Man', 'Thor'])


# %%
