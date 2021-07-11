import random
from values import Value

class Operator(Value):
  def __init__(self, firstValue, secondValue):
      self.firstValue = firstValue
      self.secondValue = secondValue

  def __repr__(self):
    return(self.__class__.__name__ + "(%s, %s)" % (self.firstValue.__repr__(), self.secondValue.__repr__()))

class Subtraction(Operator):
  def getValue(self, state, cache={}):
    return self.firstValue.getValue(state, cache) - self.secondValue.getValue(state, cache)

class Addition(Operator):
  def getValue(self, state, cache={}):
    return self.firstValue.getValue(state, cache) + self.secondValue.getValue(state, cache)

class Multiplication(Operator):
  def getValue(self, state, cache={}):
    return self.firstValue.getValue(state, cache) * self.secondValue.getValue(state, cache)

class Division(Operator):
  def getValue(self, state, cache={}):
    sv = self.secondValue.getValue(state, cache)
    if sv == 0.0:
      return 0.0

    return self.firstValue.getValue(state, cache) / sv

class Minimum(Operator):
  def getValue(self, state, cache={}):
    return min(self.firstValue.getValue(state, cache), self.secondValue.getValue(state, cache))

class Maximum(Operator):
  def getValue(self, state, cache={}):
    return max(self.firstValue.getValue(state, cache), self.secondValue.getValue(state, cache))

operators = (Subtraction, Addition, Multiplication, Division, Minimum, Maximum)

def getRandomOperator(firstValue, secondValue) -> Operator:
  return random.choice(operators)(firstValue, secondValue)