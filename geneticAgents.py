from game import Agent, Directions
import globalValues
import numpy as np

class GeneticAgent(Agent):
    "An agent that is guided by the globalValues.strategy tree."

    def isFree(self, state, x, y, considerGhosts):
        hasWall = state.hasWall(x, y)
        hasGhost = False

        if considerGhosts:
            hasGhost = (x, y) in state.getGhostPositions()

        return not (hasWall or hasGhost)

    def getNeighbors(self, state, x, y, considerGhosts):
      neighbors = []
      if self.isFree(state, x+1, y, considerGhosts):
        neighbors.append((x+1, y))
      if self.isFree(state, x-1, y, considerGhosts):
        neighbors.append((x-1, y))
      if self.isFree(state, x, y+1, considerGhosts):
        neighbors.append((x, y+1))
      if self.isFree(state, x, y-1, considerGhosts):
        neighbors.append((x, y-1))
      return neighbors

    def findDijkstraDistanceIfLessThan(self, state, x1, y1, x2, y2, maxDistance, considerGhosts=False):
      distance = {}
      queue = {}

      for i in range(state.getWalls().width):
        for j in range(state.getWalls().height):
          if self.isFree(state, i, j, considerGhosts):
            distance[(i, j)] = np.inf
            queue[(i, j)] = np.inf

      distance[(x1, y1)] = 0
      queue[(x1, y1)] = 0

      while queue:
        x, y = min(queue, key=queue.get)
        d = queue.pop((x, y))
        if x == x2 and y == y2:
          return d
        if d >= maxDistance:
          return np.inf

        for nx, ny in self.getNeighbors(state, x, y, considerGhosts):
          if (nx, ny) in queue:
            newDistance = distance[(x, y)] + 1
            if newDistance < distance[(nx, ny)]:
              queue[(nx, ny)] = newDistance
              distance[(nx, ny)] = newDistance

      return distance[(x2, y2)]

    def findBestDistanceAndPos(self, state, objects):
      px, py = state.getPacmanPosition()
      currentMin = np.inf
      currentMinX = -1
      currentMinY = -1

      for x, y in objects:
        if abs(px - x) + abs(py - y) <= currentMin:
          distance = self.findDijkstraDistanceIfLessThan(state, px, py, x, y, currentMin)
          if distance < currentMin:
            currentMin = distance
            currentMinX = x
            currentMinY = y

      return (currentMin, currentMinX, currentMinY)

    def getUnedibleGhostPositions(self, state):
      return [g.getPosition() for g in state.getGhostStates() if g.scaredTimer <= 0]

    def getEdibleGhostPositions(self, state):
      return [g.getPosition() for g in state.getGhostStates() if g.scaredTimer > 0]

    def getFoodPositions(self, state):
      foodPositions = []
      for i in range(state.getFood().width):
        for j in range(state.getFood().height):
          if state.getFood()[i][j]:
            foodPositions.append((i, j))
      return foodPositions

    def getUnedibleGhostsQuantity(self, state):
      return len(self.getUnedibleGhostPositions(state))

    def getEdibleGhostsQuantity(self, state):
      return len(self.getEdibleGhostPositions(state))

    def getFoodQuantity(self, state):
      return state.getNumFood()

    def getCapsulesQuantity(self, state):
      return len(state.getCapsules())

    def getClosestUnedibleGhostData(self, state):
      unedibleGhostPositions = self.getUnedibleGhostPositions(state)

      if not unedibleGhostPositions:
        return None

      return self.findBestDistanceAndPos(state, unedibleGhostPositions)

    def getClosestEdibleGhostData(self, state):
      edibleGhostPositions = self.getEdibleGhostPositions(state)

      if not edibleGhostPositions:
        return None

      return self.findBestDistanceAndPos(state, edibleGhostPositions)

    def getClosestFoodData(self, state):
      foodPositions = self.getFoodPositions(state)

      if not foodPositions:
        return None

      return self.findBestDistanceAndPos(state, foodPositions)

    def getClosestCapsulesData(self, state):
      capsules = state.getCapsules()

      if not capsules:
        return None

      return self.findBestDistanceAndPos(state, capsules)

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        gx, gy = state.getGhostPositions()[0]
        print("Unedible ghost qty:", self.getUnedibleGhostsQuantity(state))
        print("Edible ghost qty:", self.getEdibleGhostsQuantity(state))
        print("Food qty:", self.getFoodQuantity(state))
        print("Capsule qty:", self.getCapsulesQuantity(state))
        print("Closest unedible ghost data:", self.getClosestUnedibleGhostData(state))
        print("Closest edible ghost data:", self.getClosestEdibleGhostData(state))
        print("Closest food data:", self.getClosestFoodData(state))
        print("Closest capsule data:", self.getClosestCapsulesData(state))
        print("Location: ", state.getPacmanPosition())
        if Directions.EAST in state.getLegalPacmanActions():
            return Directions.EAST
        else:
            return Directions.STOP