# %%
import requests
import json
import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = '639c929533f6a2f74a0c77f12738b3cc'

# %%


def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key  # from the above global variable
    # must be a comma separated string to work correctly
    params_diction["tags"] = tags_string
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests.get(
        baseurl, params=params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    # Paste the result into the browser to check it out...
    print(flickr_resp.url)
    return flickr_resp.json()


# %%
result_river_mts = get_flickr_data("river,mountains")

# Some code to open up a few photos that are tagged with the mountains and river tags...
# %%
photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    webbrowser.open(url)

# %%
