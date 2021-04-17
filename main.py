from ga import GeneticAlgorithm

if __name__ == "__main__":
    phrase = "fire ball"  # The phrase we want the computer to match
    search_space = list(
        "abcdefghijklmnopqrstuvwxyz "
    )  # Our search space (to tell the computer its possible options)

    g_a = GeneticAlgorithm(search_space)
    g_a.initialize_population(100, len(phrase))