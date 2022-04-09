"""Toygar Ülgen"""

import pandas as pd
import numpy as np 

########################################################################
########################################################################

                                #PART 1
                                
########################################################################
########################################################################
#%%#%%############## 2009_2010 Data ###############
"""Extracting from Excel"""
Defensive2009_2010 = pd.read_csv('2009-2010_Defensive.csv')
Offensive2009_2010 = pd.read_csv('2009-2010_Offensive.csv')
Passing2009_2010 = pd.read_csv('2009-2010_Passing.csv')
Summary2009_2010 = pd.read_csv('2009-2010_Summary.csv')
Output = pd.read_csv('Output.csv')

#%%##############      Dropping     ##############
"""Dropping the same Nan values in the columns"""
Defensive2009_2010 = Defensive2009_2010.dropna(axis='columns', how='all') 
"""Dropping the same Nan values in the rows"""
Defensive2009_2010 = Defensive2009_2010.dropna(axis='rows')
"""Dropping the same values in the rows"""
Defensive2009_2010 = Defensive2009_2010.drop_duplicates() 

Offensive2009_2010 = Offensive2009_2010.dropna(axis='columns', how='all')
Offensive2009_2010 = Offensive2009_2010.dropna(axis='rows')
Offensive2009_2010 = Offensive2009_2010.drop_duplicates()

Passing2009_2010 = Passing2009_2010.dropna(axis='columns', how='all')
Passing2009_2010 = Passing2009_2010.dropna(axis='rows')
Passing2009_2010 = Passing2009_2010.drop_duplicates()

Summary2009_2010 = Summary2009_2010.dropna(axis='columns', how='all')
Summary2009_2010 = Summary2009_2010.dropna(axis='rows')
Summary2009_2010 = Summary2009_2010.drop_duplicates()

#%%##########       Performing new headers       ##############
"""Assigning strings in the first row as headers"""
Defensive2009_2010.columns = Defensive2009_2010.iloc[0] 
Defensive2009_2010 = Defensive2009_2010[1:]
Offensive2009_2010.columns = Offensive2009_2010.iloc[0]
Offensive2009_2010 = Offensive2009_2010[1:]
Passing2009_2010.columns = Passing2009_2010.iloc[0]
Passing2009_2010 = Passing2009_2010[1:]
Summary2009_2010.columns = Summary2009_2010.iloc[0]
Summary2009_2010 = Summary2009_2010[1:]

#%%#############     Dropping     ##############
"""Dropping columns that mutual from Summary data between Summary data and other data."""
Summary2009_2010 = Summary2009_2010.drop('Apps', axis = 1)
Summary2009_2010 = Summary2009_2010.drop('Mins', axis = 1)
Summary2009_2010 = Summary2009_2010.drop('Goals', axis = 1)
Summary2009_2010 = Summary2009_2010.drop('Assists', axis = 1)
Summary2009_2010 = Summary2009_2010.drop('SpG', axis = 1)
Summary2009_2010 = Summary2009_2010.drop('PS%', axis = 1)
Summary2009_2010 = Summary2009_2010.drop('Rating', axis = 1)

#%%#############      New Feature RatingMin        ###########
Defensive2009_2010['RatingMin'] = Defensive2009_2010.Rating.astype(float) * Defensive2009_2010.Mins.astype(float)

#%%#############    Concat and Merge    ###########
Defensive2009_2010 = pd.concat([Defensive2009_2010.reset_index(drop=True), Offensive2009_2010.reset_index(drop=True)], axis=1, join="outer")
Defensive2009_2010 = pd.concat([Defensive2009_2010.reset_index(drop=True), Passing2009_2010.reset_index(drop=True)], axis=1, join="outer")

"""Dropping similar columns using drop_duplicated"""
Defensive2009_2010 = Defensive2009_2010.loc[:,~Defensive2009_2010.columns.duplicated()] 

Output2 = pd.merge(Defensive2009_2010.reset_index(drop=True), Summary2009_2010.reset_index(drop=True), how='outer', left_on='Player', right_on='Player')

#%%
"""Splitting based on paranthesis"""
creatingAppsS1 = Output2.Apps.str.split("(", expand=True)

"""Adding to integers that split based on paranthesis, on Output2"""
Output2['Apps'] = Output2.Apps.str.split("(", expand=True)[0]

