# Task 1 - Elevator's Optimization Offline Algorithm 
### _literature Review_:
  1. https://peters-research.com/index.php/papers/understanding-the-benefits-and-limitations-of-destination-control/
  2. https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30
  3. https://trace.tennessee.edu/cgi/viewcontent.cgi?article=3380&context=utk_chanhonoproj

### _The Offline Algorithm_:
Our task is: to allocate a call in the best elevator that will execute the call\request in the fastest time and will not increase the average time.
We get a list of the call's and a list of the elevators that are in the building.
If there's only one elevator - we will allocate all the calls in that elevator.
If there's more than one elevator at the building - we will go through the list of the elevators IN the building and calculate the time it takes for every one of them to complete a specific call. 

#### _The calculate will include several parameters_: 
- the time it take's the elevator to go from her position to the source floor and then to the destination floor + the time it take to the elevator to open,close,start and stop. 
- the amount of people that because of the new call their execution time (the time it took the elevator to finish the call) will increase + the new time it take for the elevator to complete the call after we add the call to the elevator.
- then we divivde the new time we found (plus the time of the new call) with the amount of people that "stucked" because of the new call + the person of the new call.
After we calculated the time for the call in a specific elevator, we will compare each time we got in order to find the best time (the best time represent thebest elevator).
At the end, we allocate the call to the best elevator and set the allocate parameter of the call to the elevator's index.
When we finished to went through the list of calls we will create a new csv file of the calls after we allocated them.

#### _How it actually works_:
the elevator class: for every elevator, we create a call's list that contains the calls we allocated in the elevator. plus, a timer parameter which tell us when the elevator need to finish her path and a prameter ("lastFloor") that show us the last floor the elevator stopped.
the calls class: for every call, we create a statuse parameter that indicate the direction of the call - if the call is to go up, status = 1. id the call is to go down, status = -1. 
plus, we add a totalTime parameter that save the time the elevator execute the call. 

#### _we have four primary functions_:
1. allocate - in this function we go through all the calls that are in the calls list and send every one of them to the "best" function
2. best - this function tell us which elevator is the best for the specific call by comering between the elevators in the building.
we will get a call from the call's list and the list of the elevators that in the building. then, we will send a specific elevator and the call to the "calculate" function.
3. calculate -this function will calculate the total time for a call in specific elevator.
that means: for every elevator we will check the time for the call to be completed and then we will save it in the totalTime parameter we created inside the call.
4. check - this function will check if there are people that in the elevator 


