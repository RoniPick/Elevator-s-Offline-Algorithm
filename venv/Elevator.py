from Calls import Calls

class Elevator:
    def __init__(self, data):  # load the data to create a new elevator object
        self.id = data["_id"]
        self.speed = data["_speed"]
        self.minFloor = data["_minFloor"]
        self.maxFloor = data["_maxFloor"]
        self.openTime = data["_openTime"]
        self.closeTime = data["_closeTime"]
        self.startTime = data["_startTime"]
        self.stopTime = data["_stopTime"]
        self.callList = []  # a list of the calls that were allocated at the elevator
        self.timer = 0  # counting the elevator time while adding calls
        self.flag = 0


    def calculateTime(self):  # calculating the elevator total time
        return self.closeTime + self.openTime + self.stopTime + self.startTime

    def add(self, call):  # adding the call to the specific elevator list
        self.callList.append(call)

    def remove(self):  # removing the first call from the list
        self.callList.pop(0)

    def current_state(self, call): #return the elevator current state - up or down
        if len(callList)==0:
            return 1 #return ok to any call
        else:
            return call.get_direction == 1 and self.callList[len(callList)-1].dest<=call.src or call.get_direction == -1 and self.callList[len(callList)-1].dest>=call.src

    def get_speed(self):
        return self.speed

    def get_id(self):
        return self.id

    def get_callList(self):
        return self.callList

    def get_timer(self):
        return self.timer

    def get_flag(self):
        return self.flag