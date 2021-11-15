import json
from Elevator import Elevator


class Building:


    def __init__(self, data):
        self.minFloor = data["_minFloor"]
        self.maxFloor = data["_maxFloor"]
        self.elevators = []
        self.numOfElevators = len(self.elevators)

    def load_json(self, file_name): # load the file to the building class
        with open(file_name, "r") as buildingFile:
            self.elevators = []
            dict = json.load(buildingFile)
            self.minFloor = dict["_minFloor"]
            self.maxFloor = dict["_maxFloor"]
            for data in dict["_elevators"]:
                e = Elevator(data)
                self.elevators.append(e)
            self.numOfElevators = len(self.elevators)



    def get_minFloor(self):
        return self.minFloor

    def get_maxFloor(self):
        return self.maxFloor

    def get_numOfElevators(self):
        return self.numOfElevators

    def get_elevators(self):
        return self.elevators

