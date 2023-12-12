from pitch_analysis import PitchAnalysis


def display_results(pitch_type, analysis):
    team_speed_dict = analysis.avg_pitch_speed(pitch_type)

    print(f"\nAverage Speed for {pitch_type} by Team (descending order):")
    for team, speed in team_speed_dict.items():
        print(f"{team}: {speed:.2f} mph")


def display_top_pitches(attribute1, attribute2, pitch_type, analysis):
    top_players_data = analysis.top_pitches(attribute1, attribute2, pitch_type)

    if top_players_data is not None:
        print(f"\nPitches with the highest sum of standard deviations above the mean:")
        print(top_players_data)


if __name__ == "__main__":
    FILE_PATH = '/Users/StersCSV.xlsx'
    analysis = PitchAnalysis(FILE_PATH)

    # User input for the desired pitch type
    user_pitch_input = input("Enter the pitch type (Fastball, Cutter, Sinker, Slider, Curveball, ChangeUp): ")

    # Validate user input
    valid_pitch_types = ['Fastball', 'Cutter', 'Sinker', 'Slider', 'Curveball', 'ChangeUp']
    if user_pitch_input not in valid_pitch_types:
        print("Invalid pitch type. Please enter a valid pitch type.")
    else:
        display_results(user_pitch_input, analysis)

    user_attribute1_input = input("Enter the first attribute (RelSpeed, SpinRate, VertBreak, HorzBreak, Extension): ")
    user_attribute2_input = input("Enter the second attribute (RelSpeed, SpinRate, VertBreak, HorzBreak, Extension):  ")

    # Calculate sum of standard deviations above the mean and display top players
    display_top_pitches(user_attribute1_input, user_attribute2_input, user_pitch_input, analysis)
