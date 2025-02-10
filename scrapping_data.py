import pandas as pd

url ="https://en.wikipedia.org/wiki/Demographics_of_Indonesia"

tables = pd.read_html(url)

data = tables[1]
data.to_csv('capital.csv')