import pandas as pd

# rows is the list of dictionaries created by the code you provided
df = pd.DataFrame(rows)

# reorder columns
df = df[headers]

# remove duplicates
df.drop_duplicates(inplace=True)

# reset index
df.reset_index(drop=True, inplace=True)