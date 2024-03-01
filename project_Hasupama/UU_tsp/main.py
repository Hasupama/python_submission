import random

# Cities class defined in cities.py and imported here
from cities import Cities

# Initialize cities with a predefined distance matrix
cities = Cities()
num_cities = len(cities.distances)

def tour_distance(tour, start_index):
    # Calculate the total distance of the tour starting and ending at start_index
    full_tour = [start_index] + tour + [start_index]
    return sum(cities.get_distance(full_tour[i], full_tour[i-1]) for i in range(1, len(full_tour)))

def initial_population(pop_size, start_index):
    # Generate initial population, ensuring all tours exclude the start_index
    city_indices = list(range(num_cities))
    city_indices.remove(start_index)
    return [random.sample(city_indices, num_cities-1) for _ in range(pop_size)]

def fitness(tour, start_index):
    # Fitness is the inverse of tour distance
    return 1 / tour_distance(tour, start_index)

def tournament_selection(population, start_index, k=3):
    # Select k individuals from the population and return the best
    selection = random.sample(population, k)
    best = min(selection, key=lambda x: tour_distance(x, start_index))
    return best

def ordered_crossover(parent1, parent2):
    # Perform ordered crossover between two parents
    start, end = sorted(random.sample(range(num_cities - 1), 2))
    child = [None] * (num_cities - 1)
    child[start:end] = parent1[start:end]
    for item in parent2:
        if item not in child:
            child[child.index(None)] = item
    return child

def swap_mutation(tour, mutation_rate=0.1):
    # Randomly swap two cities in the tour
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm(start_index, pop_size=100, generations=1000, mutation_rate=0.1):
    population = initial_population(pop_size, start_index)
    for _ in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = tournament_selection(population, start_index)
            parent2 = tournament_selection(population, start_index)
            child = ordered_crossover(parent1, parent2)
            child = swap_mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_tour = min(population, key=lambda x: tour_distance(x, start_index))
    return best_tour, tour_distance(best_tour, start_index)

# Specify the initial city index here
start_index = 5

best_tour, best_distance = genetic_algorithm(start_index)
ordered_city_names = [cities.get_city_name(i) for i in best_tour]
print("Best Tour starting from city", cities.get_city_name(start_index), ":", [cities.get_city_name(start_index)]
      + ordered_city_names + [cities.get_city_name(start_index)])
print("Minimum Distance:", best_distance, "km")
