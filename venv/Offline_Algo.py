import json
import csv
from Building import Building
from Elevator import Elevator
from Calls import Calls

class Offline_Algo:
    ## the main function of the program. we receive the files and we will need to return a new file
    ## the load function will be in the building and calls class
    ## the creation of the return file will be in a function inside the calls class
    ## --> after we finished with the creation we will send the list of calls / a single call
    ##  and the elevator's list to the allocate_call function
    ## at the end of the function we will write a new scv file and we will return it.

    #@staticmethod
    def load_csv(filename):  # load the file to the calls class
        calls = []
        with open(filename, 'r') as callsFile:
            csv_reader = csv.reader(callsFile)
            line = next(csv_reader)
            for row in csv_reader:
                c = Calls(row)
                calls.append(c)

        return calls

    def main_function(building , Calls_csv, output):
        b1=Building()
        b1.load_json(building)
        calls = load_csv(Calls_csv)
        allocate_call(calls, b1.get_elevators())

    def allocate_call(calls, elevators):
        if len(elevators) == 1: #if we have only 1 elevator - allocate the call to the spesific elevator
            return elevators[0].id
        else:
            for call in calls:
                cur = -1
                time = float('inf')
                for elev in elevators:
                    if elev.get_timer + calculate_time(call, elev) < time and elev.current_state(elev, call.get_direction):
                        time=elev.get_timer + calculate_time(call, elev)
                        cur=elev.get_id
                        chosen_elev=elev
                cur.get_timer+=calculate_time(call, cur)
                chosen_elev.add(cur.callList, call)
            return cur




    ## this function will calculate the total time for a call in specific elevator
    ## that means: for every elevator we will check the time for the call to be completed and then we will save it in the
    ## totalTime parameter we created inside the call.
    def calculate_time(call,elevator):
        elevTime = elevator.calculateTime() # the elevator generic time
        calltime = abs(call.src() - call.dest())/elevator.speed() # the time ro go from src to dest at this elevator
        totalTime = elevTime + calltime
        return totalTime


    if __name__ == '__main__':
        main_function("C://Users//User//PycharmProjects//Ex1//B1.json", "C://Users//User//PycharmProjects//Ex1//Calls_a.csv", "output.csv")




