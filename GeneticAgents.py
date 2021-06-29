from game import Agent, Directions
import global_values

class GeneticAgent(Agent):
    "An agent that goes West until it can't."
    
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print(global_values.strategy)
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Going West.")
            return Directions.STOP