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
            self.numOfElevators = len(self.elevators)

