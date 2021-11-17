import csv
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


def creat_csv(call, output):
    f = open('output.csv', 'w')
    writer = csv.writer(f)
    for i in call:
        writer.writerow(["Elevator call", i.time, i.src, i.dest, i.status, i.allocate])
    f.close()


def allocate(calls_list, elevator_list):
    if len(elevator_list) == 1:
        for call in calls_list:
            call.allocate = 0
    else:
        for call in calls_list:
            i = best(elevator_list, call)
            call.allocate = i


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


def calculate(elevator, call):
    while not len(elevator.callList) == 0 and call.time > elevator.timer:
        elevator.lastFloor = elevator.callList[0].dest
        list = elevator.callList
        list.pop(0)
    e_time = elevator.calculateTime()
    c_time = abs(float(call.dest - call.src)) / elevator.speed + abs(
        float(elevator.lastFloor) - float(call.src)) / elevator.speed
    avg = e_time + c_time
    total = check(call, elevator, elevator.callList, avg)
    return total


def check(call, elevator, callList, avg):
    people = 1
    counter = 0
    k = 0
    ans = avg
    sum = avg
    if abs(elevator.lastFloor - call.src) / elevator.speed < call.time:
        for index in callList:
            sum = sum + index.totalTime
            k = k + 1
        if (len(callList) != 0):
            ans = sum + abs(callList[k - 1].dest - call.src)
        return ans
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

        ans = (sum + counter * elevator.calculate_func) / people
        return ans


# def allocate_call(calls, elevators):
#     cur = -1
#     time = float('inf')
#     call = calls
#     chosen_elev = elevators[0]
#     if len(elevators) == 1:  # if we have only 1 elevator - allocate the call to the spesific elevator
#         return elevators[0].id
#     else:
#         for elev in elevators:
#             if (elev.get_timer() + calculate_time(call, elev)) < time:
#                 if elev.current_state(call.get_direction()) == 1:
#                     time = elev.get_timer() + calculate_time(call, elev)
#                     cur = elev.get_id()
#                     chosen_elev = elev
#         chosen_elev.set_timer(chosen_elev.get_timer() + calculate_time(call, chosen_elev))
#         chosen_elev.add(call)
#     return cur


# def calculate_time(call, elevator):
#     print(type(call))
#     elevTime = float(elevator.calculateTime())  # the elevator generic time
#     calltime = abs(float(call.get_src()) - float(call.get_dest())) / float(
#         elevator.get_speed())  # the time ro go from src to dest at this elevator
#     totalTime = elevTime + calltime
#     return totalTime


## the main function of the program. we receive the files and we will need to return a new file
## the load function will be in the building and calls class
## the creation of the return file will be in a function inside the calls class
## --> after we finished with the creation we will send the list of calls / a single call
##  and the elevator's list to the allocate_call function
## at the end of the function we will write a new scv file and we will return it.
class Offline_Algo:

    # @staticmethod

    def main_function(building, Calls_csv, output):
        b1 = Building()
        b1.load_json(building)
        calls = load_csv(Calls_csv)
        allocate(calls, b1.elevators)
        creat_csv(calls, output)

    ## this function will calculate the total time for a call in specific elevator
    ## that means: for every elevator we will check the time for the call to be completed and then we will save it in the
    ## totalTime parameter we created inside the call.
