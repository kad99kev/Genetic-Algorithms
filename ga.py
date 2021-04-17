import random
from typing import List


class GeneticAlgorithm:
    """
    Class for a Genetic Algorithm.

    Arguments:
        search_space: The space of all the possible solutions.
    """

    def __init__(self, search_space: List):
        self.search_space = search_space

    def initialize_population(self, population_size: int, chromosome_size: int):
        """
        Function to initialize the population with a given population size and a chromosome length.

        Arguments:
            population_size: Size of the population.
            chromosome_size: Size of the chromosome (the length of the target chromosome).
        """

        self.population = []
        for _ in range(population_size):
            chromo = [random.choice(self.search_space) for __ in range(chromosome_size)]
            self.population.append(chromo)
