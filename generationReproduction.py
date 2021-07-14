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
  valuesTrees = random.sample(firstStrategy.valuesTrees, round(len(firstStrategy.valuesTrees) / 2))
  valuesTrees += random.sample(secondStrategy.valuesTrees, round(len(secondStrategy.valuesTrees) / 2))
  return Strategy(valuesTrees)