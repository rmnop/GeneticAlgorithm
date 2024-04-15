# GeneticAlgorithm

 
<h2>This program utilizes a genetic algorithm to optimize a space utilization schedule for activities conducted by the Sophisticated Learning Association (SLA). The goal is to assign appropriate rooms, times, and facilitators to each activity while considering various constraints and preferences.</h2>

Input:
<br>
List of activities with their expected enrollment, facilitator preferences, and other details.
List of available facilitators.
Parameters such as population size, mutation rate, and number of generations.

Output:
<br>
Best fitness score achieved.
Optimized schedule written to an output file.
Algorithm Overview:

Functionality: 
<br>
Initialization: Generate an initial population of random possible schedules.
Fitness Evaluation: Calculate the fitness score for each schedule based on the given fitness function.
Selection: Use softmax normalization to convert fitness scores into a probability distribution and select pairs of schedules for reproduction.
Crossover: Create offspring by combining genetic information from selected parent schedules.
Mutation: Introduce random mutations in the offspring according to the mutation rate.
Next Generation: Add offspring to the next-generation pool.
Repeat: Continue steps 2-6 for a specified number of generations or until improvement in average fitness is less than 1% over a certain number of generations.
Output: Print the best fitness score achieved and the optimized schedule to an output file.
Fitness Function: Considers factors such as scheduling conflicts, room size, facilitator preferences, facilitator load, and activity-specific adjustments.
Assigns scores to each activity based on the defined criteria.
