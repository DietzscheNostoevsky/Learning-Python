# %%
import requests


def get_movies_from_tastedive(searchquery):

    moviename = str(searchquery)
    apikey = ""
    base_url = "https://tastedive.com/api/similar"
    paramdict = {}

    paramdict['q'] = moviename
    paramdict['type'] = "movies"
    paramdict['limit'] = '5'

    tastediveresponse = requests.get(base_url, paramdict)
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
def get_movie_rating(indict):
    rating = 0
    try:
        if indict['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            rating = int(indict['Ratings'][1]['Value'].replace('%', ''))
    except:
        rating = 0

    return rating


def get_sorted_recommendations(movielist):

    relatedmovies = get_related_titles(movielist)
    retlist = []
    moviedict = {}
    for movie in relatedmovies:
        rating = get_movie_rating(get_movie_data(movie))

        moviedict[movie] = rating
    sortedmoviedict = dict(
        sorted(moviedict.items(), key=lambda k: (k[1], k[0]), reverse=True))
    retlist = list(sortedmoviedict.keys())

    return retlist


#get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

# %%
