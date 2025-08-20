from search import Problem
import math

class MovingVehicles(Problem):

    """ Initialize the parameters needed to solve the problem """
    def __init__(self, parkingSize):
        #decides which car will be moved
        self.carIndex = 0
        #the size of the parking lot (matrix)
        self.parkingSize = parkingSize
        #number of actions the algorithm takes into consideration 
        self.consideredActions = 0
        
        #the parking lots at the begining and at the end
        initialState = list() 
        goalState = list() 

        #generate the matrix for the two states
        for i in range (parkingSize):
             for j in range (parkingSize):
                 
                 #for initial state: number them on the first column
                 if(i == 0):
                     initialState.append(j + 1)
                 else:
                     initialState.append(0)
                  
                 #for the goal state: number them on the lasts column, in reversed
                 if(i == parkingSize - 1):
                     goalState.append(parkingSize - j)
                 else:
                     goalState.append(0)

        #we need to transform them into a hashable containter
        Problem.__init__(self, tuple(initialState), tuple(goalState))


    """Search for an empty space and return its index, for the given state"""
    def findFirstEmptySpot(self, state):
       
        #if we have not reached the last car, increase the index
        if self.carIndex <= self.parkingSize:
            self.carIndex += 1
        
        #if we reached the last car we reset the index
        if self.carIndex == self.parkingSize + 1:
            self.carIndex = 1

        return state.index(self.carIndex)


    """Define all the possible actions (states) a car can make"""
    def actions(self, state):
        #the default action is to remain in the same place
        possibleActions = ['Stay']
        self.index = self.findFirstEmptySpot(state)

        #if we reached our goal state, we remain here
        if state[self.index] == self.goal[self.index]:
            return possibleActions
      
        #Conditions needed to ensure that a car does not move out of bounds
        
        if self.index >= self.parkingSize and state[self.index - self.parkingSize] == 0:
            possibleActions.append('MoveUp')
        
        if self.index <= (pow(self.parkingSize, 2) - self.parkingSize - 1) and state[self.index + self.parkingSize] == 0:
            possibleActions.append('MoveDown')

        if self.index % self.parkingSize != self.parkingSize - 1 and state[self.index + 1] == 0:
            possibleActions.append('MoveRight')

        if self.index % self.parkingSize != 0 and state[self.index - 1] == 0:
            possibleActions.append('MoveLeft')

        if self.index >= 2 * self.parkingSize and state[self.index - 2 * self.parkingSize] == 0 and state[self.index - self.parkingSize] != 0 :
            possibleActions.append('JumpUp')

        if self.index <= (pow(self.parkingSize, 2) - 2 * self.parkingSize - 1) and state[self.index + self.parkingSize] != 0 and state[self.index + 2 * self.parkingSize] == 0:
            possibleActions.append('JumpDown')

        if self.index % self.parkingSize < self.parkingSize - 2 and state[self.index + 2] == 0 and state[self.index + 1] != 0:
            possibleActions.append('JumpRight')

        if self.index % self.parkingSize > 1 and state[self.index - 2] == 0 and state[self.index - 1] != 0:
            possibleActions.append('JumpLeft')

        #increase number of considered actions
        self.consideredActions += len(possibleActions)
        
        #return a list of all the actions a car can make at a given step
        return possibleActions
    
    

    """ We take into consideration a state and an action, and decide what will be the 
        result following the action, for each state """
    def result(self, state, action):
        
        #create a new state        
        nextState = list(state)
        #create a list of all the possible actions and results for each state
        carActions = {'Stay':0,
                 'MoveUp': -self.parkingSize,  
                 'MoveDown': self.parkingSize, 
                 'MoveRight':1, 
                 'MoveLeft':-1, 
                 'JumpUp': -2 * self.parkingSize,
                 'JumpDown': +2 * self.parkingSize, 
                 'JumpRight': 2, 
                 'JumpLeft': -2 } 
        
        #find the index of the position where we want to move the car
        nextPositionIndex = self.index + carActions[action]
        nextState[self.index], nextState[nextPositionIndex] = nextState[nextPositionIndex], nextState[self.index] 

        return tuple(nextState)


    """The heuristic used to solve the problem. Here is the Manhattan Distance"""
    def heuristic(self, node):
        return sum( abs(currentState - goalState) / 2 for (currentState, goalState) in zip(node.state, self.goal) )
    
    
    """Auxiliary function used to print the number of actions taken into consideration"""
    def totalConsideredActions(self):
        return str( self.consideredActions )
