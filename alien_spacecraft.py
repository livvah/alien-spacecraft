# Olivia Vahsen
# =================================================================
# AlienSpacecraft Class
# =================================================================
def main():
    
    shipVulcan = AlienSpacecraft()
    showMenuVulcanShip(shipVulcan)
    
#user input for ammunition, set ammunition level
def addAmmunitionVulcanShip(shipVulcan):
    
    ammunitionLevel = int(input("\nPlease enter a number between 1 and 10 for ammunition: "))
    shipVulcan.setAmmunitionLevel(ammunitionLevel)
    showMenuVulcanShip(shipVulcan)
    
#print current values
def ValuesVulcanShip(shipVulcan):
    shipVulcan.printCurrentValues()
    showMenuVulcanShip(shipVulcan)
    
#user input for direction, set direction
def setDirection(shipVulcan):
    try:
        directionInput= input("Please enter \'north\', \'south\', \'east\' or \'west\' ")
            
    except ValueError as e:
        print(e)
        sys.exit()
                
    try:
        shipVulcan.setDirection(directionInput)
                
    except ValueError as e:
        print("Not a direction, Spock!", e)
        
    showMenuVulcanShip(shipVulcan)
    
#user input velocity int, set velocity
def setVelocity(shipVulcan):
    try:
        velocityInput= int(input("Please enter a number between 0 and 10 for velocity:"))
            
    except ValueError as e:
        print(e)
        sys.exit()
                
    try:
        shipVulcan.setVelocity(velocityInput)
                
    except ValueError as e:
        print("Wrong input, Spock!", e)
        sys.exit()
    showMenuVulcanShip(shipVulcan)
                    
#main user menu, should repeat until exit prompt entered
def showMenuVulcanShip(shipVulcan):
    
    userInput = 0
    
    while ((userInput > 6) or (userInput < 1)):
        
        print("\n1) Add Ammunition (1-10)")
        print("2) Set Velocity (0-10)")
        print("3) Set Direction (North, South, East, West)")
        print("4) Fire Weapons")
        print("5) Print Current Values")
        print("6) Exit\n")
        
        try:
            userInput = int(input("Ambassador Spock, please enter your selection: "))
        except ValueError:
            print("\n Ambassador Spock, please make a selection from the following choices:")
            
    if (userInput == 1):
        addAmmunitionVulcanShip(shipVulcan)
        
    if (userInput == 2):
        print("You selected:",userInput)
        setVelocity(shipVulcan)
        
    if (userInput == 3):
        print("You selected:",userInput)
        setDirection(shipVulcan)

    if (userInput == 4):
        print("You selected:",userInput)
        shipVulcan.fireWeapons()
        showMenuVulcanShip(shipVulcan)
        
    if (userInput == 5):
        ValuesVulcanShip(shipVulcan)
        
    if (userInput == 6):
        print("Exit. Goodbye, Amabassador Spock.")
        
    

class AlienSpacecraft(object):
    
    # Constructor
    # Creates an AlienSpacecraft and initializes class variables
    #
    def __init__(self):
        
        print("A alien spacecraft has been created!")
        self.velocity = 0
        self.direction = "north"
        self.ammunitionLevel = 0  
    
    # setVelocity()
    # Sets the velocity of the alien spacecraft
    # Valid values are 0 - 10
    # raises ValueError if velocity is out of range
    #    
    def setVelocity(self, velocity) :
        
        if (velocity < 0 or (velocity + self.velocity) > 10 ) :
            raise ValueError("Error: velocity must be between 0 and 10")
        
        self.velocity = velocity
        
        print("Moving ", self.direction, "at velocity of ", self.velocity)
    
    # getVelocity()
    # returns the current spacecraft velocity
    #    
    def getVelocity(self) :
        return self.velocity
    
    # setDirection()
    # Sets the direction of the spacecraft
    # Valid directions are north, south, east or west
    # Raises a ValueError for an invalid direction
    def setDirection(self, direction) :
        
        allDirections = ["north", "south", "east", "west"]
        
        if (direction not in allDirections ) :
            raise ValueError("Error: directon must be north, south, east or west")
        
        self.direction = direction
        
        print("Direction set to ", self.direction)
    
    # getDirection()
    # Returns the current direction
    #
    def getDirection(self):
        
        return self.direction
    
    # setAmmunitionLevel()
    # Sets the ammunitionLevel of the spacecraft
    # Valid values are 0 - 10
    # Raises a ValueError if for an invalid ammunitionLevel
    #
    def setAmmunitionLevel(self, ammunitionLevel):
        
        if (ammunitionLevel < 0 or ammunitionLevel > 10) :
            raise ValueError("AmmunitionLevel must be between 0 and 10")
    
        self.ammunitionLevel = ammunitionLevel
        
        print("AmmunitionLevel set to ", self.ammunitionLevel)

    # getAmmunitionLevel()
    # Returns the current ammumition level
    #
    def getAmmunitionLevel(self):
        
        return self.ammunitionLevel

    # fireWeapons()
    # Fires the alien spacecraft weapons.
    # Decrements ammunitionlevel by 1
    # Prints error message if weapons fired and there is no
    # ammunition
    def fireWeapons(self):
        
        if (self.ammunitionLevel ==  0) :
            print("No Ammunition!  Rats, we're done for!")
            return
        else :
            self.ammunitionLevel -= 1
            print("Weapons fired!")

    # printCurrentValues()
    # Prints current values of object attributes
    #
    def printCurrentValues(self):
        
        print("\nCurrent Values:\n-------------------")
        print("Velocity: ", self.getVelocity())
        print("Directon: ", self.getDirection())
        print("Ammunition Level: ", self.getAmmunitionLevel())
        print("\n\n")

main()  