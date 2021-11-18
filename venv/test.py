import unittest
from Building import Building
import Ex1
from Elevator import Elevator
import pandas as pd

class MyTestCase(unittest.TestCase):
    def test_main(self):
        buildings = ["B1.json", "B2.json", "B3.json", "B4.json"]
        calls = ["Calls_a.csv", "Calls_b.csv", "Calls_c.csv", "Calls_d.csv"]
        for building_jason in buildings:
            for calls_csv in calls:
                Ex1.Offline_Algo.main_function(building_jason, calls_csv, "output")
                df=pd.read_csv("output.csv", index_col=False, header=None)
                perc = len(df.index)*0.01
                b = Building()
                b.load_json(building_jason)
                for k in df[[5]].value_counts():
                    self.assertTrue(k > perc)

    def test_calculateTime(self):
        Ex1.Offline_Algo.main_function("B1.json", "Calls_a.csv", "output")
        b = Building()
        b.load_json("B1.json")
        elevtime = 2.0+2.0+3.0+3.0
        self.assertEqual(elevtime, Elevator.calculateTime(b.elevators[0]))

        Ex1.Offline_Algo.main_function("B2.json", "Calls_a.csv", "output")
        b = Building()
        b.load_json("B2.json")
        elev0time = 2.0 + 2.0 + 3.0 + 3.0
        self.assertEqual(elev0time, Elevator.calculateTime(b.elevators[0]))
        self.assertEqual(elev0time, Elevator.calculateTime(b.elevators[1]))

        Ex1.Offline_Algo.main_function("B3.json", "Calls_a.csv", "output")
        b = Building()
        b.load_json("B3.json")
        elev0time = 2.0 + 2.0 + 3.0 + 3.0
        elev1time = 1.4285714285714286 + 1.4285714285714286 + 2.142857142857143 + 2.142857142857143
        self.assertEqual(elev0time, Elevator.calculateTime(b.elevators[0]))
        self.assertEqual(elev1time, Elevator.calculateTime(b.elevators[1]))


if __name__ == '__main__':
    unittest.main()
