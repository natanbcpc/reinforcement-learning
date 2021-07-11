import copy
import operators
import random
import strategyGenerator
from strategy import Strategy

def regenerate(strategy):
  newStrategy = copy.deepcopy(strategy)
  a = random.randint(0, len(newStrategy.values) - 1)
  newStrategy.values[a] = strategyGenerator.generateValueTree()
  return newStrategy

def swap(strategy):
  newStrategy = copy.deepcopy(strategy)
  a = random.randint(0, len(newStrategy.values) - 1)
  b = random.randint(0, len(newStrategy.values) - 1)
  aux = newStrategy.values[a]
  newStrategy.values[a] = newStrategy.values[b]
  newStrategy.values[b] = aux
  return newStrategy

def branchSwap(strategy):
  newStrategy = copy.deepcopy(strategy)
  a = random.randint(0, len(newStrategy.values) - 1)
  b = random.randint(0, len(newStrategy.values) - 1)
  aux = newStrategy.values[a].firstValue
  newStrategy.values[a].firstValue = newStrategy.values[b].secondValue
  newStrategy.values[b].secondValue = aux
  return newStrategy

def mutate(strategy):
  return random.choice((regenerate, swap, branchSwap))(strategy)

def crossover(firstStrategy, secondStrategy):
  firstStrategyCopy = copy.deepcopy(firstStrategy)
  secondStrategyCopy = copy.deepcopy(secondStrategy)
  values = []
  for i in range(len(firstStrategyCopy.values)):
    firstStrategyRoot = firstStrategyCopy.values[i].__class__
    secondStrategyRoot = secondStrategyCopy.values[i].__class__

    values.append(random.choice((firstStrategyCopy.values[i], secondStrategyCopy.values[i], firstStrategyRoot(firstStrategyCopy.values[i].firstValue, secondStrategyCopy.values[i].secondValue), secondStrategyRoot(secondStrategyCopy.values[i].firstValue, firstStrategyCopy.values[i].secondValue), operators.getRandomOperator(firstStrategyCopy.values[i], secondStrategyCopy.values[i]))))
  return Strategy(values)