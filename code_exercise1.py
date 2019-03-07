import pandas as pd
import re


def get_min_spread(file_path):
    file = open(file_path, 'r')
    raw_data = file.readlines()[4:-2]
    data = []

    # get the header for the table
    header = [x for x in raw_data[0].split(' ') if len(x) > 1][:3]

    for line in raw_data[1:]:
        # skip the empty line
        if len(line) > 1:
            # leave number only, e.g. 97* -> 97
            item = [re.sub("\D", "", x) for x in line.split(' ') if len(x) >= 1]

            # convert str to int
            item = [int(x) for x in item[:3]]

            if len(item) > 1:
                data.append(item)

    df = pd.DataFrame(data)
    df.columns = header

    # calculate the temperature difference
    df['Spread'] = df['MxT'] - df['MnT']
    print("The day with the smallest temperature spread:")
    # return the row with minimum spread
    print(df[df['Spread'] == df['Spread'].min()])


get_min_spread('w_data (5).dat')