from Offline_Algo import Offline_Algo
import sys

if __name__ == "__main__":
    # main_function("files\\B1.json", "files\\Calls_a.csv", "output.csv")

    list = sys.argv
    buildingLocation = list[1]
    callsLocation = list[2]
    outputLocation = list[3]
    Offline_Algo.main_function(buildingLocation, callsLocation, outputLocation)
