from algorithms.problems import SearchProblem
import algorithms.utils as utils
from algorithms.utils import PriorityQueue
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
    frontera = PriorityQueue()
    visitados = set()
    
    estado_incial = problem.getStartState()
    frontera.push((estado_incial, [], 0), 0)
    
    while not frontera.isEmpty():
        estado, acciones, costo_total = frontera.pop()
        
        if estado in visitados:
            continue
        visitados.add(estado)
        
        if problem.isGoalState(estado):
            return acciones
        
        for siguiente, accion, costo, in problem.getSuccessors(estado):
            if siguiente not in visitados:
                nuevo_costo = costo_total + costo
                frontera.update((siguiente, acciones + [accion], nuevo_costo), nuevo_costo)
    return []

def aStarSearch(problem, heuristic):
    """
    Implementación de A* basada directamente en Uniform Cost Search.
    La prioridad en la frontera es f(n) = g(n) + h(n).
    """

    estado_inicial = problem.getStartState()

    frontera = PriorityQueue()
    visitados = set()

    # (estado, acciones, costo_real)
    costo_inicial = 0
    frontera.push((estado_inicial, [], costo_inicial),costo_inicial + heuristic(estado_inicial, problem))

    costos = {estado_inicial: 0}

    while not frontera.isEmpty():
        estado, acciones, costo_real = frontera.pop()

        if estado in visitados:
            continue
        visitados.add(estado)

        if problem.isGoalState(estado):
            return acciones

        for siguiente, accion, costo_paso in problem.getSuccessors(estado):

            nuevo_costo_real = costo_real + costo_paso

            if siguiente not in costos or nuevo_costo_real < costos[siguiente]:
                costos[siguiente] = nuevo_costo_real
                nuevas_acciones = acciones + [accion]

                prioridad = nuevo_costo_real + heuristic(siguiente, problem)

                frontera.push((siguiente, nuevas_acciones, nuevo_costo_real),prioridad)

    return []
# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
