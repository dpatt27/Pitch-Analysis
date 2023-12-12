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

    def top_performers(self, attribute1, attribute2):
        for attribute in [attribute1, attribute2]:
            if attribute not in self.df.columns:
                print(f"Invalid attribute: {attribute}. Please enter a valid attribute.")
                return

        mean_value1 = self.df[attribute1].mean()
        std_dev1 = self.df[attribute1].std()

        mean_value2 = self.df[attribute2].mean()
        std_dev2 = self.df[attribute2].std()

        # Calculate standard deviations above the mean for each player
        self.df['StdDevsAboveMean1'] = (self.df[attribute1] - mean_value1) / std_dev1
        self.df['StdDevsAboveMean2'] = (self.df[attribute2] - mean_value2) / std_dev2

        # Sum of standard deviations above the mean for both attributes
        self.df['SumStdDevsAboveMean'] = self.df['StdDevsAboveMean1'] + self.df['StdDevsAboveMean2']

        # Find players with the highest values
        top_players = self.df.nlargest(5, 'SumStdDevsAboveMean')  # Adjust 5 to the number of top players you want to display

        return top_players[['Pitcher', attribute1, attribute2, 'SumStdDevsAboveMean']]