"""Splitting based on second paranthesis"""
Output2['AppsS'] = creatingAppsS1[1].str.split(")", expand=True)[0]

"""Splitting the double space"""
aaa = Output2.Player.str.split("\n\n", expand=True)

"""Adding Player names which clean age and teams"""
Output2['Player'] = aaa[0]

"""Splitting comma """
aaa = aaa[1].str.split(", ",expand=True)

"""Adding Team"""
Output2['Team'] = aaa[0]

"""Adding Age"""
Output2['Age'] = aaa[1]

"""Adding Position"""
Output2['Position'] = aaa[2]

"""Replacing - to zero"""
Output2 = Output2.replace({'-': 0})
#%%################## 2010_2011 Data #########################
"""Extracting from Excel"""
Defensive2010_2011 = pd.read_csv('2010-2011_Defensive.csv')
Offensive2010_2011 = pd.read_csv('2010-2011_Offensive.csv')
Passing2010_2011 = pd.read_csv('2010-2011_Passing.csv')
Summary2010_2011 = pd.read_csv('2010-2011_Summary.csv')

#%%#%%##############      Dropping      ##############
"""Dropping the same Nan values in the columns"""
Defensive2010_2011 = Defensive2010_2011.dropna(axis='columns', how='all')
"""Dropping the same Nan values in the rows"""
Defensive2010_2011 = Defensive2010_2011.dropna(axis='rows')
"""Dropping the same values in the rows"""
Defensive2010_2011 = Defensive2010_2011.drop_duplicates() 

Offensive2010_2011 = Offensive2010_2011.dropna(axis='columns', how='all')
Offensive2010_2011 = Offensive2010_2011.dropna(axis='rows')
Offensive2010_2011 = Offensive2010_2011.drop_duplicates()

Passing2010_2011 = Passing2010_2011.dropna(axis='columns', how='all')
Passing2010_2011 = Passing2010_2011.dropna(axis='rows')
Passing2010_2011 = Passing2010_2011.drop_duplicates()

Summary2010_2011 = Summary2010_2011.dropna(axis='columns', how='all')
Summary2010_2011 = Summary2010_2011.dropna(axis='rows')
Summary2010_2011 = Summary2010_2011.drop_duplicates()

#%%#############       Performing new headers       ##############
"""Assigning strings in the first row as headers"""
Defensive2010_2011.columns = Defensive2010_2011.iloc[0] 
Defensive2010_2011 = Defensive2010_2011[1:]
Offensive2010_2011.columns = Offensive2010_2011.iloc[0]
Offensive2010_2011 = Offensive2010_2011[1:]
Passing2010_2011.columns = Passing2010_2011.iloc[0]
Passing2010_2011 = Passing2010_2011[1:]
Summary2010_2011.columns = Summary2010_2011.iloc[0]
Summary2010_2011 = Summary2010_2011[1:]

#%%#############     Dropping     ##############
"""Dropping columns that mutual from Summary data between Summary data and other data."""
Summary2010_2011 = Summary2010_2011.drop('Apps', axis = 1)
Summary2010_2011 = Summary2010_2011.drop('Mins', axis = 1)
Summary2010_2011 = Summary2010_2011.drop('Goals', axis = 1)
Summary2010_2011 = Summary2010_2011.drop('Assists', axis = 1)
Summary2010_2011 = Summary2010_2011.drop('SpG', axis = 1)
Summary2010_2011 = Summary2010_2011.drop('PS%', axis = 1)
Summary2010_2011 = Summary2010_2011.drop('Rating', axis = 1)

#%%#############      New Feature RatingMin        ###########
Defensive2010_2011['RatingMin'] = Defensive2010_2011.Rating.astype(float) * Defensive2010_2011.Mins.astype(float)

#%%#############    Concat and Merge    ###########
Defensive2010_2011 = pd.concat([Defensive2010_2011.reset_index(drop=True), Offensive2010_2011.reset_index(drop=True)], axis=1, join="outer")
Defensive2010_2011 = pd.concat([Defensive2010_2011.reset_index(drop=True), Passing2010_2011.reset_index(drop=True)], axis=1, join="outer")

"""Dropping similar columns using drop_duplicated"""
Defensive2010_2011 = Defensive2010_2011.loc[:,~Defensive2010_2011.columns.duplicated()] #Aynı olan columnsları siliyor.

