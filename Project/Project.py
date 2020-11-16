# importing pandas, numpy, matplotlib and seaborn library.
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

##############################################################################################################

#   QUESTION-1
#   Read the data set.

# reading the dataset.
data = pd.read_csv("C:\\Users\\Hp\\PycharmProjects\\pubg.csv")
print("\n", data)

##############################################################################################################

#   QUESTION-2
#   Check the datatype of all the columns.

# checking the datatype of all columns.
datatype = data.dtypes
# printing the datatype of columns.
print("\n", datatype)

###############################################################################################################

#   QUESTION-3
#   Find the summary of all the numerical columns and write your findings about it.

# getting summary of all the numerical columns describe() function.
data_summary = data.describe()
print("\n", data_summary)

################################################################################################################

#   QUESTION-4
#   The average person kills how many players?

# getting average kills of a person.
avg_kills = data['kills'].mean()
# printing average kills.
print("\n On an average the person kills :", avg_kills, "players")

#################################################################################################################

#   QUESTION-5
#   99% of people have how many kills?

# getting kills of 99% people.
nn_per_kills = np.percentile(data.kills, 99)
# printing kills of 99% people.
print("\n 99% of people have", nn_per_kills, "kills")

#################################################################################################################

#   QUESTION-6
#   The most kills ever recorded are how much?

#
most_kill = data["kills"].max()
#
print("\n The most kill ever recorded are :", most_kill)

###############################################################################################################

#   QUESTION-7
#   Print all the columns of the dataframe.

# getting all the columns.
all_cols = data.columns
# printing all the columns.
print("\n", all_cols)

##############################################################################################################

#   QUESTION=8
#   Comment on distribution of the match's duration. Use seaborn.

# plotting the data.
sb.displot(data['matchDuration'])
# displaying the chart.
plt.show()
# printing the comments on the chart.
print("\n The match duration is mostly high during", 1250, "to", 1500, "and", 1750, "to", 2000)

############################################################################################################

#   QUESTION-9
#   Comment on distribution of the walk distance. Use seaborn.

# plotting the walkdistance data.
sb.displot(data['walkDistance'])
# displaying the chart.
plt.show()
# printing the comments on the chart.
print("\n Mostly the walk distance lies between 0 to 3000")

############################################################################################################

#   QUESTION-10
#   Plot distribution of the match's duration vs walk distance one below the other.

# plotting match's duration vs walk distance one below the other.
fig, axs = plt.subplots(2, 1)
sb.histplot(data.matchDuration, ax=axs[0])
sb.histplot(data.walkDistance, ax=axs[1])
# displaying the plot.
plt.show()

############################################################################################################

#   QUESTION-11
#   Plot distribution of the match's duration vs walk distance side by side.

# plotting the match's duration vs walk distance side by side.
fig, axs = plt.subplots(1, 2)
sb.histplot(data.matchDuration, ax=axs[0])
sb.histplot(data.walkDistance, ax=axs[1])
# displaying the plot.
plt.show()

#############################################################################################################

#   QUESTION-12
#   Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups.

# plotting the dataframe.

# displaying the plot.

# printing the comments on kills vs damage dealt.
print("\n The relation between kills vs damage dealt is directly proportional")
# printing the comments on maxPlace vs numGroups.
print("\n The relation between maxplace vs numGroups is linear")

#############################################################################################################

#   QUESTION-13
#   How many unique values are there in 'matchType' and what are their counts?

# getting unique values and it's count.
unique = data.matchType.value_counts()
# printing unique value and it's count.
print("\n", unique)

##############################################################################################################

#   QUESTION-14
#   Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences.

# getting barplot of matchtype and killPoints.
sb.barplot(data.matchType, data.killPoints)
# rotating the bar name for proper visibility.
plt.xticks(rotation=85)
# displaying the bar plot
plt.show()
#############################################################################################################

#   QUESTION-15
#   Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences.

# plotting a barplot of matchType and weaponsAcquired.
sb.barplot(data.matchType, data.weaponsAcquired)
# rotating the bar name for proper visibility.
plt.xticks(rotation=85)
# displaying the barplot.
plt.show()

#############################################################################################################

#   QUESTION-16
#   Find the Categorical columns.

# getting the categorical columns.
cat_col = data.select_dtypes(exclude=['number'])
# printing the cat_col.
print("\n", cat_col)

#############################################################################################################

#   QUESTION-17
#   Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’. Write your inferences.

# plotting a boxplot of matchType and winPlacePerc.
sb.boxplot(data.matchType, data.winPlacePerc)
# rotating the box name for proper visibility.
plt.xticks(rotation=85)
# displaying the boxplot.
plt.show()
#############################################################################################################

#   QUESTION-18
#   Plot a boxplot of ‘matchType’ vs ‘matchDuration’. Write your inferences.

# plotting a boxplot of matchType and matchDuration.
sb.boxplot(data.matchType, data.matchDuration)
# rotating the box name for proper visibility.
plt.xticks(rotation=85)
# displaying the boxplot.
plt.show()

#############################################################################################################

#   QUESTION-19
#   Change the orientation of the above plot to horizontal.

# changing the orientation to horizontal.
sb.boxplot(data.matchDuration, data.matchType)
# rotating the box name for proper visibility.
plt.xticks(rotation=85)
# displaying the boxplot
plt.show()

#############################################################################################################

#   QUESTION-20
#   Add a new column called ‘KILL’ which contains the sum of following columns viz. headshot Kills,teamKills, roadKills.

# adding a new column.
data['KILL'] = data['headshotKills'] + data['teamKills'] + data['roadKills']
# printing the 'KILL' column.
print("\n", data['KILL'])

#############################################################################################################

#   QUESTION-21
#   Round off column ‘winPlacePerc’ to 2 decimals.

# rounding off the 'winPlacePerc' column.
data['winPlacePerc'].round(decimals=2)
# printing the 'winPlacePerc' column.
print("\n", data['winPlacePerc'])

#############################################################################################################

#   QUESTION-22
#   Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot it on a histogram and comment on its distribution.

# Taking a sample of size 50 from the column damageDealt for 100 times.
x = []
for i in range(100):
    x.append(data['damageDealt'].sample(50).mean())
# converting list x into array.
mean = np.array(x)
# plotting the mean.
sb.histplot(mean)
# displaying the plot.
plt.show()
# commenting on the damageDefault's mean.
print("Usually the damage default is high from 82 to 175")



#######################################  THE END  #######################################################