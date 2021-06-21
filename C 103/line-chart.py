import pandas as pd
import plotly.express as pe

df = pd.read_csv('line_chart.csv')
graph = pe.line(df ,x='Year', y ='Per capita income', color= 'Country', title='Per Capita Income in Countries')
graph.show()

