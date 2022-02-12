
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
import requests_with_caching


def get_movies_from_tastedive(searchquery):

    moviename = str(searchquery)
    apikey = ""
    base_url = "https://tastedive.com/api/similar"
    paramdict = {}

    paramdict['q'] = moviename
    paramdict['type'] = "movies"
    paramdict['limit'] = '5'

    tastediveresponse = requests_with_caching.get(base_url, paramdict)
    x = tastediveresponse.json()

    return x
# -----------------------------------------------------------------------


def extract_movie_titles(indict):
    x = indict

    movielist = []
    for res1 in x['Similar']['Results']:
        movie = res1['Name']
        movielist.append(movie)
    return movielist
# -----------------------------------------------------------------------


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
get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])
