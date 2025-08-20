import time
from search import *
from movingVehicles import *
import os

def main():
    #find the paths
    inputPath= os.path.dirname(os.path.abspath(__file__)) + "/InputData/test.txt"
    outputPath= os.path.dirname(os.path.abspath(__file__)) + "/OutputData/outputTest.txt"
    #open files
    inputFile =  open(inputPath, "r") 
    outputFile = open(outputPath, "a")
    #make sure output file will be empty
    outputFile.truncate(0)
    
    #read input
    parkingSize = int( inputFile.read() )
    #initialize the problem data
    movingVehicles = MovingVehicles(parkingSize) 
   
    #measure time passed during search
    startTime = time.time()
    pathSolution = astar_search(movingVehicles, movingVehicles.heuristic)
    endTime = time.time()

    #store the output in a string so it can be written in the file at the end
    outputString =  str (pathSolution.solution() )
    outputString += "\n\nPath cost: " + str(pathSolution.path_cost)
    outputString += "\nPossible actions: " + movingVehicles.totalConsideredActions()
    outputString += "\nElapsed time: " + str(endTime - startTime)
    
    outputFile.write(outputString)
    
    #close files
    inputFile.close()
    outputFile.close()
    
    
if __name__ == "__main__":
    main()
