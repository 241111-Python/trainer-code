import pandas as pd
import csv
import matplotlib.pyplot as plt

path = './../../SourceData/pokemon.csv'

# with open(path, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(*row)

df = pd.read_csv(path, index_col='ID', usecols=['ID', 'Total', 'HP', 'Attack', 'Defense', 'Speed'])
# print(df[['Name','Generation']])


# Histogram
#plt.hist(df['HP'])
#plt.show()
#plt.savefig("HP_Histogram.png")

# Scatter plotting
# plt.scatter(df['Attack'], df['Defense'])
# plt.savefig("attack_defense.png")


df.sort_values('HP', inplace=True)
print(df)
plt.plot(df['HP'], df['Speed'])
plt.plot(df['HP'], df['Defense'])
plt.savefig("HP-Speed-Line.png")