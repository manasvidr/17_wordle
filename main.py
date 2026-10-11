from game import WordleGame, VALID_LENGTHS


def choose_length():
    options = ", ".join(str(n) for n in VALID_LENGTHS)
    while True:
        raw = input(f"Choose word length ({options}; default 5): ").strip()
        if raw == "":
            return 5
        if raw.isdigit() and int(raw) in VALID_LENGTHS:
            return int(raw)
        print(f"Enter one of: {options}.")


if __name__ == "__main__":
    WordleGame(choose_length()).run()
