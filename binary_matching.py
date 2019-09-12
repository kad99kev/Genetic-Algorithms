import random
from time import sleep
import os

POP_SIZE = 15
TARGET_CHROMO = []
MUT_RATE = 0.1 # 10%


class Chromosome:
    def __init__(self):
        self.genes = []
        self.score = 0
        self.fitness = 0
        for i in range(len(TARGET_CHROMO)):
            if random.random() >= 0.5:
                self.genes.append(1)
            else:
                self.genes.append(0)

    def calc_score(self):
        self.score = 0
        for ind, ele in enumerate(self.genes):
            if ele == TARGET_CHROMO[ind]:
                self.score += 1

    def return_genes(self):
        return "".join(map(lambda x: str(x), self.genes))

class Population:
    def __init__(self, size):
        self.population = []
        for i in range(size):
            self.population.append(Chromosome())

    def return_chromosomes(self):
        self.population.sort(key=lambda x: x.score, reverse=True)
        return self.population


class GeneticAlgorithm:

    @staticmethod
    def evolve(pop):
        new_pop = Population(0)
        GeneticAlgorithm._normalize_fitness(pop)
        for i in range(POP_SIZE):
            parent1 = GeneticAlgorithm._pick_one(pop)
            parent2 = GeneticAlgorithm._pick_one(pop)
            new_pop.population.append(GeneticAlgorithm._reproduce(parent1, parent2))
        return new_pop

    @staticmethod
    def _reproduce(parent1, parent2):
        child = Chromosome()
        midpoint = int(random.randrange(len(parent1.genes)))
        for i in range(len(parent1.genes)):
            if i < midpoint:
                child.genes[i] = parent1.genes[i]
            else:
                child.genes[i] = parent2.genes[i]
        child = GeneticAlgorithm._mutate(child)
        child.calc_score()
        return child



    @staticmethod
    def _mutate(child):
        for ind, ele in enumerate(child.genes):
            if random.random() < MUT_RATE:
                if ele == 1:
                    child.genes[ind] = 0
                else:
                    child.genes[ind] = 1
        return child

    @staticmethod
    def _normalize_fitness(pop):
        sum = 0
        chromos = pop.return_chromosomes()
        for ele in chromos:
            ele.calc_score()
            sum += ele.score

        for ele in chromos:
            ele.fitness = ele.score / sum

    @staticmethod
    def _pick_one(pop):
        index = 0
        r = random.random()

        while r > 0:
            r -= pop.population[index].fitness
            index += 1

        index -= 1
        return pop.population[index]


def print_generation(pop, generation):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generation Number: {generation}")
    for ind, ele in enumerate(pop.return_chromosomes()):
        print(f"Chromosome {ind+1}: Genes = {ele.return_genes()} | Score = {ele.score}")
    sleep(0.1)

def main():

    # Initalizing a random pattern
    for i in range(15):
        if random.random() >= 0.5:
            TARGET_CHROMO.append(1)
        else:
            TARGET_CHROMO.append(0)

    print("Target Pattern: ", *TARGET_CHROMO, sep = '')
    sleep(3)

    pop = Population(POP_SIZE)
    gen_num = 0
    print_generation(pop, gen_num)

    while  pop.return_chromosomes()[0].score < len(TARGET_CHROMO):
        pop = GeneticAlgorithm.evolve(pop)
        gen_num += 1
        print_generation(pop, gen_num)

main()
