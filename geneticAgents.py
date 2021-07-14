import globalValues
from game import Agent

class GeneticAgent(Agent):
    "An agent that is guided by the globalValues.strategy tree."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        directionOrder = globalValues.strategy.getDirectionOrder(state)

        for d in directionOrder:
          if d in state.getLegalPacmanActions():
            globalValues.strategy.setLastTakenDirection(d)
            return d