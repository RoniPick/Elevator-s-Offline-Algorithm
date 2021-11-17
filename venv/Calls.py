import csv


class Calls:
    def load(self): # load the data to create a new call object
        self.name = 0
        self.time = 0
        self.src = 0
        self.dest = 0
        self.status = 0 # isn't relevant
        self.allocate = 0
        self.totalTime = 0 # we would like to know the time it took to do the call (when allocate to the elevator)

    def __init__(self, row): # load the data to create a new call object
        self.name = row[0]
        self.time = float(row[1])
        self.src = int(row[2])
        self.dest = int(row[3])
        self.status = 0 # isn't relevant
        self.allocate = row[5]
        self.totalTime = 0 # we would like to know the time it took to do the call (when allocate to the elevator)



    def create_csv(self, filename, calls):
        with open('filename', 'wb', newline=" ") as output:
            filewriter=csv.writer(output)
            for call in calls:
                c=call.__dict__
                filewriter.writerow(c)


    def get_time(self):
        return self.time

    def get_direction(self):
        if self.src<self.dest:
            return 1
        else:
            return -1

    def get_allocate(self):
        return self.allocate

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest
