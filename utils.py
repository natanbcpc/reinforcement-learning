import numpy as np
from game import Directions

def isFree(state, x, y, considerGhosts):
  hasWall = state.hasWall(x, y)
  hasGhost = False

  if considerGhosts:
      hasGhost = (x, y) in state.getGhostPositions()

  return not (hasWall or hasGhost)

def getNeighbors(state, x, y, considerGhosts):
  neighbors = []
  if isFree(state, x+1, y, considerGhosts):
    neighbors.append((x+1, y))
  if isFree(state, x-1, y, considerGhosts):
    neighbors.append((x-1, y))
  if isFree(state, x, y+1, considerGhosts):
    neighbors.append((x, y+1))
  if isFree(state, x, y-1, considerGhosts):
    neighbors.append((x, y-1))
  return neighbors

def findDijkstraDistanceIfLessThan(state, x1, y1, x2, y2, maxDistance, considerGhosts=False):
  distance = {}
  queue = {}

  for i in range(state.getWalls().width):
    for j in range(state.getWalls().height):
      if isFree(state, i, j, considerGhosts):
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

    for nx, ny in getNeighbors(state, x, y, considerGhosts):
      if (nx, ny) in queue:
        newDistance = distance[(x, y)] + 1
        if newDistance < distance[(nx, ny)]:
          queue[(nx, ny)] = newDistance
          distance[(nx, ny)] = newDistance

  return distance[(x2, y2)]

def findBestDistanceAndPos(state, objects):
  px, py = state.getPacmanPosition()
  currentMin = np.inf
  currentMinX = -1
  currentMinY = -1

  estimation = [abs(px - x) + abs(py - y) for x, y in objects]
  estimationOrderedObjects = [o for _,o in sorted(zip(estimation, objects))]

  for x, y in estimationOrderedObjects:
    if abs(px - x) + abs(py - y) > currentMin:
      return (currentMin, currentMinX, currentMinY)

    distance = findDijkstraDistanceIfLessThan(state, px, py, round(x), round(y), currentMin)
    if distance < currentMin:
      currentMin = distance
      currentMinX = x
      currentMinY = y

  return (currentMin, currentMinX, currentMinY)

def getUnedibleGhostPositions(state):
  return [g.getPosition() for g in state.getGhostStates() if g.scaredTimer <= 0]

def getEdibleGhostPositions(state):
  return [g.getPosition() for g in state.getGhostStates() if g.scaredTimer > 0]

def getFoodPositions(state):
  foodPositions = []
  for i in range(state.getFood().width):
    for j in range(state.getFood().height):
      if state.getFood()[i][j]:
        foodPositions.append((i, j))
  return foodPositions

def getUnedibleGhostsQuantity(state):
  return len(getUnedibleGhostPositions(state))

def getEdibleGhostsQuantity(state):
  return len(getEdibleGhostPositions(state))

def getFoodQuantity(state):
  return state.getNumFood()

def getCapsulesQuantity(state):
  return len(state.getCapsules())

def getClosestUnedibleGhostData(state):
  unedibleGhostPositions = getUnedibleGhostPositions(state)

  if not unedibleGhostPositions:
    return None

  return findBestDistanceAndPos(state, unedibleGhostPositions)

def getClosestEdibleGhostData(state):
  edibleGhostPositions = getEdibleGhostPositions(state)

  if not edibleGhostPositions:
    return None

  return findBestDistanceAndPos(state, edibleGhostPositions)

def getClosestFoodData(state):
  foodPositions = getFoodPositions(state)

  if not foodPositions:
    return None

  return findBestDistanceAndPos(state, foodPositions)

def getClosestCapsuleData(state):
  capsules = state.getCapsules()

  if not capsules:
    return None

  return findBestDistanceAndPos(state, capsules)

def getPacmanPosition(state):
  return state.getPacmanPosition()

def getScore(state):
  return state.getScore()

def getOppositeDirection(direction):
  if direction == Directions.EAST:
    return Directions.WEST
  elif direction == Directions.WEST:
    return Directions.EAST
  elif direction == Directions.NORTH:
    return Directions.SOUTH
  elif direction == Directions.SOUTH:
    return Directions.NORTH