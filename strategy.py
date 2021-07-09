from game import Directions

class Strategy:
  def getDirectionOrder(self, state):
    values = [v.getValue(state) for v in self.values]
    return [x for _,x in sorted(zip(values, self.directions), reverse=True)]

  def __init__(self, values):
    self.values = values
    self.directions = [Directions.EAST, Directions.SOUTH, Directions.WEST, Directions.NORTH, Directions.STOP]