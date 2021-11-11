import csv


class Calls:
    def __init__(self, row):
        self.name = row[0]
        self.time = row[1]
        self.src = row[2]
        self.dest = row[3]
        self.status = 0
        self.allocate = row[5]

    def __init__(self, filename):
        calls = []
        with open(filename) as callsFile:
            csv_reader = csv.reader(callsFile)
            line = next(csv_reader)
            for row in csv_reader:
                c = Calls(row)
                calls.append(c)
