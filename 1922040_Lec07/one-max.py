import random
import copy

LIST_SIZE = 10
POPULATION_SIZE = 10
GENERATION = 25
MUTATE = 0.1
SELECT_RATE = 0.5
# calc_fitness
# sort_fitness
# selection
# crossover
# mutation
def print_population(population):
    for individual in population:
        print(individual)
print("----")
    
def print_individual(individual):
    print(individual)
print("----")

def calc_distance(individual):
    return sum(individual)

def sort_fitness(population):
    fp = []
    for individual in population:
        fitness = calc_distance(individual)
        fp.append((fitness, individual))
    fp.sort(reverse=True)

    sorted_population = []

    for fitness, individual in fp:
        sorted_population.append(individual)
    print_population(sorted_population)
    return sorted_population

def selection(population):
    sorted_population = sort_fitness(population)
    n = int(POPULATION_SIZE * SELECT_RATE)
    return sorted_population[0:n]

def crossover(ind1, ind2):
    r1 = random.randint(0, LIST_SIZE - 1)
    r2 = random.randint(r1 + 1, LIST_SIZE)
    ind = copy.deepcopy(ind1)
    ind[r1:r2] = ind2[r1:r2]
    return ind

def mutation(ind1):
    ind2 = copy.deepcopy(ind1)
    for i in range(LIST_SIZE):
        if random.random() < MUTATE:
            ind2[i] = random.randint(0, 1)
    return ind2

if __name__ == "__main__":
    population = []
    for i in range(POPULATION_SIZE):
        individual = []
        for j in range(LIST_SIZE):
            individual.append(random.randint(0, 1))
        population.append(individual)

    for generation in range(GENERATION):
        print(str(generation + 1) + " generation")
        print_population(population)
        population = selection(population)
        print_population(population)
        n = POPULATION_SIZE - len(population)
        for i in range(n):
            r1 = random.randint(0, len(population) - 1)
            r2 = random.randint(0, len(population) - 1)
            individual = crossover(population[r1], population[r2])
            print_individual(individual)
            individual = mutation(individual)
            print_individual(individual)
            population.append(individual)
        print_population(population)