import json
import math

from Elevator import Elevator


class Building:

    def load_json(self, file_name):
        with open(file_name, "r") as buildingFile:
            self.elevators = []
            dict = json.load(buildingFile)
            self.minFloor = dict["_minFloor"]
            self.maxFloor = dict["_maxFloor"]
            for data in dict["_elevators"]:
                e = Elevator(data)
                self.elevators.append(e)
            self.numOfElevators = len(self.elevators)

    def minFloor(self):
        return self.minFloor

    def maxFloor(self):
        return self.maxFloor

    def numOfElevators(self):
        return self.numOfElevators

    def elevators(self):
        return self.elevators

