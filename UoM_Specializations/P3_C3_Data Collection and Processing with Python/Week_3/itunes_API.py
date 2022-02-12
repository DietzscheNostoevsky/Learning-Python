# %%
import json
import requests
import requests_with_caching

# %%
parameters = {"term": "Ann Arbor", "entity": "podcast"}

iTunes_response = requests.get(
    "https://itunes.apple.com/search", params=parameters)
py_data = json.loads(iTunes_response.text)

# %%

results = [r['trackName'] for r in py_data['results']]
i = 1
for _ in results:

    print(i, ":", _)
    i += 1

# %%
