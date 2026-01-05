import json as j
class SurvivalGame:
    
    def __init__(self,n):
        
        self.name = n
        self.day = 0
        self.hunger = "Satisfied"
        self.energy = "Very High"
        self.energyLevels = {1:"Very High",2:"High",3:"Medium",4:"Low",5:"Very Low",6:"Zero"}
        self.hungerLevels = {1:"Satisfied",2:"Slightly Hungry",3:"Hungry",4:"Very Hungry",5:"Starving"}
        self.actions = {"search_food": {"energy": "decrease","hunger": "decrease","logic": "Energy spent searching, hunger reduced after eating food"},
                        "rest": {"energy": "increase","hunger": "increase","logic": "Body recovers, but hunger builds"},
                        "explore": {"energy": "decrease","hunger": "increase","logic": "Long travel without guaranteed food"},
                        "do_nothing": {"energy": "decrease","hunger": "increase","logic": "Time passes with no benefit"}}        
                    
    def runGame(self):
        
        # file-handling & storing every player data
        try:
            with open("SurvivalGame.json","r+")as jfo:
                
                # reading data
                data = j.load(jfo)
            
                if data == {}:
                    po = [{"players":{self.name:self.day}}]
                    j.dump(po,jfo)
                    
        except(FileNotFoundError,j.JSONDecodeError):
            with open("SurvivalGame.json","w+")as jfo:
                po = [{"players":{self.name:self.day}}]
                j.dump(po,jfo)
                jfo.seek(0)
                data = j.load(jfo)
                
        # showing warning status to player
        print("energy becomes zero or hunger becomes starving then you die!")
        
        def hungerIncrement():
            # hunger increment
            if self.hunger != "Starving":
                
                for level in self.hungerLevels:
                    
                    if self.hunger == self.hungerLevels[level]:
                        
                        self.hunger = self.hungerLevels[level + 1]
                        
                        break
        
        # day-by-day survival loop
        while not (self.energy == "Zero" or self.hunger == "Starving"):
            
            # showing current status
            print(f"day {self.day}")
            print(f"energy: {self.energy}")
            print(f"hungry: {self.hunger}")
                
            # player chosing choice           
            print("choose choise in this options only")
            print("search_food","rest","explore","do_nothing")
            choice = input("enter your choise:\n")
            
            # choice is choosing wrong , then re-ask choice 
            while choice not in ("search_food","rest","explore","do_nothing"):
                choice = input("enter your choise:\n")
            
            print(self.actions[choice]["logic"])
            action = self.actions[choice]
            
            energyIncrementOrDecrement = action["energy"]
            hungerIncrementOrDecrement = action["hunger"] 
            
            # energy increase or decrease based on player choice
            if energyIncrementOrDecrement == "decrease":
                
                # energy decrement
                if self.energy != "Zero": 
                    
                    for level in self.energyLevels:
                        
                        if self.energy == self.energyLevels[level]:
                            
                            self.energy = self.energyLevels[level + 1]
                            
                            break
            else:
                
                # energy increment
                if self.energy != "Very High":
                    
                    for level in self.energyLevels:
                        
                        if self.energy == self.energyLevels[level]:
                            
                            self.energy = self.energyLevels[level - 1]
                            
                            break
            
            # hunger increase or decrease based on player choice
            if hungerIncrementOrDecrement == "decrease":
                
                # hunger decrement
                if self.hunger != "Satisfied":
                    
                    for level in self.hungerLevels:
                        
                        if self.hunger == self.hungerLevels[level]:
                            
                            self.hunger = self.hungerLevels[level - 1]
                            
                            break
            
            else:
                hungerIncrement()
            
            # action is search food dont consider
            if choice != "search_food":
                hungerIncrement()
                
            self.day += 1
                
        else:
            print(f"Game Over\nYou Survived {self.day} days")
            
            # updating json
            with open("SurvivalGame.json","w") as jfo:          
                data[0]["players"][self.name] = self.day
                j.dump(data,jfo)
              
n = input("enter your name:\n")
obj = SurvivalGame(n)
obj.runGame()