from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem
import math

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    Manhattan distance heuristic that works for both Simple and Multi survivor problems.
    """
    x, y = state
    gx, gy = problem.goal
    return abs(x - gx) + abs(y - gy)

def euclideanHeuristic(state, problem):
    """
    Euclidean distance heuristic for Simple and Multi survivor problems.
    """
    x, y = state
    gx, gy = problem.goal
    return math.sqrt((x - gx)**2 + (y - gy)**2)

def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    utils.raiseNotDefined()
