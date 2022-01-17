# %%
import csv
import os
# %%
hosts = [["workstation.local", "192.168.0.1"], ["webserver.cloud", "1.1.1.1"]]

# %%
with open('hosts.csv', 'w') as hosts_csv:
    writer1 = csv.writer(hosts_csv)
    writer1.writerows(hosts)


# %%
