import operators
import random
import strategyGenerator
from strategy import Strategy

def regenerate(strategy):
  a = random.randint(0, len(strategy.values) - 1)
  strategy.values[a] = strategyGenerator.generateValueTree()
  return strategy

def swap(strategy):
  a = random.randint(0, len(strategy.values) - 1)
  b = random.randint(0, len(strategy.values) - 1)
  aux = strategy.values[a]
  strategy.values[a] = strategy.values[b]
  strategy.values[b] = aux
  return Strategy(strategy.values)

def branchSwap(strategy):
  a = random.randint(0, len(strategy.values) - 1)
  b = random.randint(0, len(strategy.values) - 1)
  aux = strategy.values[a].firstValue
  strategy.values[a].firstValue = strategy.values[b].secondValue
  strategy.values[b].secondValue = aux
  return strategy

def mutate(strategy):
  return random.choice((regenerate, swap, branchSwap))(strategy)

def crossover(firstStrategy, secondStrategy):
  values = []
  for i in range(5):
    firstStrategyRoot = firstStrategy.values[i].__class__
    secondStrategyRoot = secondStrategy.values[i].__class__

    values.append(random.choice((firstStrategy.values[i], secondStrategy.values[i], firstStrategyRoot(firstStrategy.values[i].firstValue, secondStrategy.values[i].secondValue), secondStrategyRoot(secondStrategy.values[i].firstValue, firstStrategy.values[i].secondValue), operators.getRandomOperator(firstStrategy.values[i], secondStrategy.values[i]))))
  return Strategy(values)