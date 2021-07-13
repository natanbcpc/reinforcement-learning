import random
import strategyGenerator
from strategy import Strategy

def addLine(strategy):
  valuesTrees = list(strategy.valuesTrees)
  for _ in range(50):
    line = []
    for _ in range(4):
      line.append(strategyGenerator.generateValueTree())
    valuesTrees.append(line)
  return Strategy(valuesTrees)

def removeLine(strategy):
  valuesTrees = list(strategy.valuesTrees)
  if len(valuesTrees) > 50:
    for _ in range(50):
      i = random.randint(0, len(valuesTrees) - 1)
      valuesTrees.pop(i)
  return Strategy(valuesTrees)

def mutate(strategy):
  return random.choice((addLine, removeLine))(strategy)

def crossover(firstStrategy, secondStrategy):
  valuesTrees = []
  shouldMantainLargerSize = bool(random.getrandbits(1))
  for i in range(max(len(firstStrategy.valuesTrees), len(secondStrategy.valuesTrees))):
    if i < len(firstStrategy.valuesTrees) and i < len(secondStrategy.valuesTrees):
      valuesTrees.append(random.choice((firstStrategy.valuesTrees[i], secondStrategy.valuesTrees[i])))
    elif not shouldMantainLargerSize:
      return Strategy(valuesTrees)
    elif i > len(firstStrategy.valuesTrees) - 1:
      valuesTrees.append(secondStrategy.valuesTrees[i])
    else:
      valuesTrees.append(firstStrategy.valuesTrees[i])
  return Strategy(valuesTrees)