from strategy import Strategy
import operators
import random
import values
from strategy import Strategy

def generateStrategy():
  values = []
  for _ in range(5):
    values.append(generateValueTree())

  return Strategy(values)

def generateValueTree(level=1):
  operator = random.random() < (0.95 ** (level - 1))

  if operator:
    firstValue = generateValueTree(level + 1)
    secondValue = generateValueTree(level + 1)
    return operators.getRandomOperator(firstValue, secondValue)

  return values.getRandomValue()