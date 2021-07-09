from utils import Utils

class Value:
  def getValue(self, state):
    "Should return a value to be used for a strategy"
    pass

  def __init__(self):
    self.utils = Utils()

class PacmanX(Value):
  def getValue(self, state):
    return self.utils.getPacmanPosition(state)[0]

class PacmanY(Value):
  def getValue(self, state):
    return self.utils.getPacmanPosition(state)[0]

class ClosestFoodDistance(Value):
  def getValue(self, state):
    return self.utils.getClosestFoodData(state)[0]

class ClosestFoodX(Value):
  def getValue(self, state):
    return self.utils.getClosestFoodData(state)[1]

class ClosestFoodY(Value):
  def getValue(self, state):
    return self.utils.getClosestFoodData(state)[2]

class Constant0(Value):
  def getValue(self, state):
      return 0.0

class Constant0_1(Value):
  def getValue(self, state):
      return 0.1

class Constant1(Value):
  def getValue(self, state):
      return 1.0

class Constant10(Value):
  def getValue(self, state):
      return 10.0

class Constant_1(Value):
  def getValue(self, state):
      return -1.0
