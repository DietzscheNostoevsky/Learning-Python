# %%

# %%
import re
# %%
record = "Sabrina Green,802-867-5309,System Administrator"

# %%
new_record = re.sub(r",([\d-]+)", r"", record)
print(new_record)
# %%
