import pandas as pd
import numpy as np

class prediction_football:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def get_winner(self):
        winner = ''
        df = pd.read_csv('premier_csv.csv')

        # 20개 팀 리스트
        team_list = ['리버풀', '맨시티', '맨유', '첼시', '레스터', '토트넘', '울버햄튼',
                     '아스널', '셰필드', '번리', '샤우샘프턴', '에버턴', '뉴캐슬',
                     '브라이튼', '팰리스', '웨스트햄', '아스톤 빌라', '본머스', '왓포드', '노리치']

        print(self.team1, self.team2)
        # team1과 경기 기록
        self.team1_df = pd.DataFrame(df.loc[df['team_1'] == self.team1])
        self.team1_df = self.team1_df.append(df.loc[df['team_2'] == self.team1])

        self.team1_df.index = [i for i in range(len(self.team1_df))]
        print(self.team1+'경기기록')
        print(self.team1_df)


        # team2과 경기 기록
        self.team2_df = pd.DataFrame(df.loc[df['team_1'] == self.team2])
        self.team2_df = self.team2_df.append(df.loc[df['team_2'] == self.team2])

        self.team2_df.index = [i for i in range(len(self.team2_df))]
        print(self.team2 + ' 경기기록')
        print(self.team2_df)

        
        team1_win, team2_win = self.countWin()
        team1_goal, team2_goal = self.countGoal()
        team1_mean, team2_mean = self.meanGoal()

        team1_total, team2_total = 0, 0
        func = lambda x, y, z : x + y + z
        team1_total += func(team1_win, team1_goal, team1_mean)
        team2_total += func(team2_win, team2_goal, team2_mean)

        if team1_total > team2_total:
            winner = self.team1
        else:
            winner = self.team2


        result1 = df.loc[df['team_1'] == self.team1][df['team_2'] == self.team2]
        result2 = df.loc[df['team_1'] == self.team2][df['team_2'] == self.team1]
        print(result1)
        print(result2)

        return winner

    # 이긴 경기 수 카운트
    def countWin(self):
        # team1이 이긴 경기 기록들
        team1_win = self.team1_df.loc[self.team1_df['score_1'] > self.team1_df['score_2']][self.team1_df['team_1'] == self.team1]
        team1_win = team1_win.append(self.team1_df.loc[self.team1_df['score_1'] < self.team1_df['score_2']][self.team1_df['team_2'] == self.team1])
        #print(team1_win)

        # team2가 이긴 경기 기록들
        team2_win = self.team2_df.loc[self.team2_df['score_1'] > self.team2_df['score_2']][self.team2_df['team_1'] == self.team2]
        team2_win = team2_win.append(self.team2_df.loc[self.team2_df['score_1'] < self.team2_df['score_2']][self.team2_df['team_2'] == self.team2])
        #print(team2_win)

        return len(team1_win), len(team2_win)


    # 골 카운트
    def countGoal(self):
        team1_goal, team2_goal = 0, 0
        print('countGoal')
        team1_1 = pd.DataFrame(self.team1_df.loc[self.team1_df['team_1'] == self.team1])
        team1_2 = pd.DataFrame(self.team1_df.loc[self.team1_df['team_2'] == self.team1])
        team1_goal += sum(team1_1['score_1'])
        team1_goal += sum(team1_2['score_2'])

        team2_1 = pd.DataFrame(self.team2_df.loc[self.team2_df['team_1'] == self.team2])
        team2_2 = pd.DataFrame(self.team2_df.loc[self.team2_df['team_2'] == self.team2])
        team2_goal += sum(team2_1['score_1'])
        team2_goal += sum(team2_2['score_2'])

        return team1_goal, team2_goal

    # 넣은 골 수 평균
    def meanGoal(self):
        team1_mean, team2_mean = 0, 0
        team1_1 = pd.DataFrame(self.team1_df.loc[self.team1_df['team_1'] == self.team1])
        team1_2 = pd.DataFrame(self.team1_df.loc[self.team1_df['team_2'] == self.team1])
        team1_1mean = (team1_1.describe().loc[['mean']]).loc['mean', 'score_1']
        team1_2mean = (team1_2.describe().loc[['mean']]).loc['mean', 'score_2']
        team1_mean = np.mean([team1_1mean, team1_2mean])

        team2_1 = pd.DataFrame(self.team2_df.loc[self.team2_df['team_1'] == self.team2])
        team2_2 = pd.DataFrame(self.team2_df.loc[self.team2_df['team_2'] == self.team2])
        team2_1mean = (team2_1.describe().loc[['mean']]).loc['mean', 'score_1']
        team2_2mean = (team2_2.describe().loc[['mean']]).loc['mean', 'score_2']
        team2_mean = np.mean([team2_1mean, team2_2mean])

        return team1_mean, team2_mean


if __name__ == '__main__':
    ex = prediction_football()



