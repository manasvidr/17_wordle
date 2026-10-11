import random
from words import WORDS
from feedback import evaluate

VALID_LENGTHS = (4, 5, 6)
MAX_GUESSES = 6


class WordleGame:
    def __init__(self, length=5):
        if length not in VALID_LENGTHS:
            raise ValueError(f"Unsupported word length: {length}")
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def run(self):
        print(f"Wordle - {self.length} letters, {MAX_GUESSES} guesses.")
        won = False
        while len(self.history) < MAX_GUESSES:
            guess = input("> ").strip().lower()
            if guess == "q":
                break
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue  # invalid input does not consume a turn
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            self._print_history()
            if guess == self.target:
                won = True
                break
        self._print_summary(won)

    def _print_history(self):
        print(f"-- Guess history ({len(self.history)}/{MAX_GUESSES}) --")
        for i, (guess, feedback) in enumerate(self.history, start=1):
            row = " ".join(f"{ch.upper()}:{mark}" for ch, mark in zip(guess, feedback))
            print(f"  {i}. {row}")

    def _print_summary(self, won):
        print("\n--- Session summary ---")
        if won:
            n = len(self.history)
            print(f"Result: WIN in {n} guess{'es' if n != 1 else ''}.")
        elif len(self.history) == MAX_GUESSES:
            print("Result: LOSS (out of guesses).")
        else:
            print("Result: QUIT.")
        print(f"Target word: {self.target.upper()}")
        self._print_history()
