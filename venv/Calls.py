import csv


class Calls:
    def __init__(self, row): # load the data to create a new call object
        self.name = row[0]
        self.time = row[1]
        self.src = row[2]
        self.dest = row[3]
        self.status = 0 # isn't relevant
        self.allocate = row[5]
        self.totalTime = 0 # we would like to know the time it took to do the call (when allocate to the elevator)

    def load_csv(self, filename):  # load the file to the calls class
        calls = []
        with open(filename) as callsFile:
            csv_reader = csv.reader(callsFile)
            line = next(csv_reader)
            for row in csv_reader:
                c = Calls(row)
                calls.append(c)
        return calls

    def get_time(self):
        return self.time


    def get_allocate(self):
        return self.allocate

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest



