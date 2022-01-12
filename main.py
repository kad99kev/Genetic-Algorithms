import time
from tqdm import tqdm
import matplotlib.pyplot as plt
from ga import GeneticAlgorithm


if __name__ == "__main__":

    phrase = "fire ball"  # The phrase we want the computer to match
    search_space = list(
        "abcdefghijklmnopqrstuvwxyz "
    )  # Our search space (to tell the computer its possible options)

    g_a = GeneticAlgorithm(search_space)

    # Perform experiment.
    run_iters = []
    run_time = []
    exp_start = time.time()
    for i in tqdm(range(10)):
        start_time = time.time()
        curr_iter = g_a.run(phrase)
        time_taken = time.time() - start_time
        # Append iterations taken.
        run_iters.append(curr_iter)
        # Append time taken.
        run_time.append(time_taken)

    print(f"Total time taken to run experiment: {time.time() - exp_start:.2f} seconds")

    fig, ax = plt.subplots(1, 2)
    ax[0].plot(range(len(run_iters)), run_iters)
    ax[1].plot(range(len(run_time)), run_time)
    fig.suptitle("Experiment Results")
    plt.show()
