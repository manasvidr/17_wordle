from collections import Counter


def evaluate(target, guess):
    """Standard Wordle feedback: exact matches resolve first, and each occurrence
    in the target can satisfy at most one occurrence in the guess."""
    result = ["gray"] * len(guess)
    remaining = Counter(target)

    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[ch] -= 1

    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if remaining[ch] > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result
