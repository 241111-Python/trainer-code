import pandas as pd
import csv

path = './../../SourceData/pokemon.csv'

# with open(path, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(*row)

df = pd.read_csv(path, index_col='ID', usecols=['ID', 'Name', 'Type 1', 'Type 2', 'HP', 'Generation'])
# print(df[['Name','Generation']])
print(df)