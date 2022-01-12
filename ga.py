import random


class GeneticAlgorithm:
    """
    Class for a Genetic Algorithm.

    Arguments:
        search_space: The space of all the possible solutions.
        population_size: Size of the population.
    """

    def __init__(self, search_space, population_size=100, mutation_rate=0.01):
        self.search_space = search_space
        self.population_size = population_size
        self.mutation_rate = mutation_rate

    def _initialize_population(self, chromosome_size):
        """
        Function to initialize the population with a given population size and a chromosome length.

        Arguments:
            chromosome_size: Size of the chromosome (the length of the target chromosome).
        """

        self.population = []  # This will be our population attribute for the class
        for _ in range(self.population_size):
            chromo = [random.choice(self.search_space) for __ in range(chromosome_size)]
            self.population.append(chromo)

    def _fitness_function(self, input_chromo):
        """
        Fitness Function for character example.

        Arguments:
            target: Our target phrase.
            input_chromo: The current chromosome under evaluation.
        """
        score = 0
        for i in range(len(self.target)):
            if self.target[i] == input_chromo[i]:
                score += 1
        return score / len(self.target)  # Return percentage score.

    def _roulette_wheel_selection(self):
        """
        Roulette Wheel Selection algorithm.
        """
        # Calculate the fitness for each chromosome in the population.
        self.population_fitness = [
            self._fitness_function(chromo) for chromo in self.population
        ]

        # Calculate the probability for each chromosome.
        probabilities = [
            chromo_fitness / sum(self.population_fitness)
            for chromo_fitness in self.population_fitness
        ]

        # Return a chromosome based on its probability.
        return random.choices(self.population, weights=probabilities)[0]

    def _reproduce(self, parent_1, parent_2):
        """
        Performs crossover with two parents.

        Arguments:
            parent_1: The first parent.
            parent_2: The second parent.
        """
        child = ""  # Initialise and empty child.
        midpoint = int(
            random.randrange(len(self.target))
        )  # Calculate the midpoint for crossover
        for i in range(len(parent_1)):
            if i <= midpoint:
                child += parent_1[i]
            else:
                child += parent_2[i]
        return child

    def _mutate(self, child):
        """
        Performs mutation.

        Arguments:
            child: The child to be mutated.
        """
        child_list = list(child)
        for idx in range(len(child)):
            if random.random() < self.mutation_rate:
                child_list[idx] = random.choice(self.search_space)
        return "".join(child_list)

    def _evolve(self):
        new_population = []  # Our new (and evolved) population.
        for _ in range(len(self.population)):
            # Using roulette wheel selection pick out two parents.
            parent_1 = self._roulette_wheel_selection()
            parent_2 = self._roulette_wheel_selection()
            # Create a new child and add it to the new population.
            child = self._reproduce(parent_1, parent_2)
            # Mutate child.
            child = self._mutate(child)
            # Add new child to population.
            new_population.append(child)
        self.population = new_population

    def _evaluate(self):

        # If algorithm has not run yet.
        if not hasattr(self, "population_fitness"):
            return False

        # Argument sort based on fitness.
        # Reference: https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
        fitness_idx = sorted(
            range(len(self.population_fitness)),
            key=self.population_fitness.__getitem__,
            reverse=True,
        )

        # We check if the chromosome with the highest fitness is a match.
        if self.population[fitness_idx[0]] == self.target:
            return True

        return False

    def run(self, target, debug_steps=None):
        # Initialise population.
        self._initialize_population(len(target))
        self.target = target
        self.iter_num = 1
        while not self._evaluate():
            # Evaluate and evolve.
            self._evolve()
            # Perform debugging.
            if debug_steps is not None:
                if self.iter_num % debug_steps == 0:
                    print(self.population)
            self.iter_num += 1
        return self.iter_num
