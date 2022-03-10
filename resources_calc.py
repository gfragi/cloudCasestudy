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
import plotly.io as pio
import random

pio.renderers.default = "browser"
import plotly.graph_objects as go

# %%==============  Define the initial values  =========

users = random.sample(range(1000, 300000), 15000)
tot_users = np.array(users)

iaas_dict = {}
caas_dict = {}

# %%==============  Calculate the total resources per technology by users   =========

for users in tot_users:
    iaas_dict[users] = mf.iaas.iaas_total(users)
    caas_dict[users] = mf.caas.caas_total(users)

# Convert dictionary to dataframe
iaas = pd.DataFrame.from_dict(iaas_dict)

caas = pd.DataFrame.from_dict(caas_dict)

# Transpose the dataframe
iaas = iaas.transpose()
caas = caas.transpose()

# Add a column for tech
iaas['technology'] = 'iaas'
caas['technology'] = 'caas'

# Make index to column
iaas.reset_index(inplace=True)
caas.reset_index(inplace=True)

# Rename the columns
iaas.columns = ['users', 'ram', 'cores', 'disk', 'technology']
caas.columns = ['users', 'ram', 'cores', 'disk', 'technology']

# Concatenate the dataframes
frames = [iaas, caas]
df = pd.concat(frames, ignore_index=True)

# %% ================ Visualization ========================
#
# Grouped figured with averaged value
fig = px.histogram(df, x="technology", y=['ram', 'cores', 'disk'], log_y=True,
                   barmode='group', text_auto=True, histfunc='avg')
fig.show()
fig.write_html("resources_compare.html")
# %%
fig2 = px.scatter(df, x="users", y=['ram', 'cores', 'disk'], facet_col='technology', log_y=True)
fig2.show()
fig2.write_html("users_resources.html")
