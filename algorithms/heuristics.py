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
    # Sacamos la posición actual y la cuadrícula de sobrevivientes del estado
    (pos, survivors_grid) = state

    hinfo = problem.heuristicInfo

    # Preparamos los diccionarios para guardar cálculos y no repetirlos
    if "dist_cache" not in hinfo:
        hinfo["dist_cache"] = {}
    if "mst_cache" not in hinfo:
        hinfo["mst_cache"] = {}
    # Buscamos el costo mínimo de moverse en el mapa (una sola vez)
    if "min_step_cost" not in hinfo:
        min_cost = float("inf")
        walls = problem.walls
        for x in range(walls.width):
            for y in range(walls.height):
                if not walls[x][y]:
                    c = problem.startingMissionState.getTerrainCost(x, y)
                    if c < min_cost:
                        min_cost = c
        hinfo["min_step_cost"] = min_cost if min_cost != float("inf") else 1

    dist_cache = hinfo["dist_cache"]
    mst_cache  = hinfo["mst_cache"]
    min_step_cost = hinfo["min_step_cost"]

    # Obtenemos la lista de posiciones donde hay sobrevivientes
    survivors = survivors_grid.asList()

    # Si no quedan sobrevivientes, ya terminamos
    if not survivors:
        return 0

    def manhattan(a, b):
        # Usamos una clave ordenada para no calcular la misma distancia dos veces
        key = (a, b) if a <= b else (b, a)
        if key not in dist_cache:
            dist_cache[key] = abs(a[0] - b[0]) + abs(a[1] - b[1])
        return dist_cache[key]

    # Distancia al sobreviviente más cercano desde donde estamos
    min_to_nearest = min(manhattan(pos, s) for s in survivors)

    # Si solo hay uno, con esa distancia alcanza
    if len(survivors) == 1:
        return min_to_nearest * min_step_cost

    # Calculamos el árbol de expansión mínima (MST) entre todos los sobrevivientes
    # Esto nos da una estimación del recorrido mínimo para visitarlos a todos
    surv_set = frozenset(survivors)
    if surv_set not in mst_cache:
        points = list(surv_set)
        # Empezamos desde el primer punto; los demás arrancan con distancia infinita
        key_dist = {v: float("inf") for v in points}
        key_dist[points[0]] = 0
        in_tree = set()
        mst_cost = 0

        for _ in range(len(points)):
            # Tomamos el punto más barato que aún no está en el árbol
            u = min((v for v in points if v not in in_tree), key=lambda v: key_dist[v])
            in_tree.add(u)
            mst_cost += key_dist[u]
            # Actualizamos las distancias de los puntos vecinos
            for v in points:
                if v not in in_tree:
                    d = manhattan(u, v)
                    if d < key_dist[v]:
                        key_dist[v] = d

        mst_cache[surv_set] = mst_cost

    mst_cost = mst_cache[surv_set]

    # La heurística es: llegar al más cercano + recorrer todos los demás
    return (min_to_nearest + mst_cost) * min_step_cost