import pandas as pd

#print("hello again everyone!")

# pandas comes with two structures that we can interact with: Series and DataFrames

# Series: 1D - a structured collection of one dimension
# DataFrame: 2D - a structured "table" of rows and columns

data = { 'Names': ['Alice', 'Bob', 'Drew', 'Romeo'],
        'Age': [25, 30, 31, 28],
        'City': ['New York', 'London', 'Knoxville', 'Los Angeles']}

df = pd.DataFrame(data)

# new entry using .loc() - location
new_row = {'Names': 'Richard', 'Age':33, 'City': 'Oklahoma City'}
#dataframe.loc(len(dataframe)) = new_entry
df.loc[len(df)] = new_row

# new entry using pd.concat() - concatentate to structures
new_row = {'Names': 'Jonathan', 'Age':28, 'City': 'Miami'}
new_row_df = pd.DataFrame([new_row])
df = pd.concat([df, new_row_df], ignore_index=True)

from csv import writer
from io import StringIO #ByteIO let us treat the strings or the bytes like a file object - in memory - for reading and writing

output = StringIO()
df.to_csv(output)
csv_writer = writer(output)
new_row = [[6, 'Charles', 30, 'Philadelphia'],[7,'Emily',35, 'Reston'],[8,'Kurt',40,'Reston']]
#csv_writer.writerow(str(item) for item in new_row)
for row in new_row:
#    csv_writer.writerow(str(item) for item in row)
    csv_writer.writerow(row) #for item in row)
output.seek(0) # returning the "cursor" to the top of the file object
df = pd.read_csv(output, index_col=0)

# don't forget about inplace= to decide if you're operating on the same objet, or producing a new one

# a new object may be less space/memory effecient, but MAYBE faster(?)
new_df = df.rename(columns={'Names': 'First Name'})
# reusing the same object again saves memory, but may be slower(?)
df.rename(columns={'Names': 'First Name'}, inplace=True)

# Filter
old_folks = df[df['Age'] > 30]
# Filtering with Query syntax
old_folks_again = df.query('Age > 30')

# Reset the index
old_folks_again.reset_index(drop=True, inplace=True)


print(old_folks_again)