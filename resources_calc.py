# %%============== Import libraries =========
import numpy as np
import pandas as pd
import warnings
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import stats
from scipy import stats
import my_functions as mf


# %%==============  Define the initial values  =========
tot_users = 100000

# initiate the total variables for each component (i_* = mf.iaas, c_* = mf.iaas,
i_total_ram = 0
i_total_cores = 0
i_total_disk = 0
c_total_ram = 0
c_total_cores = 0
c_total_disk = 0

# %% ============ Calculate total resources per technology ============

i_nginx_resc = mf.iaas.nginx(tot_users)
i_framework_resc = mf.iaas.framework(tot_users)
i_rel_db_resc = mf.iaas.rel_db(tot_users)
i_memory_db_resc = mf.iaas.memory_db(tot_users)

c_nginx_resc = mf.iaas.nginx(tot_users)
c_framework_resc = mf.iaas.framework(tot_users)
c_rel_db_resc = mf.iaas.rel_db(tot_users)
c_memory_db_resc = mf.iaas.memory_db(tot_users)

i_components_list = [i_nginx_resc, i_framework_resc, i_rel_db_resc, i_memory_db_resc]
c_components_list = [c_nginx_resc, c_framework_resc, c_rel_db_resc, c_memory_db_resc]

# initiate the total variables for each component
total_ram = 0
total_cores = 0
total_disk = 0

# calculate the totals
for i in range(0, 4):
    i_total_ram = i_components_list[i].get('ram') + total_ram
    i_total_cores = i_components_list[i].get('cores') + total_cores
    i_total_disk = i_components_list[i].get('disk') + total_disk
    c_total_ram = i_components_list[i].get('ram') + total_ram
    c_total_cores = i_components_list[i].get('cores') + total_cores
    c_total_disk = i_components_list[i].get('disk') + total_disk


