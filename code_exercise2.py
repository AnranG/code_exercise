import pandas as pd
import re


file = open('soccer.dat', 'r')
raw_data = file.readlines()[2:-1]
data = []

# get the header for the table
header = [x for x in raw_data[0].split(' ') if len(x)>0]

for line in raw_data[1:]:

    line = line.replace("-",' ')
    item = [x for x in line.split(' ') if len(x) >= 1]
    num = [int(x) for x in item[2:]]

    if len(item) > 1:
        item = [item[1]] + num
        data.append(item)


df = pd.DataFrame(data)
df.columns = header

# calculate the difference
df['diff'] = abs(df['F'] - df['A'])
print("The team with the smallest difference in ‘for’ and ‘against’ goals:")
# return the row with minimum diff
print(df[df['diff'] == df['diff'].min()])