Output3 = pd.merge(Defensive2010_2011.reset_index(drop=True), Summary2010_2011.reset_index(drop=True), how='outer', left_on='Player', right_on='Player')

#%%##############
"""Splitting based on paranthesis"""
creatingAppsS2 = Output3.Apps.str.split("(", expand=True)

"""Adding to integers that split based on paranthesis, on Output3"""
Output3['Apps'] = Output3.Apps.str.split("(", expand=True)[0]

"""Splitting based on second paranthesis"""
Output3['AppsS'] = creatingAppsS2[1].str.split(")", expand=True)[0]

"""Splitting the double space"""
aaa1 = Output3.Player.str.split("\n\n", expand=True)

"""Adding Player names which clean age and teams"""
Output3['Player'] = aaa1[0] 

"""Splitting comma """
aaa1 = aaa1[1].str.split(", ",expand=True)

"""Adding Team"""
Output3['Team'] = aaa1[0]

"""Adding Age"""
Output3['Age'] = aaa1[1]

"""Adding Position"""
Output3['Position'] = aaa1[2]

"""Replacing - to zero"""
Output3 = Output3.replace({'-': 0})
#%%###############    Combining two outputs (last merge) ##################

LastOutput = pd.merge(Output2, Output3, how='outer', left_on='Player', right_on='Player')

"""If it has another integers, but contains nan or None, converting to zero."""
LastOutput = LastOutput.replace(np.nan, 0)
LastOutput = LastOutput.drop_duplicates()

"""Exporting Excel"""
LastOutput.to_csv('DS501ProjectNewData.csv', index = True)


########################################################################
########################################################################

                                #PART 2
                                
########################################################################
########################################################################

LastOutput = pd.read_csv('DS501ProjectNewData.csv')
LastOutput = LastOutput.reset_index(drop=True)
LastOutput = LastOutput.drop('Unnamed: 0', axis = 1)

#%%###### Part A ########
"""Dropping rows of players did not transfer in two seasons from the data"""
df1 = LastOutput.drop(LastOutput[LastOutput['Team_x'] == LastOutput['Team_y']].index)
"""Sorting"""
df1 = df1.sort_values(['Rating_y'], ascending=[False])
print(df1.head(5))
#%%###### Part B #########
"""Dropping rows of the players who did not take minutes in 2009-2010 season."""
df_new = LastOutput.drop(LastOutput[LastOutput['Mins_x'] == 0].index)

df2 = df_new.filter(['Player'], axis=1)

"""Substracting the rating of 2010-11 to the rating of 2009-2010"""
df2['Difference'] = df_new['Rating_y'].subtract(df_new['Rating_x'])

"""Sorting"""
df2 = df2.sort_values(['Difference'], ascending = False)
print(df2.head(5))
#%%###### Part C #########
"""Reverse Sorting"""
df2 = df2.sort_values(['Difference'], ascending = True)
print(df2.head(5))
#%%###### Part D #########

df_thebestteamofseason = LastOutput.filter(['Player'], axis=1)
df_thebestteamofseason['Rating_x'] = LastOutput.filter(['Rating_x'], axis=1)
df_thebestteamofseason['Rating_y'] = LastOutput.filter(['Rating_y'], axis=1)
df_thebestteamofseason['Position_x'] = LastOutput.filter(['Position_x'], axis=1)
df_thebestteamofseason['Position_y'] = LastOutput.filter(['Position_y'], axis=1)

"""Sorting rating for 2009-2010 Season"""
df_thebestteamofseason = df_thebestteamofseason.sort_values(['Rating_x'], ascending = False)
df_thebestteamofseason = df_thebestteamofseason.reset_index(drop=True)

"""Copy paste dataframe for 2009-2010"""
firstteam = df_thebestteamofseason.copy()
secondteam = df_thebestteamofseason.copy()

"""Resetting indexes"""
firstteam = firstteam.reset_index(drop=True)
secondteam = secondteam.reset_index(drop=True)
    
#%% 2009-2010 Season (4-4-2)
"""Dropping multiple player names"""
firstteam = firstteam.drop_duplicates(subset=['Player'], keep='first')

#4-4-2 for Forward 
searchfor = ['F', 'FW', 'Forward']
"""Searching Position_x based on searchfor"""
firstteamnew = firstteam[firstteam['Position_x'].str.contains('|'.join(searchfor))].head(2)

