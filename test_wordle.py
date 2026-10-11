"""Quick self-check for the duplicate-letter fix and the guess-handling rules.
Run: python test_wordle.py
"""
from unittest.mock import patch

from feedback import evaluate
from game import WordleGame, VALID_LENGTHS
from words import WORDS


def test_duplicate_letter_capped_by_target_count():
    # target has one 'r' (used by the green match at index 4); the guess's other
    # two 'r's must be gray, not yellow.
    assert evaluate("boxer", "rarer") == ["gray", "gray", "gray", "green", "green"]


def test_duplicate_letter_covered_when_target_has_enough():
    assert evaluate("eerie", "sheer") == ["gray", "gray", "yellow", "yellow", "yellow"]


def test_exact_match_is_all_green():
    assert evaluate("apple", "apple") == ["green"] * 5


def test_absent_letters_are_all_gray():
    assert evaluate("apple", "zzzzz") == ["gray"] * 5


def test_invalid_guess_does_not_consume_a_turn():
    game = WordleGame(length=5)
    game.target = "apple"
    inputs = iter(["bad", "zz", "apple"])  # two invalid lengths, then the win
    with patch("builtins.input", lambda *_: next(inputs)):
        game.run()
    assert len(game.history) == 1, "invalid attempts must not be recorded as guesses"
    assert game.history[0][0] == "apple"


def test_losing_after_six_valid_guesses():
    game = WordleGame(length=5)
    game.target = "apple"
    inputs = iter(["grape", "crane", "stare", "steam", "stone", "plant"])
    with patch("builtins.input", lambda *_: next(inputs)):
        game.run()
    assert len(game.history) == 6


def test_quitting_stops_immediately():
    game = WordleGame(length=5)
    inputs = iter(["q"])
    with patch("builtins.input", lambda *_: next(inputs)):
        game.run()
    assert len(game.history) == 0


def test_all_three_lengths_have_word_lists():
    for length in VALID_LENGTHS:
        assert any(len(w) == length for w in WORDS), f"no words of length {length}"


def test_four_and_six_letter_games_work():
    for length in (4, 6):
        game = WordleGame(length=length)
        assert len(game.target) == length
        assert evaluate(game.target, game.target) == ["green"] * length


if __name__ == "__main__":
    test_duplicate_letter_capped_by_target_count()
    test_duplicate_letter_covered_when_target_has_enough()
    test_exact_match_is_all_green()
    test_absent_letters_are_all_gray()
    test_invalid_guess_does_not_consume_a_turn()
    test_losing_after_six_valid_guesses()
    test_quitting_stops_immediately()
    test_all_three_lengths_have_word_lists()
    test_four_and_six_letter_games_work()
    print("All tests passed.")
