import unittest
from src.analysis.pitch_analysis import *


class TestPitchAnalysis(unittest.TestCase):
    def setUp(self):
        # Load in Test Data
        self.analysis = PitchAnalysis('/Users/Test Data.xlsx')

    def test_group_by_teams(self):

        # Call the method being tested
        result = self.analysis.group_by_teams()
        expected_result = ['Foresters', 'Blues', 'Saints']
        # Assert the expected result
        self.assertCountEqual(result, expected_result)

    def test_avg_pitch_speed(self):
        result = self.analysis.avg_pitch_speed('Fastball')

        expected_result = {'Blues': 100.0, 'Foresters': 90.0, 'Saints': 70.0}
        self.assertDictEqual(result, expected_result)


    def test_top_pitches(self):
        result = self.analysis.top_pitches('SpinRate', 'RelSpeed', 'Fastball')
        expected_result = pd.DataFrame({
            'Pitcher': ['Homie Buelher', 'Clip Hamstring', 'Skid Can'],
            'SpinRate': [2500, 2000, 1500],
            'RelSpeed': [100, 90, 70],
            'SumStdDevs': [2.788660, 1.023546, -1.629624]
        })

        result = result.reset_index(drop=True)
        expected_result = expected_result.reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()
