from game import Directions

class Strategy:
  def getDirectionOrder(self, state):
    cache = {}
    votes = [0] * 4
    for valuesTreesLine in self.valuesTrees:
      values = [v.getValue(state, cache, self.lastTakenDirection) for v in valuesTreesLine]
      votes[values.index(max(values))] += 1
    return [x for _,x in sorted(zip(votes, self.directions), reverse=True)]

  def setLastTakenDirection(self, direction):
    self.lastTakenDirection = direction

  def __init__(self, valuesTrees):
    self.valuesTrees = valuesTrees
    self.directions = [Directions.EAST, Directions.SOUTH, Directions.WEST, Directions.NORTH]
    self.lastTakenDirection = None

  def __repr__(self):
    return self.__class__.__name__ + "(%s)" % (self.valuesTrees.__repr__())