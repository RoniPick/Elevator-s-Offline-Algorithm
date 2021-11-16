import json
from Elevator import Elevator


class Building:

    def __init__(self, data):
        self.minFloor = data["_minFloor"]
        self.maxFloor = data["_maxFloor"]
        self.elevators = []
        self.numOfElevators = len(self.elevators)

    def load_json(self, filename):  # load the file to the building class
        with open(filename, "r") as buildingFile:
            dict = json.load(buildingFile)
            b = Building(buildingFile)
            for data in dict["_elevators"]:
                e = Elevator(data)
                b.elevators.append(e)
        return b



    def get_minFloor(self):
        return self.minFloor

    def get_maxFloor(self):
        return self.maxFloor

    def get_numOfElevators(self):
        return self.numOfElevators

    def get_elevators(self):
        return self.elevators

