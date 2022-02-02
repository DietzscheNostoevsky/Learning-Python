# %%
import requests
import json

# %%

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150])  # print the first 150 characters
print(page.url, "\n")  # print the url that was fetched
print("--------------------------------")

# %%
x = page.json()  # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2))  # pretty print the results


# %%
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
# https://www.google.com/search?q=%22violins+and+guitars%22&tbm=isch
print(results.url)

# %%
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150])  # print the first 150 characters
print(page.url)  # print the url that was fetched
# %%
new = requests.get("http://bar.com/goodstuff",
                   params={'greet': 'hi there', 'frosted': 'no'})
# %%
y = new.json()
print(type(y))

# %%
