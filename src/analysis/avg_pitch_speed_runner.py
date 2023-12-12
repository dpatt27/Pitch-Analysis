from avg_pitch_speed import *


def display_results(pitch_type):
    avg_speed_obj = AveragePitchSpeed()
    teams = group_by_teams()
    team_speed_dict = avg_speed_obj.avg_pitch_speed(pitch_type)

    print(f"\nAverage Speed for {pitch_type} by Team (descending order):")
    for team, speed in team_speed_dict.items():
        print(f"{team}: {speed:.2f} mph")


# Main runner
if __name__ == "__main__":
    # User input for the desired pitch type
    user_pitch_input = input("Enter the pitch type (Fastball, Cutter, Sinker, Slider, Curveball, ChangeUp): ")

    # Validate user input
    valid_pitch_types = ['Fastball', 'Cutter', 'Sinker', 'Slider', 'Curveball', 'ChangeUp']
    if user_pitch_input not in valid_pitch_types:
        print("Invalid pitch type. Please enter a valid pitch type.")
    else:
        display_results(user_pitch_input)