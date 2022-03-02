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
import plotly.express as px
import my_functions as mf
import plotly.graph_objects as go

# %%==============  Define the initial values  =========
tot_users = 100000

iaas = pd.DataFrame(['vms', 'ram', 'cores', 'disk'])
caas = pd.DataFrame(['instances', 'ram', 'cores', 'disk'])

# %% ============ Calculate total resources per technology ============
# IaaS
iaas['technology'] = 'iaas'
iaas['nginx'] = mf.iaas.nginx(tot_users)
iaas['framework'] = mf.iaas.framework(tot_users)
iaas['rel_db'] = mf.iaas.rel_db(tot_users)
iaas['memory_db'] = mf.iaas.memory_db(tot_users)
iaas['totals'] = iaas['nginx'] + iaas['framework'] + iaas['rel_db'] + iaas['memory_db']

iaas.rename(columns={0: 'component'}, inplace=True)

#%% CaaS
caas['technology'] = 'caas'
caas['nginx'] = mf.caas.nginx(tot_users)
caas['framework'] = mf.caas.framework(tot_users)
caas['rel_db'] = mf.caas.rel_db(tot_users)
caas['memory_db'] = mf.caas.memory_db(tot_users)
caas['totals'] = caas['nginx'] + caas['framework'] + caas['rel_db'] + caas['memory_db']
caas.rename(columns={0: 'component'}, inplace=True)

frames = [iaas, caas]
df = pd.concat(frames, ignore_index=True, sort=False)
df = df.transpose()
headers = df.iloc[0]
new_df = pd.DataFrame(df.values[1:], columns=headers)
#%% ================ Visualization ========================



