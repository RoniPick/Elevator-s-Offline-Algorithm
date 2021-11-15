import json
import csv
import Building
import Elevator
import Calls


class Offline_Algo:
    ## the main function of the program. we receive the files and we will need to return a new file
    ## the load function will be in the building and calls class
    ## the creation of the return file will be in a function inside the calls class
    ## --> after we finished with the creation we will send the list of calls / a single call
    ##  and the elevator's list to the allocate_call function
    ## at the end of the function we will write a new scv file and we will return it.
    def main_function(Building_File, Calls_File, output_File):
    building =
    calls =

    def load_json(self):  # load the file to the building class
        with open(self, "r") as buildingFile:
            dict = json.load(buildingFile)
            b = Building(buildingFile)
            for data in dict["_elevators"]:
                e = Elevator(data)
                b.elevators.append(e)
        return b

    def load_csv(self, filename):  # load the file to the calls class
        calls = []
        with open(filename) as callsFile:
            csv_reader = csv.reader(callsFile)
            line = next(csv_reader)
            for row in csv_reader:
                c = Calls(row)
                calls.append(c)
        return calls

    ## this function will get a list of calls /a single call and allocate the call at an elevator
    ## we will run all over the new list we created to the calls - as long as the list isn't empty.
    ## if we have only one elevator - send the call to this elevator for all the calls.
    ## if we have more than one elevator - for every call we will run all over the elevators that in the building
    ## we will use the best_time and calculate_time function
    ## after we will allocate the call to the elevator we will change the location number to the relevant elevator.
    def allocate_call(calls, []):


    # this call will tell us which elevator is the best for the specific call
    ## we will get a call from the call's list and the list of the elevators that in the building.
    ## then, we will send a specific elevator and the call to the calculate_time function
    def best_time():

    # this function will calculate the total time for a call in specific elevator
    ## that means: for every elevator we will check the time for the call to be completed and then we will save it in the
    ## totalTime parameter we created inside the call.
    def calculate_time(calls,elevator):


    if __name__ == '__main__':
        main_function()




