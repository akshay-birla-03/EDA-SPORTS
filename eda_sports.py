# -*- coding: utf-8 -*-
"""EDA-SPORTS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1apf1uGk_cIeP0QMVuyMqjjt7EfucP91d
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("/content/matches.csv")

data.head()

Data = pd.read_csv("deliveries.csv")

Data.head()

season_data=data[['id','season','winner']]

complete_data=Data.merge(season_data,how='inner',left_on='match_id',right_on='id')

data.columns.values

data = data.drop(columns=["umpire3"],axis=1)

data.head()

wins_per_season = data.groupby("season")["winner"].value_counts()
wins_per_season

plt.figure(figsize = (18,10))
sns.countplot(x='season', data=data, palette="summer")  # Specify 'season' as the x-axis variable
plt.title("Number of Matches played in each IPL season",fontsize=10)
plt.xlabel("season",fontsize=7)
plt.ylabel('Matches',fontsize=7)
plt.show()

plt.figure(figsize = (18,10))
sns.countplot(x='winner',data=data, palette='RdBu')
plt.title("Numbers of matches won by team ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("Teams",fontsize=15)
plt.ylabel("No of wins",fontsize=15)
plt.show()

data['win_by']=np.where(data['win_by_runs']>0,'Bat first','Bowl first')

Win=data.win_by.value_counts()
labels=np.array(Win.index)
sizes = Win.values
colors = ['#0077be', '#00b7eb']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Match Result',fontsize=20)
plt.axis('equal')  # Remove the invalid 'fontsize' argument

# Set font size for axis labels separately
plt.xlabel('X-axis label', fontsize=10)  # Adjust fontsize as needed
plt.ylabel('Y-axis label', fontsize=10)  # Adjust fontsize as needed

plt.show()

plt.figure(figsize = (18,10))
sns.countplot(x='season', hue='win_by', data=data, palette='viridis')  # Changed palette to 'viridis'
plt.title("Numbers of matches won by batting and bowling first ",fontsize=20)
plt.xlabel("Season",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.xticks(rotation=90)
plt.show()

# we will plot pie chart on Toss decision
Toss=data.toss_decision.value_counts()
labels=np.array(Toss.index)
sizes = Toss.values
colors = ['#228B22', '#3CB371']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Toss result',fontsize=20)
plt.axis('equal') # Remove the invalid fontsize argument. Use xlabel and ylabel to set font size for axis labels

# Set font size for axis labels separately
plt.xlabel('X-axis label', fontsize=10)  # Adjust fontsize as needed
plt.ylabel('Y-axis label', fontsize=10)  # Adjust fontsize as needed

plt.show()

# we will plot graph on Numbers of matches won by Toss result
plt.figure(figsize = (18,10))
sns.countplot(x='season', hue='toss_decision', data=data, palette='afmhot')  # Use 'data' instead of 'df'
plt.title("Numbers of matches won by Toss result ",fontsize=20)
plt.xlabel("Season",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.show()

# we will print winner season wise
final_matches=data.drop_duplicates(subset=['season'], keep='last')

final_matches[['season','winner']].reset_index(drop=True).sort_values('season')

# we will plot pie chart on Winning percentage in final
match = final_matches.win_by.value_counts()
labels=np.array(match.index) # Use match index for labels
sizes = match.values
colors = ['#E0FFFF', '#AFEEEE']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Match Result',fontsize=20)
plt.axis('equal')

# Set font size for axis labels
plt.xlabel('Win By', fontsize=12)  # Adjust fontsize as needed
plt.ylabel('Winning Percentage', fontsize=12)  # Adjust fontsize as needed

plt.show()

Toss=final_matches.toss_decision.value_counts()
labels=np.array(Toss.index)
sizes = Toss.values
colors = ['#FFBF00', '#FA8072']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Toss Result',fontsize=20)
plt.axis('equal') # Keep this to set the aspect ratio
# Set font size for axis labels separately
plt.xlabel('X-axis label', fontsize=10)  # Adjust fontsize as needed
plt.ylabel('Y-axis label', fontsize=10)  # Adjust fontsize as needed
plt.show()

# we will print name of top player in IPL
plt.figure(figsize = (18,10))
top_players = data.player_of_match.value_counts()[:10]
fig, ax = plt.subplots()
ax.set_ylim([0,20])
ax.set_ylabel("Count")
ax.set_title("Top player of the match Winners")
top_players.plot.bar()
sns.barplot(x = top_players.index, y = top_players, orient='v', palette="rocket");
plt.show()

# We will print IPL Finals venues and winners along with the number of wins.
final_matches.groupby(['city','winner']).size()

# we will print number of season won by teams
final_matches["winner"].value_counts()

# we will print toss winner, toss decision, winner in final matches.
final_matches[['toss_winner','toss_decision','winner']].reset_index(drop=True)

# we will print man of the match
final_matches[['winner','player_of_match']].reset_index(drop=True)

len(final_matches[final_matches['toss_winner']==final_matches['winner']]['winner'])

# we will print numbers of fours hit by team
four_data=complete_data[complete_data['batsman_runs']==4]
four_data.groupby('batting_team')['batsman_runs'].agg([('runs by fours','sum'),('fours','count')])

# we will plot graph on four hit by players
batsman_four=four_data.groupby('batsman')['batsman_runs'].agg([('four','count')]).reset_index().sort_values('four',ascending=0)
ax=batsman_four.iloc[:10,:].plot('batsman','four',kind='bar',color='purple')
plt.title("Numbers of fours hit by playes ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("Player name",fontsize=15)
plt.ylabel("No of fours",fontsize=15)
plt.show()

# we will plot graph on no of four hit in each season
ax=four_data.groupby('season')['batsman_runs'].agg([('four','count')]).reset_index().plot('season','four',kind='bar',color = 'green')
plt.title("Numbers of fours hit in each season ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("season",fontsize=15)
plt.ylabel("No of fours",fontsize=15)
plt.show()

# we will print no of sixes hit by team
six_data=complete_data[complete_data['batsman_runs']==6]
six_data.groupby('batting_team')['batsman_runs'].agg([('runs by six','sum'),('sixes','count')])

# we will plot graph of six hit by players
batsman_six=six_data.groupby('batsman')['batsman_runs'].agg([('six','count')]).reset_index().sort_values('six',ascending=0)
ax=batsman_six.iloc[:10,:].plot('batsman','six',kind='bar',color='Black')
plt.title("Numbers of six hit by playes ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("Player name",fontsize=15)
plt.ylabel("No of six",fontsize=15)
plt.show()

# we will plot graph on no of six hit in each season
ax=six_data.groupby('season')['batsman_runs'].agg([('six','count')]).reset_index().plot('season','six',kind='bar',color = 'blue')
plt.title("Numbers of fours hit in each season ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("season",fontsize=15)
plt.ylabel("No of fours",fontsize=15)
plt.show()

# We will print the top 10 leading run scorer in IPL
batsman_score=Data.groupby('batsman')['batsman_runs'].agg(['sum']).reset_index().sort_values('sum',ascending=False).reset_index(drop=True)
batsman_score=batsman_score.rename(columns={'sum':'batsman_runs'})
print("*** Top 10 Leading Run Scorer in IPL ***")
batsman_score.iloc[:10,:]

# we will print no of matches played by batsman
No_Matches_player= Data[["match_id","player_dismissed"]]
No_Matches_player =No_Matches_player .groupby("player_dismissed")["match_id"].count().reset_index().sort_values(by="match_id",ascending=False).reset_index(drop=True)
No_Matches_player.columns=["batsman","No_of Matches"]
No_Matches_player .head(5)

# Dismissals in IPL
plt.figure(figsize=(18,10))
ax=sns.countplot(Data.dismissal_kind)
plt.title("Dismissals in IPL",fontsize=20)
plt.xlabel("Dismissals kind",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.xticks(rotation=90)
plt.show()

wicket_data=Data.dropna(subset=['dismissal_kind'])
wicket_data=wicket_data[~wicket_data['dismissal_kind'].isin(['run out','retired hurt','obstructing the field'])]

#The highest number of match played in IPL season was 2013,2014,2015.

#The highest number of match won by Mumbai Indians i.e 4 match out of 12 matches.

#Teams which Bowl first has higher chances of winning then the team which bat first.

#After winning toss more teams decide to do fielding first.

#In finals teams which decide to do fielding first win the matches more then the team which bat first.

#In finals most teams after winning toss decide to do fielding first.

#Top player of match winning are CH gayle, AB de villers.

#It is interesting that out of 12 IPL finals,9 times the team that won the toss was also the winner of IPL.

#The highest number of four hit by player is Shikar Dhawan.

#The highest number of six hit by player is CH gayle.

#Top leading run scorer in IPL are Virat kholi, SK Raina, RG Sharma.

#The highest number of matches played by player name are SK Raina, RG Sharma.

#Dismissals in IPL was most by Catch out .

#The IPL most wicket taken blower is SL Malinga.