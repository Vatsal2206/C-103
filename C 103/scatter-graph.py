import pandas as pd
import plotly.express as pe

df = pd.read_csv('data.csv')
scatterGraph = pe.scatter(df, x='Population', y = 'Per capita',size='Percentage', color='Country', size_max = 60)
scatterGraph.show()