"""Dropping the list of 11 selected from the data."""
firstteam = firstteam.drop(firstteamnew.index)

#4-4-2 for Defense
searchfor = ['D', 'D(C)', 'Defense', 'DMC', 'D(L)', 'D(CR)', 'D(R)', 'D(LR)', 'D(CLR)', 'D(CL)']
"""Appending the list of 11 and Searching on Position_x"""
firstteamnew = firstteamnew.append(firstteam[firstteam['Position_x'].str.contains('|'.join(searchfor))].head(4))

"""Finding indexes of new players"""
firstteamindex = firstteam[firstteam['Position_x'].str.contains('|'.join(searchfor))].index

"""Dropping new players for the list of 11"""
firstteam = firstteam.drop(firstteamindex[0:4])

#4-4-2 for Midfielder
searchfor = ['M', 'Midfielder', 'AM', 'M(R)', 'M(L)', 'M(C)', 'DMC', 'M(CLR)', 'M(CL)']
"""Appending the list of 11 and Searching on Position_x"""
firstteamnew = firstteamnew.append(firstteam[firstteam['Position_x'].str.contains('|'.join(searchfor))].head(4))

#4-4-2 for Goalkeeper
searchfor = ['GK', 'Goalkeeper']
"""Appending the list of 11 and Searching on Position_x"""
firstteamnew = firstteamnew.append(firstteam[firstteam['Position_x'].str.contains('|'.join(searchfor))].head(1))

print(firstteamnew[['Player', 'Position_x']])

#%% 2009-2010 Season (3-5-2)
"""Dropping multiple player names"""
secondteam = secondteam.drop_duplicates(subset=['Player'], keep='first')

#3-5-2 for Forward
searchfor = ['F', 'FW', 'Forward']
"""Searching Position_x based on searchfor"""
secondteamnew = secondteam[secondteam['Position_x'].str.contains('|'.join(searchfor))].head(2)

"""Dropping the list of 11 selected from the data."""
secondteam = secondteam.drop(secondteamnew.index)

#3-5-2  for Defense
searchfor = ['D', 'D(C)', 'Defense', 'DMC', 'D(L)', 'D(CR)', 'D(R)', 'D(LR)', 'D(CLR)', 'D(CL)']
"""Appending the list of 11 and Searching on Position_x"""
secondteamnew = secondteamnew.append(secondteam[secondteam['Position_x'].str.contains('|'.join(searchfor))].head(3))

"""Finding indexes of new players"""
secondteamindex = secondteam[secondteam['Position_x'].str.contains('|'.join(searchfor))].index

"""Dropping new players for the list of 11"""
secondteam = secondteam.drop(secondteamindex[0:3])

#3-5-2  for Midfielder
searchfor = ['M', 'Midfielder', 'AM', 'M(R)', 'M(L)', 'M(C)', 'DMC', 'M(CLR)', 'M(CL)']
"""Appending the list of 11 and Searching on Position_x"""
secondteamnew = secondteamnew.append(secondteam[secondteam['Position_x'].str.contains('|'.join(searchfor))].head(5))

#3-5-2  for Midfielder
searchfor = ['GK', 'Goalkeeper']
secondteamnew = secondteamnew.append(secondteam[secondteam['Position_x'].str.contains('|'.join(searchfor))].head(1))

print(secondteamnew[['Player', 'Position_x']])

#%% 2010-2011 Season 

"""Sorting rating for 2010-2011 Season"""
df_thebestteamofseason = df_thebestteamofseason.sort_values(['Rating_y'], ascending = False)
df_thebestteamofseason = df_thebestteamofseason.reset_index(drop=True)

"""Copy paste dataframe for 2010-2011"""
thirdteam = df_thebestteamofseason.copy()
fourthteam = df_thebestteamofseason.copy()

"""Resetting indexes"""
thirdteam = thirdteam.reset_index(drop=True)
fourthteam = fourthteam.reset_index(drop=True)

#%% 2010-2011 Season (4-4-2)
"""Dropping multiple player names"""
thirdteam = thirdteam.drop_duplicates(subset=['Player'], keep='first')

#4-4-2 for Forward
searchfor = ['F', 'FW', 'Forward']
"""Searching Position_y based on searchfor"""
thirdteamnew = thirdteam[thirdteam['Position_y'].str.contains('|'.join(searchfor))].head(2)

