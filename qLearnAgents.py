import game
from game import Agent
from pacman import Directions
import util

def QLearnAgent(Agent):

    learningRate = 0.2,
    explorationRate = 0.05,
    discountFactor = 0.8,
    numTraining = 10

    episodesCount = 0
    q_value = util.Counter()
    score = 0
    lastState = []
    lastAction = []