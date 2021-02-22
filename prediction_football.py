import pandas as pd

df = pd.read_csv('premier_csv.csv')

team1 = input('첫 번쨰 팀 : ')
team2 = input('두 번째 팀 : ')

# team1과 경기만 경력들

# print(df.loc[df['team_1'] == team1])
# print(df.loc[df['team_2'] == team1])

team1_df = pd.DataFrame(df.loc[df['team_1'] == team1])
team1_df = team1_df.append(df.loc[df['team_2'] == team1])

team1_df.index = [i for i in range(len(team1_df))]
print(team1_df)


team2_df = pd.DataFrame(df.loc[df['team_1'] == team2])
team2_df = team2_df.append(df.loc[df['team_2'] == team2])

team2_df.index = [i for i in range(len(team2_df))]
print(team2_df)


team1_win = team1_df.loc[team1_df['score_1'] > team1_df['score_2']][team1_df['team_1'] == team1]
team1_win = team1_win.append(team1_df.loc[team1_df['score_1'] < team1_df['score_2']][team1_df['team_2'] == team1])
print(team1_win)


team2_win = team2_df.loc[team2_df['score_1'] > team2_df['score_2']][team2_df['team_1'] == team2]
team2_win = team2_win.append(team2_df.loc[team2_df['score_1'] < team2_df['score_2']][team2_df['team_2'] == team2])
print(team2_win)


if len(team1_win) > len(team2_win):
    print(team1)
elif len(team1_win) < len(team2_win):
    print(team2)

result1 = df.loc[df['team_1'] == team1][df['team_2'] == team2]
result2 = df.loc[df['team_1'] == team2][df['team_2'] == team1]
