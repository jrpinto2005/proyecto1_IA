from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    from algorithms.utils import Stack
    frontier = Stack()
    visitados = set()
    
    estado_incio = problem.getStartState()
    frontier.push((estado_incio, []))
    
    while not frontier.isEmpty():
        estado, acciones = frontier.pop()
        
        if estado in visitados:
            continue
        visitados.add(estado)
        
        if problem.isGoalState(estado):
            return acciones
        
        for siguiente, accion, costo, in problem.getSuccessors(estado):
            if siguiente not in visitados:
                frontier.push((siguiente, acciones +[accion]))
    return []

def breadthFirstSearch(problem: SearchProblem):
    from algorithms.utils import Queue
    
    frontier = Queue()
    visitados = set()
    
    estado_inicio = problem.getStartState()
    frontier.push((estado_inicio, []))
    visitados.add(estado_inicio)

    while not frontier.isEmpty():
        estado, acciones = frontier.pop()

        if problem.isGoalState(estado):
            return acciones

        for siguiente, accion, costo in problem.getSuccessors(estado):
            if siguiente not in visitados:
                visitados.add(siguiente)
                frontier.push((siguiente, acciones + [accion]))
    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