"""Dropping the list of 11 selected from the data."""
thirdteam = thirdteam.drop(thirdteamnew.index)

#4-4-2 for Defense
searchfor = ['D', 'D(C)', 'Defense', 'DMC', 'D(L)', 'D(CR)', 'D(R)', 'D(LR)', 'D(CLR)', 'D(CL)']
"""Appending the list of 11 and Searching on Position_y"""
thirdteamnew = thirdteamnew.append(thirdteam[thirdteam['Position_y'].str.contains('|'.join(searchfor))].head(4))

"""Finding indexes of new players"""
thirdteamindex = thirdteam[thirdteam['Position_y'].str.contains('|'.join(searchfor))].index

"""Dropping new players for the list of 11"""
thirdteam = thirdteam.drop(thirdteamindex[0:4])

#4-4-2 for Midfielder
searchfor = ['M', 'Midfielder', 'AM', 'M(R)', 'M(L)', 'M(C)', 'DMC', 'M(CLR)', 'M(CL)']
"""Appending the list of 11 and Searching on Position_y"""
thirdteamnew = thirdteamnew.append(thirdteam[thirdteam['Position_y'].str.contains('|'.join(searchfor))].head(4))

#4-4-2 for Goalkeeper
searchfor = ['GK', 'Goalkeeper']
thirdteamnew = thirdteamnew.append(thirdteam[thirdteam['Position_y'].str.contains('|'.join(searchfor))].head(1))

print(thirdteamnew[['Player', 'Position_y']])

#%% 2010-2011 Season (3-5-2)
"""Dropping multiple player names"""
fourthteam = fourthteam.drop_duplicates(subset=['Player'], keep='first')

#3-5-2 for Forward
searchfor = ['F', 'FW', 'Forward']
"""Searching Position_y based on searchfor"""
fourthteamnew = fourthteam[fourthteam['Position_y'].str.contains('|'.join(searchfor))].head(2)

"""Dropping the list of 11 selected from the data."""
fourthteam = fourthteam.drop(fourthteamnew.index)

#3-5-2  for Defense
searchfor = ['D', 'D(C)', 'Defense', 'DMC', 'D(L)', 'D(CR)', 'D(R)', 'D(LR)', 'D(CLR)', 'D(CL)']
"""Appending the list of 11 and Searching on Position_y"""
fourthteamnew = fourthteamnew.append(fourthteam[fourthteam['Position_y'].str.contains('|'.join(searchfor))].head(3))

"""Finding indexes of new players"""
fourthteamindex = fourthteam[fourthteam['Position_y'].str.contains('|'.join(searchfor))].index

"""Dropping new players for the list of 11"""
fourthteam = fourthteam.drop(fourthteamindex[0:3])

#3-5-2  for Midfielder
searchfor = ['M', 'Midfielder', 'AM', 'M(R)', 'M(L)', 'M(C)', 'DMC', 'M(CLR)', 'M(CL)']
"""Appending the list of 11 and Searching on Position_y"""
fourthteamnew = fourthteamnew.append(fourthteam[fourthteam['Position_y'].str.contains('|'.join(searchfor))].head(5))

searchfor = ['GK', 'Goalkeeper']
fourthteamnew = fourthteamnew.append(fourthteam[fourthteam['Position_y'].str.contains('|'.join(searchfor))].head(1))

print(fourthteamnew[['Player', 'Position_y']])

#%%###### Part E #########
"""Appending four different teams"""
Thebestplayer = firstteamnew.append(secondteamnew)
Thebestplayer = secondteamnew.append(thirdteamnew)
Thebestplayer = Thebestplayer.append(fourthteamnew)

"""Dropping the rest of the same players"""
Thebestplayer = Thebestplayer.drop_duplicates()

"""Sorting for the best player for 2009-2010"""
Thebestplayer = Thebestplayer.sort_values(['Rating_x'], ascending = False)
LastThebestplayer = Thebestplayer.head(1)

"""Sorting for the best player for 2010-2011"""
Thebestplayer = Thebestplayer.sort_values(['Rating_y'], ascending = False)

LastThebestplayer = LastThebestplayer.append(Thebestplayer.head(1))
print(LastThebestplayer[['Player']].head(2))

"""Average of the ranking between 2009-2010 and 2010-2011"""
LastThebestplayer['Average'] = LastThebestplayer.mean(axis=1)
LastThebestplayer = LastThebestplayer.sort_values(['Average'], ascending = False).head(1)

