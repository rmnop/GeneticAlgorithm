import random
import numpy as np 

activities = [
    "SLA100A", "SLA100B", "SLA191A", "SLA191B",
    "SLA201", "SLA291", "SLA303", "SLA304",
    "SLA394", "SLA449", "SLA451"
]

rooms = {
    "Slater 003": 45, "Roman 216": 30, "Loft 206": 75,
    "Roman 201": 50, "Loft 310": 108, "Beach 201": 60,
    "Beach 301": 75, "Logos 325": 450, "Frank 119": 60
}

timeslots = [
    "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"
]

facilitators = [
    "Lock", "Glen", "Banks", "Richards", "Shaw",
    "Singer", "Uther", "Tyler", "Numen", "Zeldin"
]

preferred_facilitators = {
    "SLA100A": ["Glen", "Lock", "Banks", "Zeldin"],
    "SLA100B": ["Glen", "Lock", "Banks", "Zeldin"],
    "SLA191A": ["Glen", "Lock", "Banks", "Zeldin"],
    "SLA191B": ["Glen", "Lock", "Banks", "Zeldin"],
    "SLA201": ["Glen", "Banks", "Zeldin", "Shaw"],
    "SLA291": ["Lock", "Banks", "Zeldin", "Singer"],
    "SLA303": ["Glen", "Zeldin", "Banks"],
    "SLA304": ["Glen", "Banks", "Tyler"],
    "SLA394": ["Tyler", "Singer"],
    "SLA449": ["Tyler", "Singer", "Shaw"],
    "SLA451": ["Tyler", "Singer", "Shaw"]
}

expected_enrollment = {
    "SLA100A": 50, "SLA100B": 50, "SLA191A": 50, "SLA191B": 50,
    "SLA201": 50, "SLA291": 50, "SLA303": 60, "SLA304": 25,
    "SLA394": 20, "SLA449": 60, "SLA451": 100
}

# Define the fitness function
def calculate_fitness(schedule):
    fitness = 0
    for activity, room, time_slot, facilitator in schedule:
        # Check if the room size is appropriate for the expected enrollment
        if rooms[room] < expected_enrollment[activity]:
            fitness -= 0.5
        elif rooms[room] > 3 * expected_enrollment[activity]:
            fitness -= 0.2
        elif rooms[room] > 6 * expected_enrollment[activity]:
            fitness -= 0.4
        else:
            fitness += 0.3

        # Check if the facilitator is preferred, listed, or other
        if facilitator in preferred_facilitators[activity]:
            fitness += 0.5
        elif facilitator in facilitators:
            fitness += 0.2
        else:
            fitness -= 0.1

    return fitness

# Genetic Algorithm Functions
def generate_random_schedule():
    schedule = []
    for activity in activities:
        room = random.choice(list(rooms.keys()))
        time_slot = random.choice(timeslots)
        facilitator = random.choice(facilitators)
        schedule.append((activity, room, time_slot, facilitator))
    return schedule

def initialize_population(population_size):
    population = [generate_random_schedule() for _ in range(population_size)]
    return population

def softmax(scores):
    exp_scores = np.exp(scores)
    return exp_scores / np.sum(exp_scores)

def random_select_parents(population, scores):
    probabilities = softmax(scores)
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    selected_population = [population[i] for i in selected_indices]
    return selected_population

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(schedule, mutation_rate):
    mutated_schedule = []
    for activity, room, time_slot, facilitator in schedule:
        if random.random() < mutation_rate:
            room = random.choice(list(rooms.keys()))
            time_slot = random.choice(timeslots)
            facilitator = random.choice(facilitators)
        mutated_schedule.append((activity, room, time_slot, facilitator))
    return mutated_schedule

def genetic_algorithm(population_size, mutation_rate, generations):
    population = initialize_population(population_size)
    for _ in range(generations):
        scores = [calculate_fitness(schedule) for schedule in population]
        selected_population = random_select_parents(population, scores)
        next_generation = []
        for i in range(0, len(selected_population), 2):
            parent1, parent2 = selected_population[i], selected_population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
        population = next_generation
    best_schedule = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_schedule)
    return best_schedule, best_fitness

if __name__ == "__main__":
    best_schedule, best_fitness = genetic_algorithm(population_size=500, mutation_rate=0.01, generations=100)
    print("Best Fitness:", best_fitness)
    print("Best Schedule:")
    for activity, room, time_slot, facilitator in best_schedule:
        print(activity, "-", room, "-", time_slot, "-", facilitator)
    
