from ga import GeneticAlgorithm


def fitness_characters(target, input_chromo):
    """
    Fitness Function for character example.

    Arguments:
        target: Our target phrase.
        input_chromo: The current chromosome under evaluation.
    """
    score = 0
    for i in range(len(target)):
        if target[i] == input_chromo[i]:
            score += 1
    return score / len(target)  # Return percentage score.


if __name__ == "__main__":
    phrase = "fire ball"  # The phrase we want the computer to match
    search_space = list(
        "abcdefghijklmnopqrstuvwxyz "
    )  # Our search space (to tell the computer its possible options)

    g_a = GeneticAlgorithm(search_space)
    g_a.initialize_population(100, len(phrase))