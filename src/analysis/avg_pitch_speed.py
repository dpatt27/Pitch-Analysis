# Load the data from the Excel file
import pandas as pd

df = pd.read_excel('/Users/StersCSV.xlsx')

# creates an empty list that is to be filled with team names
team_list = []


# Group data by team and pitch type, calculate average pitch velocity and spin rate
def group_by_teams():
    for name in df['PitcherTeam'].unique():
        if name not in team_list:
            team_list.append(name)
    return team_list


class AveragePitchSpeed:
    @staticmethod
    def avg_pitch_speed(pitch_type):
        pitch_list = []
        for name in team_list:
            pitch_list.append(
                df[(df['PitcherTeam'] == name) & (df['TaggedPitchType'] == pitch_type)]['RelSpeed'].mean())

        team_speed_dict = dict(sorted(zip(team_list, pitch_list), key=lambda x: x[1], reverse=True))
        return team_speed_dict



#class PitchSpeedDifference:
