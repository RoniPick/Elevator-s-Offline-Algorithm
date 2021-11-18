class Elevator:
    def __init__(self, data):  # load the data to create a new elevator object
        self.id = int(data["_id"])
        self.speed = float(data["_speed"])
        self.minFloor = int(data["_minFloor"])
        self.maxFloor = int(data["_maxFloor"])
        self.openTime = float(data["_openTime"])
        self.closeTime = float(data["_closeTime"])
        self.startTime = float(data["_startTime"])
        self.stopTime = float(data["_stopTime"])
        self.timer = 0  # save the time the elevator should finish with all her calls.
        self.lastFloor = 0  # tell us the last floor the elevator stopped at.
        self.callList = []  # a list of the calls that were allocated at the elevator

    def add(self, call):  # adding the call to the specific elevator list.
        self.callList.append(call)

    def remove(self):  # removing the first call from the list.
        self.callList.pop(0)

    def calculateTime(self):  # calculating the generic parameter's time.
        return self.openTime + self.closeTime + self.startTime + self.stopTime
