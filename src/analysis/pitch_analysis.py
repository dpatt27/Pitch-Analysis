import pandas as pd


class PitchAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        self.team_list = self.group_by_teams()

    def group_by_teams(self):
        teams = self.df['PitcherTeam'].unique()
        return list(teams)

    def avg_pitch_speed(self, pitch_type):
        pitch_list = []
        for name in self.team_list:
            pitch_list.append(
                self.df[(self.df['PitcherTeam'] == name) & (self.df['TaggedPitchType'] == pitch_type)]['RelSpeed'].mean())

        team_speed_dict = dict(sorted(zip(self.team_list, pitch_list), key=lambda x: x[1], reverse=True))
        return team_speed_dict

    def top_pitches(self, attribute1, attribute2, pitch_type):
        for attribute in [attribute1, attribute2]:
            if attribute not in self.df.columns:
                print(f"Invalid attribute: {attribute}. Please enter a valid attribute.")
                return

        mean_value1 = self.df[attribute1].mean()
        std_dev1 = self.df[attribute1].std()

        mean_value2 = self.df[attribute2].mean()
        std_dev2 = self.df[attribute2].std()

        # Filter pitches by pitch_type
        filtered_df = self.df[self.df['TaggedPitchType'] == pitch_type].copy()

        # Calculate standard deviations above the mean for each player
        filtered_df['StdDevs1'] = (filtered_df[attribute1] - mean_value1) / std_dev1
        filtered_df['StdDevs2'] = (filtered_df[attribute2] - mean_value2) / std_dev2

        # Sum of standard deviations above the mean for both attributes
        filtered_df['SumStdDevs'] = filtered_df['StdDevs1'] + filtered_df['StdDevs2']

        # Find players with the highest values
        top_players = filtered_df.nlargest(5,
                                           'SumStdDevs')  # Adjust 5 to the number of top players you want to display

        return top_players[['Pitcher', attribute1, attribute2, 'SumStdDevs']]