import random
from prepare import Rectangle
from brute_force import BruteForceAlgorithm
from map import MapAlgorithm
from persistent_segment_tree import PersistentTreeAlgorithm
from time import perf_counter_ns
import json

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def powmod(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def generate_rectangles(N):
    rectangles = []
    for i in range(N):
        rectangles.append(Rectangle(10 * i, 10 * i, 10 * (2 * N - i), 10 * (2 * N - i)))
    return rectangles

def generate_queries(N, M):
    queries = []
    prime_n1 = 10104569
    prime_n2 = 10150697
    for j in range(M):
        queries.append(Point(powmod(prime_n1 * j, 31, 20 * N), powmod(prime_n2 * j, 31, 20 * N)))
    return queries

def test():
    results = []
    n = 1
    m = 1
    max_rect = 12
    max_point = 12

    for rect in range(max_rect + 1):
        rectangles = generate_rectangles(n)
        print(f"Результат для {n} прямоугольников (BruteForceAlgorithm, MapAlgorithm, PersistentTreeAlgorithm):")
        print("Подготовка данных:")

        algorithm_results = {}

        # Measure Brute Force Algorithm
        task = BruteForceAlgorithm()
        start = perf_counter_ns()
        task.preparation(rectangles)
        brute_force_prep_time = perf_counter_ns() - start
        algorithm_results["Brute force"] = {"prep_time": brute_force_prep_time, "query_time": 0}

        # Measure Map Algorithm
        task = MapAlgorithm()
        start = perf_counter_ns()
        task.preparation(rectangles)
        map_prep_time = perf_counter_ns() - start
        algorithm_results["Map"] = {"prep_time": map_prep_time, "query_time": 0}

        # Measure Persistent Segment Tree Algorithm
        task = PersistentTreeAlgorithm()
        start = perf_counter_ns()
        task.preparation(rectangles)
        tree_prep_time = perf_counter_ns() - start
        algorithm_results["Persistent segment tree"] = {"prep_time": tree_prep_time, "query_time": 0}

        print(f"{brute_force_prep_time} ns {map_prep_time} ns {tree_prep_time} ns")

        print("Запросы:")

        for point in range(max_point + 1):
            queries = generate_queries(n, m)

            # Measure Brute Force Algorithm
            task = BruteForceAlgorithm()
            task.preparation(rectangles)
            start = perf_counter_ns()
            for p in queries:
                task.query(p.x, p.y)
            brute_force_query_time = perf_counter_ns() - start
            algorithm_results["Brute force"]["query_time"] += brute_force_query_time

            # Measure Map Algorithm
            task = MapAlgorithm()
            task.preparation(rectangles)
            start = perf_counter_ns()
            for p in queries:
                task.query(p.x, p.y)
            map_query_time = perf_counter_ns() - start
            algorithm_results["Map"]["query_time"] += map_query_time

            # Measure Persistent Segment Tree Algorithm
            task = PersistentTreeAlgorithm()
            task.preparation(rectangles)
            start = perf_counter_ns()
            for p in queries:
                task.query(p.x, p.y)
            tree_query_time = perf_counter_ns() - start
            algorithm_results["Persistent segment tree"]["query_time"] += tree_query_time

            print(f"{m}т {brute_force_query_time} ns {map_query_time} ns {tree_query_time} ns")

            m *= 2

        results.append((n, algorithm_results))
        print("\n\n\n")
        m = 1
        n *= 2



if __name__ == "__main__":
    ALGORITHMS = {
        "Brute force": BruteForceAlgorithm,
        "Map": MapAlgorithm,
        "Persistent segment tree": PersistentTreeAlgorithm
    }

    test()

