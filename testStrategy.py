import globalValues
from values import UnedibleGhostsQuantity, ClosestUnedibleGhostDistance, ClosestUnedibleGhostX, ClosestUnedibleGhostY, EdibleGhostsQuantity, ClosestEdibleGhostDistance, ClosestEdibleGhostX, ClosestEdibleGhostY, FoodQuantity, ClosestFoodDistance, ClosestFoodX, ClosestFoodY, CapsulesQuantity, ClosestCapsuleDistance, ClosestCapsuleX, ClosestCapsuleY, PacmanX, PacmanY, Constant0, Constant0_1, Constant1, Constant10, Constant_1
from operators import Subtraction, Addition, Multiplication, Division, Minimum, Maximum
from strategy import Strategy
import pacman

globalValues.strategy = Strategy([Multiplication(ClosestCapsuleDistance(), Subtraction(Addition(Subtraction(Maximum(Subtraction(Multiplication(ClosestUnedibleGhostY(), ClosestUnedibleGhostDistance()), ClosestUnedibleGhostDistance()), CapsulesQuantity()), Addition(ClosestCapsuleY(), Maximum(Subtraction(ClosestCapsuleY(), PacmanX()), Maximum(Addition(Division(EdibleGhostsQuantity(), Minimum(Subtraction(Addition(ClosestUnedibleGhostDistance(), ClosestFoodY()), UnedibleGhostsQuantity()), Constant10())), ClosestCapsuleDistance()), Addition(Minimum(Subtraction(Division(ClosestEdibleGhostX(), PacmanY()), ClosestCapsuleX()), Maximum(ClosestFoodX(), ClosestEdibleGhostDistance())), PacmanY()))))), Maximum(Subtraction(Maximum(ClosestEdibleGhostDistance(), PacmanY()), Subtraction(EdibleGhostsQuantity(), Constant0_1())), ClosestUnedibleGhostDistance())), PacmanY())), Division(Minimum(Minimum(Addition(Subtraction(Maximum(Addition(Minimum(ClosestUnedibleGhostDistance(), ClosestCapsuleY()), Multiplication(ClosestUnedibleGhostY(), Maximum(ClosestFoodY(), ClosestUnedibleGhostY()))), Addition(ClosestEdibleGhostDistance(), Addition(Maximum(Maximum(Division(ClosestEdibleGhostX(), Maximum(ClosestCapsuleDistance(), PacmanY())), Minimum(Maximum(ClosestEdibleGhostX(), ClosestFoodY()), Constant_1())), Constant10()), PacmanX()))), Subtraction(Constant1(), PacmanY())), Subtraction(Subtraction(Constant10(), Subtraction(FoodQuantity(), ClosestEdibleGhostX())), EdibleGhostsQuantity())), Multiplication(Addition(Multiplication(Multiplication(ClosestUnedibleGhostDistance(), Multiplication(Division(Constant0_1(), UnedibleGhostsQuantity()), CapsulesQuantity())), PacmanX()), Division(ClosestFoodY(), Subtraction(Minimum(Subtraction(ClosestUnedibleGhostY(), ClosestEdibleGhostY()), Division(PacmanX(), ClosestUnedibleGhostDistance())), Division(ClosestFoodY(), Addition(Subtraction(ClosestUnedibleGhostX(), ClosestCapsuleY()), Constant1()))))), Addition(Subtraction(PacmanX(), Minimum(Maximum(ClosestCapsuleX(), PacmanY()), ClosestUnedibleGhostX())), ClosestUnedibleGhostDistance()))), Maximum(Division(Minimum(Constant1(), UnedibleGhostsQuantity()), Maximum(Constant1(), Multiplication(ClosestEdibleGhostX(), Subtraction(Constant10(), Constant10())))), UnedibleGhostsQuantity())), Division(Division(Minimum(Division(ClosestCapsuleX(), ClosestFoodDistance()), Division(ClosestUnedibleGhostDistance(), ClosestUnedibleGhostY())), Addition(Subtraction(ClosestCapsuleY(), Addition(EdibleGhostsQuantity(), ClosestCapsuleDistance())), Maximum(Division(Multiplication(Subtraction(Maximum(Minimum(ClosestEdibleGhostDistance(), Subtraction(Division(Minimum(ClosestCapsuleY(), Constant_1()), ClosestCapsuleDistance()), Division(Constant_1(), Minimum(ClosestUnedibleGhostX(), ClosestCapsuleX())))), EdibleGhostsQuantity()), ClosestFoodX()), Maximum(ClosestEdibleGhostY(), Addition(Division(ClosestUnedibleGhostY(), ClosestUnedibleGhostX()), ClosestEdibleGhostX()))), Minimum(Constant0_1(), PacmanX())), Addition(Constant10(), Maximum(ClosestCapsuleX(), Minimum(FoodQuantity(), ClosestUnedibleGhostY())))))), FoodQuantity())), Division(ClosestEdibleGhostY(), Maximum(Constant10(), Addition(Division(EdibleGhostsQuantity(), Multiplication(EdibleGhostsQuantity(), Maximum(ClosestUnedibleGhostY(), Maximum(FoodQuantity(), Maximum(FoodQuantity(), Constant10()))))), Maximum(Subtraction(Constant0(), Multiplication(Division(Constant0(), Addition(ClosestCapsuleY(), Minimum(Maximum(Constant10(), Addition(Multiplication(ClosestUnedibleGhostX(), Addition(PacmanY(), ClosestUnedibleGhostDistance())), ClosestFoodX())), ClosestFoodX()))), Multiplication(ClosestFoodDistance(), Addition(Maximum(CapsulesQuantity(), Maximum(Multiplication(Subtraction(Subtraction(Addition(Addition(Constant_1(), FoodQuantity()), ClosestFoodY()), Minimum(Constant_1(), ClosestCapsuleDistance())), Multiplication(Addition(Constant_1(), Division(ClosestCapsuleY(), EdibleGhostsQuantity())), Addition(ClosestFoodY(), CapsulesQuantity()))), Division(ClosestCapsuleY(), ClosestEdibleGhostX())), Multiplication(ClosestEdibleGhostY(), ClosestUnedibleGhostX()))), Maximum(Constant_1(), UnedibleGhostsQuantity()))))), Multiplication(Multiplication(Subtraction(ClosestFoodX(), Addition(UnedibleGhostsQuantity(), Multiplication(Multiplication(ClosestFoodDistance(), Division(Multiplication(Subtraction(ClosestEdibleGhostY(), Constant_1()), CapsulesQuantity()), EdibleGhostsQuantity())), ClosestCapsuleY()))), Minimum(ClosestEdibleGhostY(), Constant0_1())), CapsulesQuantity()))))), Division(Minimum(Division(Minimum(ClosestUnedibleGhostY(), Multiplication(Subtraction(ClosestFoodDistance(), Maximum(Addition(Maximum(ClosestCapsuleY(), Addition(Multiplication(ClosestUnedibleGhostY(), ClosestFoodY()), Division(Maximum(Constant0_1(), ClosestCapsuleY()), Constant0_1()))), Minimum(ClosestCapsuleX(), Division(ClosestCapsuleX(), Multiplication(UnedibleGhostsQuantity(), Division(Constant0_1(), PacmanX()))))), Addition(Addition(Constant0_1(), Constant1()), ClosestEdibleGhostY()))), Subtraction(Subtraction(Maximum(Subtraction(Addition(ClosestUnedibleGhostY(), Addition(ClosestFoodY(), ClosestUnedibleGhostX())), ClosestCapsuleX()), Constant0()), Constant1()), Subtraction(Addition(Minimum(ClosestEdibleGhostY(), Division(Constant1(), CapsulesQuantity())), CapsulesQuantity()), Division(Division(Constant1(), ClosestEdibleGhostY()), Minimum(Subtraction(Multiplication(Maximum(ClosestFoodY(), ClosestFoodX()), Addition(FoodQuantity(), Division(Maximum(Constant0(), Minimum(Constant10(), UnedibleGhostsQuantity())), Minimum(ClosestCapsuleDistance(), Constant10())))), Subtraction(ClosestCapsuleX(), Division(ClosestUnedibleGhostY(), Multiplication(FoodQuantity(), Addition(ClosestCapsuleX(), ClosestFoodDistance()))))), CapsulesQuantity())))))), Constant0_1()), Multiplication(EdibleGhostsQuantity(), Maximum(Multiplication(ClosestEdibleGhostX(), CapsulesQuantity()), Division(Addition(Maximum(CapsulesQuantity(), ClosestUnedibleGhostDistance()), ClosestFoodDistance()), Constant10())))), Maximum(Subtraction(Multiplication(Addition(Subtraction(ClosestEdibleGhostDistance(), Maximum(Addition(Minimum(ClosestCapsuleX(), ClosestFoodY()), Maximum(UnedibleGhostsQuantity(), ClosestUnedibleGhostY())), Minimum(ClosestFoodX(), Subtraction(ClosestFoodX(), Constant_1())))), Maximum(Division(ClosestFoodDistance(), Constant10()), ClosestUnedibleGhostX())), ClosestFoodY()), Multiplication(ClosestEdibleGhostX(), Multiplication(ClosestFoodY(), Constant10()))), Addition(Minimum(Subtraction(ClosestCapsuleDistance(), ClosestUnedibleGhostX()), Subtraction(Constant_1(), ClosestCapsuleDistance())), Maximum(Addition(Subtraction(ClosestEdibleGhostDistance(), Division(ClosestFoodDistance(), ClosestUnedibleGhostDistance())), Addition(ClosestCapsuleY(), Addition(ClosestFoodX(), Multiplication(Constant0_1(), Division(ClosestEdibleGhostDistance(), Constant1()))))), ClosestCapsuleY()))))]) # update here
layout = "originalClassic" # update here
args = pacman.readCommand(["-l", layout, "-p", "GeneticAgent", "-n", "5"])
games = pacman.runGames(**args)