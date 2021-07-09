from values import Value

class Operator(Value):
  def __init__(self, firstValue, secondValue):
      self.firstValue = firstValue
      self.secondValue = secondValue

class Subtraction(Operator):
  def getValue(self, state):
    return self.firstValue.getValue(state) - self.secondValue.getValue(state)

class Addition(Operator):
  def getValue(self, state):
    return self.firstValue.getValue(state) + self.secondValue.getValue(state)

class Multiplication(Operator):
  def getValue(self, state):
    return self.firstValue.getValue(state) * self.secondValue.getValue(state)

class Division(Operator):
  def getValue(self, state):
    sv = self.secondValue.getValue(state)
    if sv == 0.0:
      return 0.0

    return self.firstValue.getValue(state) / sv

class Minimum(Operator):
  def getValue(self, state):
    return min(self.firstValue.getValue(state), self.secondValue.getValue(state))

class Maximum(Operator):
  def getValue(self, state):
    return max(self.firstValue.getValue(state), self.secondValue.getValue(state))