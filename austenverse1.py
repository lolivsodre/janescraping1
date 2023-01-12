import pandas as pd

# Define url
url = "https://en.wikipedia.org/wiki/Jane_Austen_in_popular_culture"
# Read HTML in url
df = pd.read_html(url)

# Print DF & DF lengh
print(df)
print(len(df))

# Assign DataFrames to variables
# Convert it to csv file
# Sense & Sensibility Data Frame
df[0].to_csv('sense.csv')
sense = df[0]
# Pride & Prejudice Data Frame
df[1].to_csv('pride.csv')
# Mainsfield Park Data Frame
df[2].to_csv('mainsfield.csv')
# Emma Data Frame
df[3].to_csv('emma.csv')
# Northanger Abbey Data Frame
df[4].to_csv('northabbey.csv')
# Persuasion Data Frame
df[5].to_csv('persuasion.csv')
# Sanditon Data Frame
df[6].to_csv('sanditon.csv')
# Lady Susan Data Frame
df[7].to_csv('ladysusan.csv')

# Reading Sense & Sensibility DataFrame
sensedf = pd.read_csv('sense.csv')
# Drop columns
sensedf = sensedf.drop(sensedf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
sensedf['Novel'] = "Sense and Sensibility"
# rename Adaptation Column
sensedf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
sensedf['Title'] = sensedf['Title'].str.replace("Television Miniseries", " ")
sensedf['Title'] = sensedf['Title'].str.replace("Feature Film", " ")
# create Type Column
sensedf['Type'] = ["Television Miniseries",
                   "Television Miniseries",
                   "Feature Film",
                   "Television Miniseries"]
print(sensedf)

# Reading Pride & Prejudice DataFrame
pridedf = pd.read_csv('pride.csv')
pridedf = pridedf.drop(pridedf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "novel on" Column
pridedf['Novel'] = "Pride and Prejudice"
# Rename Adaptation column to Title
pridedf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
pridedf['Title'] = pridedf['Title'].str.replace("Television movie", " ")
pridedf['Title'] = pridedf['Title'].str.replace("Feature film", " ")
pridedf['Title'] = pridedf['Title'].str.replace("Television miniseries", " ")
# create Type Column
pridedf['Type'] = ["Television movie",
                   "Feature film",
                   "Television miniseries",
                   "Television miniseries",
                   "Television miniseries",
                   "Television miniseries",
                   "Television miniseries",
                   "Television miniseries",
                   "Television miniseries",
                   "Television miniseries",
                   "Feature film"]
pridedf[['Title', 'Year', 'Type', 'Novel']]
print(pridedf)

# Reading Mainsfield Park DataFrame
mainsfdf = pd.read_csv('mainsfield.csv')
# Drop columns
mainsfdf = mainsfdf.drop(mainsfdf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
mainsfdf['Novel'] = "Mansfield Park"
# rename Adaptation Column
mainsfdf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
mainsfdf['Title'] = mainsfdf['Title'].str.replace("Television miniseries", " ")
mainsfdf['Title'] = mainsfdf['Title'].str.replace("Feature Film", " ")
mainsfdf['Title'] = mainsfdf['Title'].str.replace("Television Movie", " ")
# create Type Column
mainsfdf['Type'] = ["Television Miniseries",
                    "Feature Film",
                    "Television Movie"]
print(mainsfdf)

# Reading Emma DataFrame
emmadf = pd.read_csv('mainsfield.csv')
# Drop columns
emmadf = emmadf.drop(emmadf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# importing Dataset Emma
emmadf = pd.read_csv('emma.csv')
emmadf = emmadf.drop(emmadf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
emmadf['Novel'] = "Emma"
# rename Adaptation Column
emmadf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
emmadf['Title'] = emmadf['Title'].str.replace("Feature film", " ")
emmadf['Title'] = emmadf['Title'].str.replace("Feature Film", " ")
emmadf['Title'] = emmadf['Title'].str.replace("Television miniseries", " ")
emmadf['Title'] = emmadf['Title'].str.replace("Television movie", " ")
# create Type Column
emmadf['Type'] = ["Feature film",
                  "Television miniseries",
                  "Television miniseries",
                  "Television miniseries",
                  "Feature film",
                  "Television movie",
                  "Television miniseries",
                  "Feature film"]
print(emmadf)
# Reading Northanger Abbey DataFrame
northadf = pd.read_csv('northabbey.csv')
# Drop columns
northadf = northadf.drop(northadf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# importing Dataset Northanger Abbey
northadf = pd.read_csv('northabbey.csv')
northadf = northadf .drop(northadf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
northadf['Novel'] = "Northanger Abbey"
# rename Adaptation Column
northadf .rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
northadf['Title'] = northadf['Title'].str.replace("Feature film", " ")
northadf['Title'] = northadf['Title'].str.replace("Feature Film", " ")
northadf['Title'] = northadf['Title'].str.replace("Television miniseries", " ")
northadf['Title'] = northadf['Title'].str.replace("Television film", " ")
# create Type Column
northadf['Type'] = ["Television miniseries",
                    "Television film",
                    "Television film"]
print(northadf)
# Reading Persuasion DataFrame
persdf = pd.read_csv('persuasion.csv')
persdf = persdf.drop(persdf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
persdf['Novel'] = "Persuasion"
# rename Adaptation Column
persdf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
persdf['Title'] = persdf['Title'].str.replace("Feature Film", " ")
persdf['Title'] = persdf['Title'].str.replace("Television Miniseries", " ")
persdf['Title'] = persdf['Title'].str.replace("Television Film", " ")
# create Type Column
persdf['Type'] = ["Television Miniseries",
                  "Television miniseries",
                  "Television miniseries",
                  "Television Film",
                  "Television Film",
                  "Feature Film"]
print(persdf)
# Reading Sanditon DataFrame
# importing Dataset Sanditon
sanddf = pd.read_csv('sanditon.csv')
sanddf = sanddf.drop(sanddf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
sanddf['Novel'] = "Sanditon"
# rename Adaptation Column
sanddf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
sanddf['Title'] = sanddf['Title'].str.replace("Television series", " ")
# create Type Column
sanddf['Type'] = ["Television Series"]
print(sanddf)
# Reading Lady Susan DataFrame
ladydf = pd.read_csv('ladysusan.csv')
ladydf = ladydf.drop(ladydf.columns[[3, 4, 5, 6, 7, 8]], axis=1)
# create "Novel" Column
ladydf['Novel'] = "Lady Susan"
# rename Adaptation Column
ladydf.rename(columns={"Adaptation": "Title"}, inplace=True)
# delete Type of Adaptation from Title column
ladydf['Title'] = ladydf['Title'].str.replace("Feature Film", " ")
# create Type Column
ladydf['Type'] = ["Feature Film"]
print(ladydf)

# Combine dataframes into one
frames = [sensedf, pridedf, mainsfdf, emmadf, northadf, persdf, sanddf, ladydf]
result = pd.concat(frames)
# Rename Novel colum to Based on
result.rename(columns={"Novel": "Based on"}, inplace=True)
# Reorder results datagrame
result = result[["Title", "Year", "Based on", "Type"]]

# Sort Values
result.sort_values(['Year'],
                   axis=0,
                   ascending=True, inplace=True)
print(result)
# Convert result DataFrame to csv.
result.to_csv('adaptations.csv')