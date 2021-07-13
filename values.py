import random
import utils
from game import Directions

class Value:
  def getValue(self, state, cache={}, lastTakenDirection=None):
    "Should return a value to be used for a strategy"
    pass

  def __repr__(self):
    return self.__class__.__name__ + "()"

class UnedibleGhostsQuantity(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getUnedibleGhostsQuantity(state)

    return cache[name]

class ClosestUnedibleGhostDistance(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestUnedibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestUnedibleGhostX(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestUnedibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestUnedibleGhostY(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestUnedibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class EdibleGhostsQuantity(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getEdibleGhostsQuantity(state)

    return cache[name]

class ClosestEdibleGhostDistance(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestEdibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestEdibleGhostX(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestEdibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestEdibleGhostY(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestEdibleGhostData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class FoodQuantity(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getFoodQuantity(state)

    return cache[name]

class ClosestFoodDistance(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestFoodData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestFoodX(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestFoodData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestFoodY(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestFoodData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class CapsulesQuantity(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getCapsulesQuantity(state)

    return cache[name]

class ClosestCapsuleDistance(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestCapsuleData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[0]

    return cache[name]

class ClosestCapsuleX(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestCapsuleData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[1]

    return cache[name]

class ClosestCapsuleY(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      data = utils.getClosestCapsuleData(state)
      if not data:
        cache[name] = -1.0
      else:
        cache[name] = data[2]

    return cache[name]

class PacmanX(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getPacmanPosition(state)[0]

    return cache[name]

class PacmanY(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getPacmanPosition(state)[1]

    return cache[name]

class Score(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    name = type(self).__name__
    if name not in cache:
      cache[name] = utils.getScore(state)

    return cache[name]

class LastGoneEast(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    return 1.0 if lastTakenDirection == Directions.EAST else 0.0

class LastGoneWest(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    return 1.0 if lastTakenDirection == Directions.WEST else 0.0

class LastGoneNorth(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    return 1.0 if lastTakenDirection == Directions.NORTH else 0.0

class LastGoneSouth(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
    return 1.0 if lastTakenDirection == Directions.SOUTH else 0.0

class Constant0(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return 0.0

class Constant0_1(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return 0.1

class Constant0_5(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return 0.5

class Constant1(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return 1.0

class Constant2(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return 2.0

class Constant10(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return 10.0

class Constant_1(Value):
  def getValue(self, state, cache={}, lastTakenDirection=None):
      return -1.0

values = (UnedibleGhostsQuantity, ClosestUnedibleGhostDistance, ClosestUnedibleGhostX, ClosestUnedibleGhostY, EdibleGhostsQuantity, ClosestEdibleGhostDistance, ClosestEdibleGhostX, ClosestEdibleGhostY, FoodQuantity, ClosestFoodDistance, ClosestFoodX, ClosestFoodY, CapsulesQuantity, ClosestCapsuleDistance, ClosestCapsuleX, ClosestCapsuleY, PacmanX, PacmanY, LastGoneEast, LastGoneWest, LastGoneNorth, LastGoneSouth, Constant0, Constant0_1, Constant0_5, Constant1, Constant2, Constant10, Constant_1)

def getRandomValue() -> Value:
  return random.choice(values)()