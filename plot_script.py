import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

df = pd.read_csv('parallel_plot.csv', delimiter='\t')
df.columns = ['team', 'Start', 'GW4', 'Now', 'colour']

labels = df.sort_values('Start', ascending=True)['team'].tolist()

plt.figure(figsize=(10, 10))
parallel_coordinates(df[['team', 'Start', 'GW4', 'Now']], 'team', colormap=plt.get_cmap('Dark2'), linewidth=4)
plt.yticks(np.arange(1, 21, 1.0), labels)
plt.gca().invert_yaxis()
plt.legend().remove()
plt.savefig('parallel_plot.png')
