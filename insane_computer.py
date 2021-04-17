import random
import time


def run_brute_force(phrase, search_space):
    guessed_phrase = ""  # The current phrase guessed
    iterations = 0  # To keep a count on the number of iterations

    start_time = time.time()  # To keep a track of the elapsed time

    while guessed_phrase != phrase:
        guessed_phrase = ""
        for _ in range(len(phrase)):
            guessed_letter = random.choice(
                search_space
            )  # Choose a letter from the search space
            guessed_phrase += guessed_letter  # Add the letter to the current phrase
        iterations += 1
        print(
            f"Current Iteration: {iterations} | Phrase Guessed: {guessed_phrase} | Total Time Elapsed: {(time.time() - start_time):.3f}"
        )

    print(f"Final Output: {guessed_phrase}")
    print(f"Total Iterations Taken: {iterations}")


if __name__ == "__main__":

    phrase = "fire ball"  # The phrase we want the computer to match
    search_space = list(
        "abcdefghijklmnopqrstuvwxyz "
    )  # Our search space (to tell the computer its possible options)

    run_brute_force(phrase, search_space)