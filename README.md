# Task 1 - Elevator's Optimization Offline Algorithm 
### _by: Roni Pick - 206794075 & Almog David - 207749441_
## _literature Review_:
  1. https://peters-research.com/index.php/papers/understanding-the-benefits-and-limitations-of-destination-control/
  2. https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30
  3. https://trace.tennessee.edu/cgi/viewcontent.cgi?article=3380&context=utk_chanhonoproj

## _The Offline Algorithm_:
Our task is: to allocate a call in the best elevator that will execute the call\request in the fastest time and will not increase the average time.
We get a list of the call's and a list of the elevators that are in the building.
If there's only one elevator - we will allocate all the calls in that elevator.
If there's more than one elevator at the building - we will go through the list of the elevators IN the building and calculate the time it takes for every one of them to complete a specific call. 

### _The calculate will include several parameters_: 
- the time it take's the elevator to go from her position to the source floor and then to the destination floor + the time it take to the elevator to open,close,start and stop. 
- the amount of people that because of the new call their execution time (the time it took the elevator to finish the call) will increase + the new time it take for the elevator to complete the call after we add the call to the elevator.
- then we divivde the new time we found (plus the time of the new call) with the amount of people that "stucked" because of the new call + the person of the new call.
After we calculated the time for the call in a specific elevator, we will compare each time we got in order to find the best time (the best time represent thebest elevator).
At the end, we allocate the call to the best elevator and set the allocate parameter of the call to the elevator's index.
When we finished to went through the list of calls we will create a new csv file of the calls after we allocated them.

### _How it actually works_:
the elevator class: for every elevator, we create a call's list that contains the calls we allocated in the elevator. plus, a timer parameter which tell us when the elevator need to finish her path and a prameter ("lastFloor") that show us the last floor the elevator stopped.
the calls class: for every call, we create a statuse parameter that indicate the direction of the call - if the call is to go up, status = 1. id the call is to go down, status = -1. 
plus, we add a totalTime parameter that save the time the elevator execute the call. 

### _we have four primary functions_:
1. allocate - in this function we go through all the calls that are in the calls list and send every one of them to the "best" function
2. best - this function tell us which elevator is the best for the specific call by comering between the elevators in the building.
we will get a call from the call's list and the list of the elevators that in the building. then, we will send a specific elevator and the call to the "calculate" function.
3. calculate -this function will calculate the total time for a call in specific elevator.
that means: for every elevator we will check the time for the call to be completed and then we will save it in the totalTime parameter we created inside the call.
4. check - this function will check if there are people that in the elevator that if we add the new call to the elevator, their total execution rime for their request will be longer than before. we will calculate the average of the new time we get for each of them. 

### _How to run_:
#### In order to run the program, you will need to install a few plugings:
- in the Offline_Algo class  you need to import csv (in order to read and create the csv files) and sys (in order to allow the user to run the function's from the terminal window).
- in the Building class you need to import json (in order to read the json file).

- In order to run the simulator, first enter into the Ex1.py.

    py .\Ex1.py "Ex1_Buildings\B1.json" "Ex1_Calls\Calls_a.csv" "output.csv"
    
 You can choose every building from the following bulding file's (B1.json, B2, B3, B4 or B5).
 
 You can select every call file from the following call file's (Call_a.csv, b, c or d).
 
 Then, run the following command for the .jar file:

    java -jar Ex1_checker_V1.2_obf.jar <First_ID,Second_ID> Ex1_Buildings/B2.json output.csv Calls_a_B2_log.csv
    
 The output log file is located in output.csv.
 
#### in order to run the test: 
- open Ex1.py. and test.py 
- import pandas
- run the class "MyTestCase"

## _UML diagram_: 
![Ex1](https://user-images.githubusercontent.com/93771702/142445572-4015aaeb-3348-4907-95de-53e74edc5612.png)

## _Run results_:

| Call case/Bilding | B1     | B2     | B3     | B4     | B5     |
|-------------------|--------|--------|--------|--------|--------|
|      Case a       | 112.92 |  51.71 |  31.19 |  18.41 |  12.15 |
|      Case b       |        |        | 545.95 | 250.05 | 63.56  |
|      Case c       |        |        | 560.22 | 247.30 | 61.72  |
|      Case d       |        |        | 600.25 | 244.81 | 65.56  |

