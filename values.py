import random
from utils import Utils

class Value:
  def getValue(self, state, cache):
    "Should return a value to be used for a strategy"
    pass

  def __init__(self):
    self.utils = Utils()

class UnedibleGhostsQuantity(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      cache[name] = self.utils.getUnedibleGhostsQuantity(state)

    return cache[name]

class ClosestUnedibleGhostDistance(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestUnedibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestUnedibleGhostX(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestUnedibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestUnedibleGhostY(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestUnedibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class EdibleGhostsQuantity(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      cache[name] = self.utils.getEdibleGhostsQuantity(state)

    return cache[name]

class ClosestEdibleGhostDistance(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestEdibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestEdibleGhostX(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestEdibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestEdibleGhostY(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestEdibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class FoodQuantity(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      cache[name] = self.utils.getFoodQuantity(state)

    return cache[name]

class ClosestFoodDistance(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestFoodData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestFoodX(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestFoodData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestFoodY(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestFoodData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class CapsulesQuantity(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      cache[name] = self.utils.getCapsulesQuantity(state)

    return cache[name]

class ClosestCapsuleDistance(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestCapsuleData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestCapsuleX(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestCapsuleData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestCapsuleY(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      data = self.utils.getClosestCapsuleData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class PacmanX(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      cache[name] = self.utils.getPacmanPosition(state)[0]

    return cache[name]

class PacmanY(Value):
  def getValue(self, state, cache):
    name = type(self).__name__
    if name not in cache:
      cache[name] = self.utils.getPacmanPosition(state)[1]

    return cache[name]

class Constant0(Value):
  def getValue(self, state, cache):
      return 0.0

class Constant0_1(Value):
  def getValue(self, state, cache):
      return 0.1

class Constant1(Value):
  def getValue(self, state, cache):
      return 1.0

class Constant10(Value):
  def getValue(self, state, cache):
      return 10.0

class Constant_1(Value):
  def getValue(self, state, cache):
      return -1.0

values = (UnedibleGhostsQuantity, ClosestUnedibleGhostDistance, ClosestUnedibleGhostX, ClosestUnedibleGhostY, EdibleGhostsQuantity, ClosestEdibleGhostDistance, ClosestEdibleGhostX, ClosestEdibleGhostY, FoodQuantity, ClosestFoodDistance, ClosestFoodX, ClosestFoodY, CapsulesQuantity, ClosestCapsuleDistance, ClosestCapsuleX, ClosestCapsuleY, PacmanX, PacmanY, Constant0, Constant0_1, Constant1, Constant10, Constant_1)

def getRandomValue() -> Value:
  return random.choice(values)()