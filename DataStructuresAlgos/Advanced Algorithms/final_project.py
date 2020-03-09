import numpy as np
from collections import deque
from heapq import heappush, heappop
from functools import total_ordering


######################### Attempt Two #########################


@total_ordering
class Intersect:
    def __init__(self, num, path_cost):
        self.num = num
        self.path_cost = path_cost
        self.heuristic = None
        self.total_cost = None
        self.prior_intersections = []

    def get_num(self):
        return self.num

    def get_path_cost(self):
        return self.path_cost

    def get_heuristic(self):
        return self.heuristic

    def set_heuristic(self, goal_cost):
        self.heuristic = goal_cost
        self.total_cost = self.path_cost + self.heuristic

    def get_total_cost(self):
        return self.total_cost

    def add_priors(self, priors):
        self.prior_intersections.extend(priors)
        self.total_cost = self.total_cost + sum(
            [i.get_total_cost() for i in self.prior_intersections]
        )

    def get_priors(self):
        if len(self.prior_intersections) == 0:
            return None
        else:
            return self.prior_intersections

    def __eq__(self, other):
        return self.total_cost == other

    def __lt__(self, other):
        return self.total_cost < other

    def __repr__(self):
        s = "\n==========\n"
        s += f"Intersect: {self.num}\n"
        s += f"Path cost: {self.path_cost}\n"
        s += f"Heuristic: {self.heuristic}\n"
        s += f"Total cost: {self.total_cost}\n"
        s += f"Priors: {[i.get_num() for i in self.prior_intersections]}"
        s += "=========="
        return s


def the_shortest_path(graph, start, goal):

    if start == goal:
        return [start]

    pqueue = []
    visited = []

    start_intersect = Intersect(start, 0)
    heappush(pqueue, start_intersect)
    current_intersect = start_intersect
    print(f"Start intersection: {start_intersect}")

    while len(pqueue) != 0:
        prior_intersect = current_intersect
        current_intersect = heappop(pqueue)
        print(f"Intersection to be expanded: {current_intersect}")
        intersection_costs = expand_intersect(
            graph, current_intersect.get_num(), goal, visited
        )
        print(f"Intersection costs: {intersection_costs}")
        current_intersect.add_priors(prior_intersect.get_priors())
        visited.append(current_intersect.get_num())
        print(f"Current visited: {[i for i in visited]}")
        for intersection in intersection_costs:
            heappush(pqueue, intersection)
        print(f"Pqueue length: {len(pqueue)}")


def expand_intersect(graph, int1, goal, visited):

    #     path_distances = {int2: calc_path_cost(graph, int1, int2) for int2 in graph.roads[int1]}
    intersects = [
        Intersect(int2, calc_path_cost(graph, int1, int2))
        for int2 in graph.roads[int1]
        if int2 not in visited
    ]  # A2

    # node_costs = []  # A2

    for intersect in intersects:
        goal_distance = estimate_goal_distance(graph, intersect.get_num(), goal)
        intersect.set_heuristic(goal_distance)

    return intersects


def estimate_heuristic(graph, intersection, goal):

    int_coords = graph.intersections[intersection]
    goal_coords = graph.intersections[goal]

    distance = calc_distance(int_coords, goal_coords)

    return distance


######################### Attempt One #########################


def shortest_path(graph, start, goal):
    print("shortest path called")
    start_intersection_coordinates = graph.intersections[start]
    print(f"starting intersection: {start}")
    print(f"starting intersection coordinates: {start_intersection_coordinates}")
    start_intersection_roads = graph.roads[start]
    print(f"starting intersection roads: {start_intersection_roads}")
    print(f"goal: {goal}")

    path = []
    visited = []
    path.append(start)
    visited.append(start)
    path_cost = 0

    frontier = calc_path_costs(graph, start, goal)

    frontier_min_int = None
    frontier_min_cost = np.inf
    cost_greater_min_int = None
    cost_greater_min_cost = np.inf

    current_intersection = start

    while current_intersection != goal:

        for intersect, cost in frontier.items():
            if (cost <= frontier_min_cost) & (intersect not in visited):
                frontier_min_int = intersect
                frontier_min_cost = cost
            else:
                cost_greater_min_int = intersect
                cost_greater_min_cost = cost

        if frontier_min_int:
            current_intersection = frontier_min_int
            current_intersection_cost = frontier_min_cost
        elif cost_greater_min_int is not None:
            #             print(f"cost greater min int: {cost_greater_min_int}")
            if frontier_min_cost <= cost_greater_min_cost:
                current_intersection = frontier_min_int
                current_intersection_cost = frontier_min_cost
            else:
                current_intersection = cost_greater_min_int
                current_intersection_cost = cost_greater_min_cost
                cost_greater_min_int = None

        path_cost += current_intersection_cost
        path.append(current_intersection)
        visited.append(current_intersection)
        #         print(f"frontier: {frontier}")
        frontier = calc_path_costs(graph, current_intersection, goal)
        frontier_min_cost = np.inf
        cost_greater_min_cost = np.inf
    #         current_intersection = frontier_min_int

    print(f"path: {path}")
    print(f"path cost: {path_cost}")
    print("==================")

    return path


def calc_path_cost(graph, intersect1, intersect2):
    if intersect2 not in graph.roads[intersect1]:
        raise ValueError("No road connects the two intersects")

    int_1_coords = graph.intersections[intersect1]
    int_2_coords = graph.intersections[intersect2]

    distance_between = calc_distance(int_1_coords, int_2_coords)

    return distance_between


def estimate_goal_distance(graph, intersection, goal):

    int_coords = graph.intersections[intersection]
    goal_coords = graph.intersections[goal]

    distance = calc_distance(int_coords, goal_coords)

    return distance


def calc_path_costs(graph, int1, goal):

    path_distances = {
        int2: calc_path_cost(graph, int1, int2) for int2 in graph.roads[int1]
    }

    # min_total_cost_int = None
    min_total_cost = np.inf
    costs = {}

    for intersect, path_cost in path_distances.items():
        goal_distance = estimate_goal_distance(graph, intersect, goal)
        total_cost = path_cost + goal_distance
        costs[intersect] = total_cost
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            # min_total_cost_int = intersect

    return costs


def calc_distance(intersect1, intersect2):

    # We will use the Pythagorean theorem to calculate straight line distance between intersections
    x_distance = intersect2[0] - intersect1[0]
    y_distance = intersect2[1] - intersect1[1]

    distance = (x_distance ** 2 + y_distance ** 2) ** 0.5

    return distance
