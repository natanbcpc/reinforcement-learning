from strategy import Strategy
import operators
import random
import values
from strategy import Strategy

def generateStrategy(lines=1000):
  valuesTrees = []
  for i in range(lines):
    valuesTrees.append([])
    for _ in range(4):
      valuesTrees[i].append(generateValueTree())

  return Strategy(valuesTrees)

def generateValueTree(level=1):
  operator = random.random() < (0.5 ** (level - 1))

  if operator:
    firstValue = generateValueTree(level + 1)
    secondValue = generateValueTree(level + 1)
    return operators.getRandomOperator(firstValue, secondValue)

  return values.getRandomValue()