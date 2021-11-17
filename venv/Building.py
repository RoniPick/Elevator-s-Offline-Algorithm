import json
from Elevator import Elevator


class Building:

    def __init__(self):
        self.minFloor = 0
        self.maxFloor = 0
        self.elevators = []
        self.numOfElevators = len(self.elevators)

    def load_json(self, filename):  # load the file to the building class
        with open(filename, 'r') as buildingFile:
            dict = json.load(buildingFile)
            self.minFloor = dict["_minFloor"]
            self.maxFloor = dict["_maxFloor"]
            self.elevators = []
            for data in dict["_elevators"]:
               e = Elevator(data)
               self.elevators.append(e)


    def get_minFloor(self):
        return self.minFloor

    def get_maxFloor(self):
        return self.maxFloor

    def get_numOfElevators(self):
        return self.numOfElevators

    def get_elevators(self):
        return self.elevators

