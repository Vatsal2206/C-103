import pandas as pd
import plotly.express as pe

df = pd.read_csv('data.csv')
barGraph = pe.bar(df, x='Country', y = 'InternetUsers',title='Internet Users per Country', color='Country')
barGraph.show()