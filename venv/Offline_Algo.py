import csv
import sys

from Elevator import Elevator
from Building import Building
from Calls import Calls


def load_csv(filename):  # load the file to the calls class
    calls = []
    with open(filename) as callsFile:
        csv_reader = csv.reader(callsFile)
        line = next(csv_reader)
        for row in csv_reader:
            c = Calls(row)
            calls.append(c)
    return calls


def create_csv(call, output):  # creates a csv file from the calls list
    f = open('output.csv', 'w', newline="")
    writer = csv.writer(f)
    for i in call:
        writer.writerow(["Elevator call", i.time, i.src, i.dest, i.status, i.allocate])
    f.close()


"""in this function we go through all the calls that are in the calls list and send every one of them to the "best" 
function. At the end of the run we get the index of the elevator that fits the most for this call """


def allocate(calls_list, elevator_list):
    if len(elevator_list) == 1:
        for call in calls_list:
            call.allocate = 0
    else:
        for call in calls_list:
            i = best(elevator_list, call)
            call.allocate = i


""" this function tell us which elevator is the best for the specific call by comפering between the elevators in the building.
We will get a call from the call's list and the list of the elevators that in the building.
Then, we will send a specific elevator and the call to the "calculate" function. """


def best(elevator_list, call):
    best_time = float('inf')
    index = -1
    for i in elevator_list:
        temp = calculate(i, call)
        if best_time > temp:
            best_time = temp
            index = i
    call.totalTime = best_time
    index.add(call)
    index.timer = call.time + best_time
    return index.id


""" this function will calculate the total time for a call in specific elevator
    that means: for every elevator we will check the time for the call to be completed and then we will save it in the
    totalTime parameter we created inside the call."""


def calculate(elevator, call):
    while not len(elevator.callList) == 0 and call.time > elevator.timer:
        elevator.lastFloor = elevator.callList[0].dest
        list = elevator.callList
        list.pop(0)
    e_time = elevator.calculateTime()
    c_time = (call.call_length() + abs(float(elevator.lastFloor) - float(call.src))) / elevator.speed
    avg = e_time + c_time
    total = check(call, elevator, elevator.callList, avg)
    return total


""" this function will check if there are people that in the elevator that if we add the new call to the elevator,
their total execution rime for their request will be longer than before.
We will calculate the average of the new time we get for each of them. """


def check(call, elevator, callList, avg):
    people = 1
    counter = 0
    k = 0
    sum = avg
    if abs(elevator.lastFloor - call.src) / elevator.speed < call.time:
        for index in callList:
            sum = sum + index.totalTime
            k = k + 1
        if len(callList) != 0:
            sum = sum + abs(callList[k - 1].dest - call.src)
        return sum
    else:
        for index in callList:
            delayed = False
            if call.status == index.status:
                if call.src in range(index.src, index.dest):
                    delayed = True
                    counter + 1
                if call.dest in range(index.src, index.dest):
                    delayed = True
                    counter + 1
                if delayed:
                    people + 1
            sum = sum + index.totalTime
            index + 1

        sum = (sum + counter * elevator.calculate_func) / people
        return sum


class Offline_Algo:

    """ the main function of the program. we receive the files and we need to return a new file
    after we finished with the creation we will send the list of calls and the elevator's list to the allocate function
    at the end of the function we will write a new csv file and we will return it. """

    def main_function(building, Calls_csv, output):
        b1 = Building()
        b1.load_json(building)
        calls = load_csv(Calls_csv)
        allocate(calls, b1.elevators)
        create_csv(calls, output)

    if __name__ == "__main__":
        ##main_function("files\\B1.json", "files\\Calls_a.csv", "output.csv")
        list = sys.argv
        buildingLocation = list[1]
        callsLocation = list[2]
        outputLocation = list[3]
        main_function(buildingLocation, callsLocation, outputLocation)



