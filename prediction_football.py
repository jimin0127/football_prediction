import pandas as pd

class prediction_football:

    def __init__(self):
        df = pd.read_csv('premier_csv.csv')

        # 20개 팀 리스트
        team_list = ['리버풀', '맨시티', '맨유', '첼시', '레스터', '토트넘', '울버햄튼',
                     '아스널', '셰필드', '번리', '샤우샘프턴', '에버턴', '뉴캐슬',
                     '브라이튼', '팰리스', '웨스트햄', '아스톤 빌라', '본머스', '왓포드', '노리치']

        # team1 = input('첫 번쨰 팀 : ')
        # team2 = input('두 번째 팀 : ')

        true, false = 0, 0

        for team1 in team_list:
            for team2 in team_list:
                if team1 == team2:
                    continue
                print(team1, team2)
                # team1과 경기 기록
                team1_df = pd.DataFrame(df.loc[df['team_1'] == team1])
                team1_df = team1_df.append(df.loc[df['team_2'] == team1])

                team1_df.index = [i for i in range(len(team1_df))]
                print(team1+'경기기록')
                #print(team1_df)


                # team2과 경기 기록
                team2_df = pd.DataFrame(df.loc[df['team_1'] == team2])
                team2_df = team2_df.append(df.loc[df['team_2'] == team2])

                team2_df.index = [i for i in range(len(team2_df))]
                print(team2 + ' 경기기록')
                #print(team2_df)


                # team1이 이긴 경기 기록들
                team1_win = team1_df.loc[team1_df['score_1'] > team1_df['score_2']][team1_df['team_1'] == team1]
                team1_win = team1_win.append(team1_df.loc[team1_df['score_1'] < team1_df['score_2']][team1_df['team_2'] == team1])
                #print(team1_win)

                # team2가 이긴 경기 기록들
                team2_win = team2_df.loc[team2_df['score_1'] > team2_df['score_2']][team2_df['team_1'] == team2]
                team2_win = team2_win.append(team2_df.loc[team2_df['score_1'] < team2_df['score_2']][team2_df['team_2'] == team2])
                #print(team2_win)

                # 이긴 경기 기록의 수를 비교해서 이긴 팀 찾기
                winner = ''
                if len(team1_win) > len(team2_win):
                    winner = team1
                elif len(team1_win) < len(team2_win):
                    winner = team2
                print('승리 : ' + winner)


                result1 = df.loc[df['team_1'] == team1][df['team_2'] == team2]
                result2 = df.loc[df['team_1'] == team2][df['team_2'] == team1]
                #print(result1)
                #print(result2)

                # 정확도 구하기 (TP + TN) / (TP + TN + FP + FN)
                try:
                    if result1.iat[0, 2] == winner:
                        if result1.iat[0, 0] > result1.iat[0, 1]:
                            true += 1
                        else:
                            false += 1
                    else:
                        if result1.iat[0, 0] < result1.iat[0, 1]:
                            true += 1
                        else:
                            false += 1

                    if result2.iat[0, 2] == winner:
                        if result2.iat[0, 0] > result2.iat[0, 1]:
                            true += 1
                        else:
                            false += 1
                    else:
                        if result2.iat[0, 0] < result2.iat[0, 1]:
                            true += 1
                        else:
                            false += 1
                except(IndexError):
                    continue


        print(true, false)
        accuracy = true / (true + false)
        print('정확도 :', accuracy)

if __name__ == '__main__':
    ex = prediction_football()



