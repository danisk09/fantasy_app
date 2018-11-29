import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import requests

scores = {}
for week in range(1,17):
	r = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', params={'leagueId': 854805, 'seasonId': 2018, 'matchupPeriodId': week})
	scores[week] = r.json()

df = []
for key in scores:
	temp = scores[key]['scoreboard']['matchups']
	for match in temp:
		df.append([key,
				   match['teams'][0]['team']['teamAbbrev'],
				   match['teams'][1]['team']['teamAbbrev'],
				   match['teams'][0]['score'],
				   match['teams'][1]['score']])

df = pd.DataFrame(df, columns=['Week', 'HomeAbbrev', 'AwayAbbrev', 'HomeScore', 'AwayScore'])
df.head()
