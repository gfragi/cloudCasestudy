from pycaret.clustering import *
import my_functions as mf
import pandas as pd
import plotly.express as px
from pycaret.utils import version


version()


iaas = pd.read_csv(f'datasets/iaas_data.csv')
caas = pd.read_csv(f'datasets/caas_data.csv')
iaas = iaas[['Provider','CPU', 'RAM']]
caas = caas[['Provider','CPU', 'RAM']]

frames = [iaas, caas]
df = pd.concat(frames, ignore_index=True)


fig = px.scatter(df, x='CPU', y='RAM', size='RAM')
fig.show()


s = setup(df, normalize = True, numeric_features=('CPU', 'RAM'), log_experiment=True, log_data=True, experiment_name='cluster-rsc_ciaas',
          log_plots=True, pca=True, log_profile=True)


kmeans = create_model('kmeans', num_clusters=4)

# %%
fig = plot_model(kmeans, 'elbow')
fig.show()

result = assign_model(kmeans)
result.head()


predictions = predict_model(kmeans, data=df)
predictions.head()