"""The best player"""
print(LastThebestplayer[['Player', 'Average']])








# ########################################################################
# ########################################################################

# """ANOTHER PART D"""
                                
# ########################################################################
# ########################################################################
# # 3 - 5 - 2 ###2009-2010
# firstteam = []
# position = 'F'
# iteration1=0
# while True:
#     if (df_thebestteamofseason['Position_x'].iloc[iteration1].find(position) > -1):
#         player1 = df_thebestteamofseason['Player'].iloc[iteration1]
#         if (player1 not in firstteam): 
#             firstteam.append(df_thebestteamofseason['Player'].iloc[iteration1])
#             iteration1+=1
#             if (len(firstteam) == 2):
#                 position= 'D'
#                 iteration1 = 0
#             if (len(firstteam) == 5):
#                 position= 'M'
#                 iteration1 = 0
#             if (len(firstteam) == 10):
#                 position= 'G'
#                 iteration1 = 0
#             if (len(firstteam) == 11):
#                 break
#         else:
#              iteration1+=1
#     else:
#         iteration1+=1
# print("3 - 5 - 2 (2009-2010)", firstteam)

# # 4 - 4 - 2 ###2009-2010
# secondteam = []
# position = 'F'
# iteration1=0
# while True:
#     if (df_thebestteamofseason['Position_x'].iloc[iteration1].find(position) > -1):
#         player1 = df_thebestteamofseason['Player'].iloc[iteration1]
#         if (player1 not in secondteam): 
#             secondteam.append(df_thebestteamofseason['Player'].iloc[iteration1])
#             iteration1+=1
#             if (len(secondteam) == 2):
#                 position = 'D'
#                 iteration1 = 0
#             if (len(secondteam) == 6):
#                 position = 'M'
#                 iteration1 = 0
#             if (len(secondteam) == 10):
#                 position = 'G'
#                 iteration1 = 0
#             if (len(secondteam) == 11):
#                 break
#         else:
#              iteration1+=1
#     else:
#         iteration1+=1
# print("4 - 4 - 2 (2009-2010)", secondteam)


# df_thebestteamofseason = df_thebestteamofseason.sort_values(['Rating_y'], ascending = False) #for 2009-2010 Season
# df_thebestteamofseason = df_thebestteamofseason.reset_index(drop=True)

# 3 - 5 - 2 ###2010-2011
# thirdteam = []
# thirdteamrating = []
# position = 'F'
# iteration1=0
# while True:
#     if (df_thebestteamofseason['Position_y'].iloc[iteration1].find(position) > -1):
#         player1 = df_thebestteamofseason['Player'].iloc[iteration1]
#         if (player1 not in thirdteam): 
#             thirdteam.append(df_thebestteamofseason['Player'].iloc[iteration1])
#             thirdteamrating.append(df_thebestteamofseason['Rating_y'].iloc[iteration1])
#             iteration1+=1
#             if (len(thirdteam) == 2):
#                 position= 'D'
#                 iteration1 = 0
#             if (len(thirdteam) == 5):
#                 position= 'M'
#                 iteration1 = 0
#             if (len(thirdteam) == 10):
#                 position= 'G'
#                 iteration1 = 0
#             if (len(thirdteam) == 11):
#                 break
#         else:
#               iteration1+=1
#     else:
#         iteration1+=1
# print("3 - 5 - 2 (2010-2011)", thirdteam)

# 4 - 4 - 2 ###2010-2011
fourthteam = []
position = 'F'
iteration1=0
while True:
    if (df_thebestteamofseason['Position_y'].iloc[iteration1].find(position) > -1):
        player1 = df_thebestteamofseason['Player'].iloc[iteration1]
        if (player1 not in fourthteam): 
            fourthteam.append(df_thebestteamofseason['Player'].iloc[iteration1])
            iteration1+=1
            if (len(fourthteam) == 2):
                position= 'D'
                iteration1 = 0
            if (len(fourthteam) == 6):
                position= 'M'
                iteration1 = 0
            if (len(fourthteam) == 10):
                position= 'G'
                iteration1 = 0
            if (len(fourthteam) == 11):
                break
        else:
              iteration1+=1
    else:
        iteration1+=1
print("4 - 4 - 2 (2010-2011)", fourthteam)


















