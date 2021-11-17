# Task 1 - Elevator's Optimization Offline Algorithm 
### _literature Review_:
  1. https://peters-research.com/index.php/papers/understanding-the-benefits-and-limitations-of-destination-control/
  2. https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30
  3. https://trace.tennessee.edu/cgi/viewcontent.cgi?article=3380&context=utk_chanhonoproj

### _The Offline Algorithm_:
Our task is: to allocate a call in the best elevator that will execute the call\request in the fastest time and will not increase the average time.
We get a list of the call's and a list of the elevators that are in the building.
If there's only one elevator - we will allocate all the calls in that elevator.
If there's more than one elevator at the building - we will go through the list of the elevators at the building and calculate the time it takes for every one of them to complete a specific call.

#### _The calculate will include several parameters_: 
- the time it take's the elevator to go from the source floor to the destination floor + the time it take to the elevator to open,close,start and stop. 
- the amount of people that because of the new call their execution time (the time it took the elevator to finish the call) will increase + the new time it take for the elevator to complete the call after we add the call to the elevator.
- then we divivde the new time we found (plus the time of the new call) with the amount of people that "stucked" because of the new call + the person of the new call.
After we calculated the time for the call in a specific elevator, we will compare each time we got in order to find the best time (the best time represent thebest elevator).
At the end, we allocate the call to the best elevator and set the allocate parameter of the call to the elevator's index.
When we finished to went through the list of calls we will create a new csv file of the calls after we allocated them.

#### _How it actually works_:
for every elevator, we creating a call's list that contains the calls we allocated in the elevator.plus,  
