import random
import os

def main():
    
    #generate input 
    lowerBound = 2
    upperBound = 7
    randomSize = random.randint(lowerBound, upperBound)
    
    inputPath= os.path.dirname(os.path.abspath(__file__)) + "/InputData/test.txt"
    
    f = open(inputPath, "a")
    f.write(str(randomSize))

    f.close()
    
if __name__ == "__main__":
    main()
