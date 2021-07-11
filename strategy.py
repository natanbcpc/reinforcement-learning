from game import Directions

class Strategy:
  def getDirectionOrder(self, state):
    cache = {}
    values = [v.getValue(state, cache) for v in self.values]
    return [x for _,x in sorted(zip(values, self.directions), reverse=True)]

  def __init__(self, values):
    self.values = values
    self.directions = [Directions.EAST, Directions.SOUTH, Directions.WEST, Directions.NORTH] #, Directions.STOP]

  def __repr__(self):
    return self.__class__.__name__ + "(%s)" % (self.values.__repr__())