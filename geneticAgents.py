from game import Agent, Directions
import globalValues

class GeneticAgent(Agent):
    "An agent that is guided by the globalValues.strategy tree."

    def isFree(self, state, x, y, considerGhosts):
        hasWall = state.hasWall(x, y)
        hasGhost = False

        if considerGhosts:
            hasGhost = (x, y) in state.getGhostPositions()
        
        return not (hasWall or hasGhost)

    def findBestPath(self, state, x1, y1, x2, y2, path, currentMin=None, considerGhosts=False):
      path.append((x1, y1))

      if currentMin and len(path) >= currentMin:
        return (False, path)

      if x1 == x2 and y1 == y2:
        return (True, path)
      
      currentPath = None
      if self.isFree(state, x1+1, y1, considerGhosts) and (x1+1, y1) not in path:
        found, newPath = self.findBestPath(state, x1+1, y1, x2, y2, list(path), currentMin)
        if found and ((not currentMin) or (len(newPath) < currentMin)):
          currentMin = len(newPath)
          currentPath = newPath
      if self.isFree(state, x1-1, y1, considerGhosts) and (x1-1, y1) not in path:
        found, newPath = self.findBestPath(state, x1-1, y1, x2, y2, list(path), currentMin)
        if found and ((not currentMin) or (len(newPath) < currentMin)):
          currentMin = len(newPath)
          currentPath = newPath
      if self.isFree(state, x1, y1+1, considerGhosts) and (x1, y1+1) not in path:
        found, newPath = self.findBestPath(state, x1, y1+1, x2, y2, list(path), currentMin)
        if found and ((not currentMin) or (len(newPath) < currentMin)):
          currentMin = len(newPath)
          currentPath = newPath
      if self.isFree(state, x1, y1-1, considerGhosts) and (x1, y1-1) not in path:
        found, newPath = self.findBestPath(state, x1, y1-1, x2, y2, list(path), currentMin)
        if found and ((not currentMin) or (len(newPath) < currentMin)):
          currentMin = len(newPath)
          currentPath = newPath

      if currentPath:
        return (True, currentPath)

      return (False, path)

    def findDistance(self, state, x, y):
      px, py = state.getPacmanPosition()
      found, path = self.findBestPath(state, px, py, x, y, [])
      if not found:
        return -1
      
      print("Path:", path)
      return len(path) - 1
    
    def getClosestUnedibleGhostDistance(self, state):
      unedibleGhosts = [g for g in state.getGhostStates() if g.scaredTimer <= 0]

      if not unedibleGhosts:
        return -1

      unedibleGhostPositions = [g.getPosition() for g in unedibleGhosts]
      unedibleGhostDistances = [self.findDistance(state, x, y) for x, y in unedibleGhostPositions]
      print("Ghost position:", unedibleGhostPositions[unedibleGhostDistances.index(min(unedibleGhostDistances))])
      return min(unedibleGhostDistances)

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        gx, gy = state.getGhostPositions()[0]
        print("Closest unedible ghost distance:", self.getClosestUnedibleGhostDistance(state))
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP