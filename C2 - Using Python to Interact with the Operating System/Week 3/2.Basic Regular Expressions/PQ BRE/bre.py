# %%
import re

# %%
result = re.search(r"aza", "bazaar")  # r means rawstring

# %%

res = re.search(r'aza', 'tulips')
# %%
res1 = re.search(r"^x", "xenon")
# %%
res2 = re.search(r"p...ng", "pedsnguin")

# %%
res3 = re.search(r"p.ng", "Pangaea", re.IGNORECASE)
# %%
