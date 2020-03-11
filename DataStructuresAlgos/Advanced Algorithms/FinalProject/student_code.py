import numpy as np
from collections import deque
from heapq import heappush, heappop
from functools import total_ordering


######################### Attempt Four (Correct Answer) #########################
# Reference: https://www.redblobgames.com/pathfinding/a-star/introduction.html


def calc_distance(intersect1, intersect2):

    # We will use the Pythagorean theorem to calculate straight line distance between intersections
    x_distance = intersect2[0] - intersect1[0]
    y_distance = intersect2[1] - intersect1[1]

    distance = (x_distance ** 2 + y_distance ** 2) ** 0.5

    return distance


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


@total_ordering
class Intersection:
    def __init__(self, num, priority):
        self.num = num
        self.priority = priority

    def get_num(self):
        return self.num

    def __eq__(self, other):
        return self.priority == other

    def __lt__(self, other):
        return self.priority < other

    def __repr__(self):
        s = "\n==========\n"
        s += f"Intersect: {self.num}\n"
        s += f"Priority: {self.priority}\n"
        s += "=========="
        return s


def a_star(graph, start, goal):

    if start == goal:
        return [start]

    start_int = Intersection(start, 0)
    frontier = []
    heappush(frontier, start_int)
    intersect_priors = {}
    intersect_priors[start] = None
    cumulative_cost = {}
    cumulative_cost[start] = 0

    while len(frontier) != 0:
        current_intersect = heappop(frontier)
        int_num = current_intersect.get_num()
        if int_num == goal:
            break

        for next_int in graph.roads[int_num]:
            new_cost = cumulative_cost[int_num] + calc_path_cost(
                graph, int_num, next_int
            )
            if (next_int not in cumulative_cost) or (
                new_cost < cumulative_cost[next_int]
            ):
                cumulative_cost[next_int] = new_cost
                priority = new_cost + estimate_goal_distance(graph, next_int, goal)
                next_intersection = Intersection(next_int, priority)
                heappush(frontier, next_intersection)
                intersect_priors[next_int] = current_intersect

    path = deque()
    current = intersect_priors[goal]
    path.appendleft(goal)
    while current.get_num() != start:
        path_int = current.get_num()
        path.appendleft(path_int)
        current = intersect_priors[path_int]
    path.appendleft(start)

    return list(path)


######################### DISREGARD: PRIOR ATTEMPTS #########################


######################### Attempt Three #########################


def dijkstra(graph, start_node, end_node):
    distance_dict = {node: np.inf for node in graph.intersections.keys()}
    print(distance_dict)
    shortest_path_to_node = {}
    # shortest_path = defaultdict(list)

    distance_dict[start_node] = 0
    while distance_dict:
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[
            0
        ]
        print(f"Current node: {current_node}")
        print(f"Node distance: {node_distance}")
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)
        # shortest_path[current_node].append(current_node)

        for node in graph.roads[current_node]:
            if node in distance_dict:
                path_cost = calc_path_cost(graph, current_node, node)
                new_node_distance = node_distance + path_cost
                print(f"Node: {node}")
                print(f"Path cost: {path_cost}")
                print(f"New distance: {new_node_distance}")
                if distance_dict[node] > new_node_distance:
                    distance_dict[node] = new_node_distance

    print(shortest_path)
    print(shortest_path_to_node)
    return shortest_path_to_node[end_node]


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

    def add_priors(self, prior):
        self.prior_intersections.append(prior)
        self.prior_intersections.extend(prior.get_priors())
        self.total_cost = self.total_cost + sum(
            [
                i.get_path_cost()
                for i in self.prior_intersections
                if i.get_total_cost() is not None
            ]
        )

    def get_priors(self):
        if len(self.prior_intersections) == 0:
            return []
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
        s += f"Priors: {[i.get_num() for i in self.prior_intersections]}\n"
        s += "=========="
        return s


def the_shortest_path(graph, start, goal):

    if start == goal:
        return [start]

    pqueue = []
    visited = []
    paths = []

    start_intersect = Intersect(start, 0)
    heappush(pqueue, start_intersect)
    # min_goal_cost = np.inf
    print(f"Start intersection: {start_intersect}")

    current_intersect = None
    while len(pqueue) != 0:
        prior_intersect = current_intersect
        current_intersect = heappop(pqueue)
        print(f"Intersection to be expanded: {current_intersect.get_num()}")
        intersection_costs = expand_intersect(
            graph, current_intersect.get_num(), goal, visited
        )
        print(f"Intersection costs: {intersection_costs}")
        if prior_intersect is not None:
            current_intersect.add_priors(prior_intersect)
        if current_intersect.get_num() != goal:
            print(f"Expanded intersection: {current_intersect}")
            visited.append(current_intersect.get_num())
            print(f"Current visited: {[i for i in visited]}")
            for intersection in intersection_costs:
                if intersection.get_num() not in [i.get_num() for i in pqueue]:
                    heappush(pqueue, intersection)
            print(f"Current frontier: {[i.get_num() for i in pqueue]}")
        else:
            paths.append(current_intersect)
            current_intersect = heappop(pqueue)

    return paths


def expand_intersect(graph, int1, goal, visited):

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


# def calc_path_cost(graph, intersect1, intersect2):
#     if intersect2 not in graph.roads[intersect1]:
#         raise ValueError("No road connects the two intersects")

#     int_1_coords = graph.intersections[intersect1]
#     int_2_coords = graph.intersections[intersect2]

#     distance_between = calc_distance(int_1_coords, int_2_coords)

#     return distance_between


# def estimate_goal_distance(graph, intersection, goal):

#     int_coords = graph.intersections[intersection]
#     goal_coords = graph.intersections[goal]

#     distance = calc_distance(int_coords, goal_coords)

#     return distance


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


# def calc_distance(intersect1, intersect2):

#     # We will use the Pythagorean theorem to calculate straight line distance between intersections
#     x_distance = intersect2[0] - intersect1[0]
#     y_distance = intersect2[1] - intersect1[1]

#     distance = (x_distance**2 + y_distance**2)**.5

#     return distance
