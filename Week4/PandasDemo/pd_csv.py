import pandas as pd
import csv
import matplotlib.pyplot as plt

path = './../../SourceData/pokemon.csv'

# The "old school" read of a csv (which is usefull to make sure we have the right path, and that the data is what we expect!)
# with open(path, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(*row)

# The Pandas way of helping us out, letting us read and transform data into a dataframe in one command!
df = pd.read_csv(path, index_col='ID', usecols=['ID', 'Total', 'HP', 'Attack', 'Defense', 'Speed'])
# print(df[['Name','Generation']])

df.sort_values('HP', inplace=True)
#print(df)


# Correlations: (-1) - (1) range, higher abs value indicates a more direct correlation, lower abs value indicates less correlation
# Some good indications - high and low values, identity values (1-to-1 correlation) across the diagonal
# print(df.corr())


# Merge:
    # - have a value in common
    # - what method of join/merge to perform
        # - inner, outer, left, right, cross, self

print("Data Set A")
a = {"A": [1, 2, 3, 4, 5, 8, 9],
     "B":[2, None, 4, 5, 6, 9, 10],
     "C":[3, 4, 5, 6, 7, 10, 11]}
A = pd.DataFrame(a)
print(A)

print()
print("DataSet B")
b = {"A": [1, 2, 3, 4, 5, 6, 7],
     "D":[2, 3, 4, 5, 6, 7, 8],
     "E":[3, 4, 5, None, 7, 8, 9]}
B = pd.DataFrame(b)
print(B)

# print()
# print("Inner Merge")
# print(A.merge(B, "inner")) # only keep matching entries that appear on both data sets

# print()
# print("Outer Merge")
# print(A.merge(B, "outer")) # keep ALL entries that appear on ALL data sets (and fill missing values with "None")

# print()
# print("Left Merge")
# print(A.merge(B, "left")) # kept all of the entries from "the left", and any entry with a matching value on "the right"

# print()
# print("Right Merge")
# AB = A.merge(B, "right").interpolate() # kept all of the entries from "the right", and any entry with a matching value on "the left"
# print(AB)

# We can exmine the correlation of merged data:
# print(AB.corr())

# And graph it out for a visual too!:
# fig, ax = plt.subplots()
# ax.scatter(AB['A'], AB['B'])
# ax.scatter(AB['A'], AB['E'])
# ax.set(xlabel="A", ylabel="Value", title="B vs E over A")
# ax.legend(("b", "e"))
# fig.savefig("ABE.png")

# Histogram
# plt.hist(df['HP'])
# plt.show()
# plt.savefig("HP_Histogram.png")

# Scatter plotting
# plt.scatter(df['Attack'], df['Defense'])
# plt.savefig("attack_defense.png")

# plt.plot(df['HP'], df['Speed'])
# plt.plot(df['HP'], df['Defense'])
# plt.savefig("HP-Speed-Line.png")

fig, ax = plt.subplots()
ax.plot(df['HP'], df['Speed'])
ax.plot(df['HP'], df['Defense'])
ax.set(xlabel="HP", ylabel="Value", title="Speed vs Defense over HP")
ax.set_xscale('linear')
ax.set_yscale('linear')
ax.set_xlim(0, 200)
ax.grid()
ax.legend(('Speed','Defense'))
fig.savefig("HP-Speed-Line.png")