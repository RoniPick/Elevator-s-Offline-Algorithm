class Calls:
    def load(self):  # empty constructor
        self.name = 0
        self.time = 0
        self.src = 0
        self.dest = 0
        self.status = 0  # tell us the direction/flag of the call: up, down
        self.allocate = 0
        self.totalTime = 0  # we would like to know the time it took to do the call (when allocate to the elevator)

    def __init__(self, row):  # load the data to create a new call object
        self.name = row[0]
        self.time = float(row[1])
        self.src = int(row[2])
        self.dest = int(row[3])
        if self.src > self.dest:
            self.status = -1
        elif self.dest > self.src:
            self.status = 1
        self.allocate = row[5]
        self.totalTime = 0  # we would like to know the time it took to do the call (when allocate to the elevator)

    def call_length(self):
        return abs(self.dest - self.src)

